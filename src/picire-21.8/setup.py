# Copyright (c) 2016-2019 Renata Hodovan, Akos Kiss.
#
# Licensed under the BSD 3-Clause License
# <LICENSE.rst or https://opensource.org/licenses/BSD-3-Clause>.
# This file may not be copied, modified, or distributed except
# according to those terms.

from os.path import dirname, join
from setuptools import setup, find_packages
import subprocess


with open(join(dirname(__file__), 'picire/VERSION'), 'rb') as f:
    version = f.read().decode('ascii').strip()
    try:
        git_version = subprocess.check_output(["git", "rev-parse", "--short", "HEAD"]).decode('ascii').strip()
        if git_version:
            version = f"{version}+git{git_version}"
    except subprocess.CalledProcessError:
        pass


setup(
    name='picire',
    version=version,
    packages=find_packages(),
    url='https://github.com/renatahodovan/picire',
    license='BSD',
    author='Renata Hodovan, Akos Kiss',
    author_email='hodovan@inf.u-szeged.hu, akiss@inf.u-szeged.hu',
    description='Picire Delta Debugging Framework',
    long_description=open('README.rst').read(),
    zip_safe=False,
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'picire = picire.cli:execute'
        ]
    },
)

