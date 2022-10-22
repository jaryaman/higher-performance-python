from setuptools import find_packages
from setuptools import setup

requirements = [
    'jupyter',
    'pandas',
    'numpy',
    'numexpr',  # recommended dependency for pandas
    'bottleneck',  # recommended dependency for pandas
    'numba',
    'dask[complete]',
    'graphviz',
    'tqdm',
    'line_profiler',
    'memory_profiler',
    'pyarrow',
    'matplotlib',
    'viztracer',
]

if '__main__' == __name__:
    setup(
        author='Juvid Aryaman',
        author_email='j.aryaman25@gmail.com',
        packages=find_packages(),
        long_description=open('README.md').read(),
        install_requires = requirements,
    )