from setuptools import setup, find_packages


install_requires = [
    'pandas',
    'numpy',
    ]



setup (
    name             = 'toy', 
    packages=find_packages(where='src'),
    version          = '1.0.0',
    install_requires = install_requires,
    author           = 'jhahn',
    author_email     = 'jhahncs@gmail.com',
    description      = 'Desc'
)