# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/blender_packages_plus

import bpy
from importlib.metadata import version
import sys
from importlib.util import find_spec


class PackPlus:

    @staticmethod
    def install_pip(name, no_deps, only_binary):
        # install new package by name with pip
        if name:
            print(name)

    @staticmethod
    def is_installed(name):
        # check if package "name" is installed
        installed = None
        version_ = None
        if name and find_spec(name=name):
            version_ = version(name)
            installed = True
        return installed, version_

    @staticmethod
    def python_path():
        # returns path to blender python.exe
        try:
            python_path = bpy.app.binary_path_python
        except AttributeError:
            python_path = sys.executable
        return python_path
