from __future__ import with_statement

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def get_version():
    with open('transtool/version.txt') as f:
        return f.read().strip()


def get_readme():
    try:
        with open('README.rst') as f:
            return f.read().strip()
    except IOError:
        return ''

setup(
    name='transtool',
    version=get_version(),
    description='transtool is dictionary-rewritting-base general-purpose translation copilier',
    long_description=get_readme(),
    author='Jeong YunWon',
    author_email='jeong+transtool@youknowone.org',
    url='https://github.com/youknowone/transtool',
    packages=(
        'transtool',
        'transtool/dictionary',
        'transtool/parser',
    ),
    package_data={
        'transtool': ['version.txt']
    },
    install_requires=[
        'distribute',
        'prettyexc',
    ],
)
