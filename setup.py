import os
import sys
import versioneer

from setuptools import setup, Extension

here = os.path.dirname(__file__)

ext_files = [
  'src/mmapbitarray.c',
  'src/bloomfilter.c',
  'src/md5.c',
  'src/primetester.c',
  'src/MurmurHash3.c',
  'src/pybloomfilter.pyx'
]

print("info: Building from Cython")

ext_modules = [
  Extension("pybloomfilter", ext_files, libraries=['crypto'])
]

if sys.version_info[0] < 3:
  raise SystemError('This Package is for Python Version 3 and above.')

setup(
  name='pybloomfiltermmap3',
  version=versioneer.get_version(),
  author="Michael Axiak, Rob Stacey, Prashant Sinha",
  author_email="prashant@ducic.ac.in",
  url="https://github.com/PrashntS/pybloomfiltermmap3",
  description="A Bloom filter (bloomfilter) for Python 3 built on mmap",
  license="MIT License",
  test_suite='tests.test_all',
  install_requires=[],
  ext_modules=ext_modules,
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Intended Audience :: Science/Research',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: C',
    'Programming Language :: Cython',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Topic :: Software Development :: Libraries :: Python Modules',
  ],
  setup_requires=[
        # Setuptools 18.0 properly handles Cython extensions.
        'setuptools>=18.0',
        'cython',
  ],
  cmdclass=versioneer.get_cmdclass()
)
