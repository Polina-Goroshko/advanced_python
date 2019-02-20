from distutils.core import setup
import os


def read(file_name):
    return open(os.path.join(os.path.dirname(__file__),
                             file_name)).read()


setup(
    name='Homework10',
    version='0.1',
    author='Polina Goroshko',
    author_email='Polina_Goroshko@epam.com',
    url='http://www.epam.com',
    scripts=['start_app.py', ],
    packages=['hw10', ],
    long_description=read('README.md'),
)
