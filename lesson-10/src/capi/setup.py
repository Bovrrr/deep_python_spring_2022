from setuptools import setup, Extension

setup(
    name='utils',
    version='1.2',
    description="Different utils",
    author="Anton Kukhtichev",
    ext_modules = [
        Extension('utils', ['utils.c'])
    ]
)
