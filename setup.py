from setuptools import setup
from Cython.Build import cythonize

setup(name="qpt_generator",
      version="1.0",
      description="Question Paper Template Generator",
      author="Niraj Kamdar",
      ext_modules=cythonize('qpt_generator.pyx'))
