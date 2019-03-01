#!/usr/bin/env python

"""
setup.py file for fastfiz
"""

from distutils.core import setup, Extension

fastfiz_module = Extension(
        '_fastfiz',
        sources=['fastfiz/swig/fastfiz.i',
                 'fastfiz/src/FastFiz.cpp',
                 'fastfiz/src/Noise.cpp',
                 'fastfiz/src/Rules.cpp',
                 'fastfiz/src/Stopwatch.cpp'],
                 include_dirs=['fastfiz/include'],
                 swig_opts=['-c++', '-Wall', '-Ifastfiz/include', '-outdir', '.'],
                 extra_compile_args=['-std=c++11'],
                 extra_link_args=['-lgsl', '-lgslcblas'],
)

setup(
    name = 'fastfiz',
    description = "fastfiz Billiards engine wrapper",
    ext_modules = [fastfiz_module],
    py_modules = ["fastfiz"],
)
