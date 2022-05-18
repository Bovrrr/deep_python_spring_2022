from setuptools import setup, Extension
from Cython.Build import cythonize

setup(
    version='1.0',
    ext_modules=cythonize(['cutils.pyx'])
)
