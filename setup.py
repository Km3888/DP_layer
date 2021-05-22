from setuptools import setup, Extension
from torch.utils import cpp_extension


setup(name='dp_layer',
      ext_modules=[cpp_extension.CppExtension('dp_layer', ['dp_layer.cpp'])],
      cmdclass={'build_ext': cpp_extension.BuildExtension})


