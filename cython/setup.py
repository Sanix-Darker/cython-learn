# setup.py
from distutils.core import setup
from setuptools import find_packages, setup, Extension

try:
    from Cython.Build import cythonize
    ext_modules = cythonize(
        [
            Extension(
                "*", 
                ["*.pyx"],
                include_dirs=[],
                libraries=[]
            ),
        ],
        compiler_directives = {
            'language_level' : "3"
        }
    )
except ImportError:
    ext_modules = None

setup(
    name = 'test',
    version = '0.1',
    packages = find_packages(),
    ext_modules = ext_modules
)
