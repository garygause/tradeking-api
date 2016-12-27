# encoding: utf-8
# Copyright 2016 Gary Gause
#
# This file is provided AS IS with NO WARRANTY OF ANY KIND, INCLUDING THE
# WARRANTY OF DESIGN, MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.
#

from setuptools import setup, find_packages

def get_file(file_name):
    with open(file_name) as f:
        return f.read()

readme = get_file('README.rst')
history = get_file('HISTORY.rst')

exec(open('tradeking/version.py').read())

setup(name='tradeking-api',
      version=__version__,
      description='Unofficial Python client for the TradeKing api',
      long_description=readme + '\n\n' + history,
      url='https://github.com/garygause/tkapi',
      author='Gary Gause',
      author_email='garygause69@gmail.com',
      license='MIT',
      packages=find_packages(),
      include_package_data=True,
      install_requires=get_file('requirements.txt'),
      keywords='tradeking rest api',
      classifiers=[
          'Development Status :: 2 - Pre-Alpha',
          'Intended Audience :: Developers',
      ],
      test_suite='tests',
      tests_require=get_file('requirements_test.txt'),
      zip_safe=False)
