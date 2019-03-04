"""Homework6: create a class, representing  money in different currencies"""


class Money:
    """Class, representing  money in different currencies."""

    convert_indexes = {"RUB-BYN": 0.0325,
                       "USD-BYN": 2.138,
                       "EUR-BYN": 2.432,
                       "JPY-BYN": 0.019,

                       "BYN-RUB": 30.7692,
                       "USD-RUB": 65.7846,
                       "EUR-RUB": 74.8308,
                       "JPY-RUB": 0.59,

                       "BYN-USD": 0.4677,
                       "RUB-USD": 0.0152,
                       "EUR-USD": 1.1375,
                       "JPY-USD": 0.009,

                       "BYN-EUR": 0.4112,
                       "RUB-EUR": 0.0134,
                       "USD-EUR": 0.8791,
                       "JPY-EUR": 0.0079,

                       "BYN-JPY": 51.84,
                       "RUB-JPY": 1.69,
                       "USD-JPY": 110.44,
                       "EUR-JPY": 126.58}

    def __init__(self, value, currency: str = "USD"):
        """
        :param value: amount of money
        :param currency: name of currency
        """
        self.value = value
        self.currency = currency

    def __repr__(self):

        return "{} {}".format(self.value, self.currency)

    def __add__(self, other):

        if isinstance(other, int):
            return self

        self.convert(other)

        return Money(self.value + other.value, self.currency)

    def __radd__(self, other):

        return self.__add__(other)

    def __mul__(self, other):

        return Money(self.value * other, self.currency)

    def __rmul__(self, other):

        return self.__mul__(other)

    def convert(self, other):
        """Convert money of currencies, listed in 'convert_indexes' dict

        :param other: instance of Money class
        """
        currencies_to_convert = other.currency + "-" + self.currency

        if currencies_to_convert in Money.convert_indexes:
            other.value = \
                Money.convert_indexes[currencies_to_convert] * other.value
            other.currency = self.currency
        else:
            print("Can't convert such currencies as {}".
                  format(currencies_to_convert))
            exit(0)


if __name__ == "__main__":

    x = Money(10, "BYN")
    y = Money(11)
    z = Money(12.34, "EUR")

    print(z + 3.11 * x + y * 0.8)

    lst = [Money(10, "BYN"), Money(11), Money(12.01, "JPY")]
    s = sum(lst)

    print(s)
