from distutils.core import setup
from Cython.Build import cythonize

setup(name='bspt', ext_modules=cythonize("bspt_slow.pyx"))
