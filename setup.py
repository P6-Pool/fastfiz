#!/usr/bin/env python

"""
setup.py file for fastfiz
"""

from setuptools import setup, Extension
from setuptools.command.build_py import build_py as _build_py


class build_py(_build_py):
    def run(self):
        self.run_command("build_ext")
        return super().run()


fastfiz_module = Extension(
        '_fastfiz',
        sources=['fastfiz/swig/fastfiz.i',
                 'fastfiz/src/FastFiz.cpp',
                 'fastfiz/src/Noise.cpp',
                 'fastfiz/src/Rules.cpp',
                 'fastfiz/src/Stopwatch.cpp',
                 'fastfiz/src/LogFile.cpp',
                 ],
                 include_dirs=['fastfiz/include'],
                 swig_opts=['-c++', '-Wall', '-Ifastfiz/include', '-outdir', '.'],
                 extra_compile_args=['-std=c++11'],
                 extra_link_args=['-lgsl', '-lgslcblas'],
)


setup(
    name='fastfiz',
    version='0.0.1',
    description="fastfiz Billiards engine wrapper",
    cmdclass={'build_py': build_py},
    ext_modules=[fastfiz_module],
    py_modules=["fastfiz"],
)
