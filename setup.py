from setuptools import setup, find_packages

setup(
    name = 'login_szu',
    version = '0.0.2',
    keywords = ('login_szu', 'szu'),
    description = 'A package for login szu',
    license = 'MIT License',
    install_requires = ['django>=1.5','lxml>=3.3.4','requests>=2.2.1'],

    author = 'jimczj',
    author_email = 'jimczj@gmail.com',

    packages = find_packages(),
    platforms = 'any',
)