from setuptools import setup, find_packages

setup(
    name='nba_analytica',
    version='0.1.1',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    author='Adam Lipson',
    author_email='lipson.adam13@gmail.com',
    description='A package to fetch NBA player stats.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Adamlip1334/nba-analytica',
    license='MIT',
)
