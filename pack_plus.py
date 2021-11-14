# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/blender_packages_plus

import ctypes
from importlib.util import find_spec
from importlib.metadata import version, PackageNotFoundError
import os
from .bpy_plus.file_system import Path
from .pack_plus_pip import Pip
import platform


class PackPlus:

    @classmethod
    def install_pip(cls, name: str, no_deps: bool = False, only_binary: bool = False, user: bool = False) -> bool:
        # install new package by name with pip
        return Pip.install(
            package=name,
            no_deps=no_deps,
            only_binary=only_binary,
            user=user
        )

    @classmethod
    def uninstall_pip(cls, name: str) -> bool:
        # uninstall package by name with pip
        if cls.is_installed(name=name)[0]:
            return Pip.uninstall(
                package=name
            )

    @staticmethod
    def is_installed(name: str) -> tuple:
        # check if package "name" is installed
        installed = None
        version_ = None
        if name and find_spec(name=name):
            try:
                version_ = version(name)
                installed = True
            except PackageNotFoundError as ex:
                pass
        return installed, version_

    @staticmethod
    def source(package: str):
        # get source where package is installed
        if package:
            installed_dir = os.path.dirname(find_spec(name=package).origin)
            if Path.blender_v().lower() in installed_dir.lower():
                return 'SYSTEM'
            else:
                return 'USER'
        return None

    @staticmethod
    def is_admin() -> bool:
        # check if Blender run with administrative privileges
        system = platform.system().lower()
        if system.startswith('windows'):
            # Windows
            try:
                is_admin = bool(ctypes.windll.shell32.IsUserAnAdmin())
            except Exception as ex:
                is_admin = False
        elif system.startswith('posix') or system.startswith('darwin'):
            # Linux of MacOs
            is_admin = os.getuid() == 0
        else:
            is_admin = None
            print('Can not get information about the OS privileges')
        return is_admin
