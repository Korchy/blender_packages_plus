# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/blender_packages_plus

from importlib.metadata import version
from .pack_plus_pip import Pip
from importlib.util import find_spec


class PackPlus:

    @classmethod
    def install_pip(cls, name, no_deps=False, only_binary=False, user=False):
        # install new package by name with pip
        rez = False
        if name:
            rez = Pip.install(
                package=name,
                no_deps=no_deps,
                only_binary=only_binary,
                user=user
            )
        return rez

    @staticmethod
    def is_installed(name):
        # check if package "name" is installed
        installed = None
        version_ = None
        if name and find_spec(name=name):
            version_ = version(name)
            installed = True
        return installed, version_
