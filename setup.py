try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

from textwrap import dedent, fill

def format_desc(desc):
    return fill(dedent(desc), 200)

def format_trove(trove):
    return dedent(trove).strip().split('\n')

def file_contents(filename):
    with open(filename) as f:
        return f.read()

setup(
    name = "terminable_thread",
    version = "0.7",
    maintainer = "Ted Tibbetts",
    maintainer_email = "intuited@gmail.com",
    url = "http://github.com/intuited/terminable_thread",
    description = format_desc("""
        Provides a subclass of Thread with facilities to
        raise an exception in the thread
        or terminate the thread from another thread.
        """),
    long_description = file_contents('README.rst'),
    classifiers = format_trove("""
        Development Status :: 3 - Alpha
        Intended Audience :: Developers
        License :: Freely Distributable
        Operating System :: OS Independent
        Programming Language :: Python
        Programming Language :: Python :: 2
        Topic :: Software Development :: Libraries :: Python Modules
        Topic :: Utilities
        """),
    license = "http://sam.zoy.org/wtfpl/",
    keywords = 'threading multithreading'.split(' '),
    packages = ['terminable_thread', 'terminable_thread.test'],
    package_dir = {'terminable_thread': ''},
    test_suite = 'terminable_thread.test.suite',
    )
