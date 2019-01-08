#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    Cpp-Project build script
"""

import os
import os.path
import shutil
import sys
import argparse

version_ = "0.0.1"
project_name_ = "Cpp-Project"
app_name_ = "app"

parser = argparse.ArgumentParser(description="Cpp-Project build script")
parser.add_argument("-v", "--version", action="version", version=version_)
parser.add_argument(
    "-t",
    "--type",
    dest="build_type",
    choices=("debug", "release"),
    default="release",
    help="build type: debug or release",
)
args = parser.parse_args()


def start_build():
    source_dir = os.getcwd()
    build_dir = "{0}/build/{1}/{2}".format(source_dir, project_name_, args.build_type)
    if not os.path.exists(build_dir):
        os.makedirs(build_dir)
    os.chdir(build_dir)
    os.system(
        "cmake -DCMAKE_BUILD_TYPE={0} {1} && cmake --build . -- '-j'".format(
            args.build_type, source_dir
        )
    )
    os.chdir(source_dir)


if __name__ == "__main__":
    start_build()
