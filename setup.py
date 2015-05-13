from distutils.core import setup

setup(
    name='footballdb',
    version='0.0.1',
    author='Josh Daly',
    author_email='joshua.daly@uqconnect.edu.au',
    packages=['footballdb'],
    scripts=['bin/footballdb'],
    url='http://pypi.python.org/pypi/footballdb/',
    license='GPLv3',
    description='footballdb',
    long_description=open('README.md').read(),
    install_requires=[],
)

