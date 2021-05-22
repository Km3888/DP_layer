from setuptools import setup, Extension
from torch.utils import cpp_extension


setup(name='dp_c',
      ext_modules=[cpp_extension.CppExtension('dp_c', ['dp_c.cpp'])],
      cmdclass={'build_ext': cpp_extension.BuildExtension})


