#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    Cpp-Project build script
"""
from __future__ import absolute_import, division, print_function, \
    with_statement

import os
import os.path
import shutil
import sys
import argparse

version_ = "0.0.1"
project_name_ = "Cpp-Project"
app_name_ = "app"

parser = argparse.ArgumentParser(description='Cpp-Project build script')
parser.add_argument('-v', '--version', action='version', version=version_)
parser.add_argument('-t', '--type', dest='build_type', choices=('debug', 'release'), default='release', help='build type: debug or release')
parser.add_argument('-p', '--package', dest='package', action='store_true', default=False, help='build release and package to ./build/package/')
args = parser.parse_args()

def start_build():
    source_dir = os.getcwd()
    build_dir = '{0}/build/{1}/{2}'.format(source_dir, project_name_, args.build_type)
    if not os.path.exists(build_dir):
        os.makedirs(build_dir)
    os.chdir(build_dir)
    os.system('cmake -DCMAKE_BUILD_TYPE={0} {1} && make -j'.format(args.build_type, source_dir))
    os.chdir(source_dir)

def package():
    source_dir = os.getcwd()
    build_dir = '{0}/build/{1}/{2}'.format(source_dir, project_name_, args.build_type)
    if not os.path.exists(source_dir):
        print("build dir {0} is not exists".format(source_dir))
        sys.exit(1)
    package_dir = '{0}/build/{1}/package'.format(source_dir, project_name_)
    try:
        if not os.path.exists(package_dir):
            os.makedirs(package_dir)
        shutil.copy(build_dir + '/bin/{0}'.format(app_name_) ,package_dir)
        print("Package app to {0}".format(package_dir))
    except Exception as e:
        print(e, sys.stderr)

if __name__ == '__main__':
    start_build()
    if args.package:
        package()