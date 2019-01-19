"""
setup for five_gx
"""
from setuptools import setup

def readme():
      """ get the readme file
      """
      with open('README.rst') as f_readme:
            return f_readme.read()

setup(name='power_app',
      version='0.1',
      description='measurements for SMPS',
      long_description=readme(),
      author='Bobby Smith',
      author_email='bobby@s-tronics.com',
      packages=['power_app'],
      install_requires=[
          'numpy',
          'python-usbtmc',
          'pyusb',
          'tqdm',
          ],
      include_package_data=True,
      test_suite='nose.collector',
      tests_require=['nose'],
      zip_safe=False)


