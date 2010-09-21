try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

from textwrap import dedent, fill

def format_desc(desc):
    return fill(dedent(desc), 200)

def format_classifiers(classifiers):
    return dedent(classifiers).strip().split('\n')

setup(
    name = "terminable_thread",
    version = "0.6.4",
    maintainer = "Ted Tibbetts",
    maintainer_email = "intuited@gmail.com",
    url = "http://github.com/intuited/terminable_thread",
    description = format_desc("""
        Provides a subclass of Thread with facilities to
        raise an exception in the thread
        or terminate the thread from another thread.
        """),
    classifiers = format_classifiers("""
        Development Status :: 3 - Alpha
        Intended Audience :: Developers
        License :: OSI Approved :: GNU General Public License (GPL)
        Operating System :: OS Independent
        Programming Language :: Python
        Programming Language :: Python :: 2
        Topic :: Software Development :: Libraries :: Python Modules
        Topic :: Utilities
        """),
    keywords = 'threading multithreading'.split(' '),
    packages = ['terminable_thread', 'terminable_thread.test'],
    package_dir = {'terminable_thread': ''},
    test_suite = 'terminable_thread.test.suite',
    )
