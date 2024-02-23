from setuptools import setup, find_packages

setup(
    name='nba_stats',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    author='Adam Lipson',
    author_email='lipson.adam13@gmail.com',
    description='A package to fetch NBA player stats.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/nba_stats',
    license='MIT',
)
