from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='wiki_insight',
    version='0.1.0',
    description='WikiInsight coding challenge for Tranzact',
    long_description=readme,
    author='Kevin Pereda',
    author_email='kevin.pereda26@gmail.com',
    url='https://github.com/',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

