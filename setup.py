from distutils.core import setup
from Cython.Build import cythonize

setup(name='bspt_slow', ext_modules=cythonize("bspt_slow.pyx"))
