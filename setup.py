#!/usr/bin/env python
import distribute_setup
distribute_setup.use_setuptools()

from setuptools import setup, find_packages

setup(name='feather',
      version='0.9.0',
      setup_requires = ['setuptools_git >= 0.3'],
      packages=find_packages(),
      include_package_data=False,
      description="A small framework for developing small plugin-based applications",
#      long_description=open('README').read(),
      classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Plugins',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules'
        ], 
      keywords='framework plugins plugin frameworks multiprocessing',
      author='Jeremiah Dodds',
      author_email='jeremiah.dodds@gmail.com',
      url='https://github.com/jdodds/feather',
      download_url='https://github.com/jdodds/feather/downloads',
      license='BSD',
      zip_safe=True
      )
