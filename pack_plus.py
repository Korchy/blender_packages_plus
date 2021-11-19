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
    def install_pip(cls, name: str, no_deps: bool = False, only_binary: bool = False, target: str = 'USER') -> bool:
        # install new package by name with pip
        return Pip.install(
            package=name,
            no_deps=no_deps,
            only_binary=only_binary,
            target=target
        )

    @classmethod
    def uninstall_pip(cls, name: str) -> bool:
        # uninstall package by name with pip
        if cls.is_installed(package=name)[0]:
            return Pip.uninstall(
                package=name
            )
        else:
            return False

    @staticmethod
    def is_installed(package: str) -> tuple:
        # check if package "name" is installed
        installed = None
        version_ = None
        source = None
        installed_dir = None
        if package:
            # search in Blender installation dir
            find_spec_ = find_spec(name=package)
            if not find_spec_:
                # not found - search in user dir
                Pip.ensure_user_site_packages()
                find_spec_ = find_spec(name=package)
            if find_spec_:
                installed = True
                installed_dir = os.path.dirname(find_spec_.origin)
                if Path.blender_v().lower() in installed_dir.lower():
                    source = 'BLENDER'
                else:
                    source = 'USER'
                try:
                    version_ = version(package)
                except PackageNotFoundError:
                    pass
        return installed, version_, source, installed_dir

    @classmethod
    def source(cls, package: str):
        # get source where package is installed
        if package:
            return cls.is_installed(package=package)[2]
        return None

    @staticmethod
    def is_admin() -> bool:
        # check if Blender run with administrative privileges
        system = platform.system().lower()
        if system.startswith('windows'):
            # Windows
            try:
                is_admin = bool(ctypes.windll.shell32.IsUserAnAdmin())
            except Exception:
                is_admin = False
        elif system.startswith('linux') or system.startswith('posix') or system.startswith('darwin'):
            # Linux of MacOs
            is_admin = os.getuid() == 0
        else:
            is_admin = None
            print('Can not get information about the OS privileges')
        return is_admin

    @classmethod
    def import_code(cls, package: str) -> str:
        # generate code for import instructions based on where package is installed
        code = ''
        source = cls.source(package=package)
        if source == 'BLENDER':
            code = 'import ' + package
        elif source == 'USER':
            code_ = [
                'def ensure_user_site_packages(package):',
                '    # this needs to be called only once, and then you can import the package as usual',
                '    import bpy',
                '    import os',
                '    import site',
                '    import sys',
                '    user_site_packages_dir = site.getusersitepackages()',
                '    if not os.path.exists(user_site_packages_dir):',
                '        user_site_packages_dir = os.path.join(bpy.utils.user_resource(\'SCRIPTS\'), \'site-packages\')',
                '    if user_site_packages_dir not in sys.path:',
                '        sys.path.append(user_site_packages_dir)',
                '',
                '# call this function once',
                'ensure_user_site_packages(\'' + package + '\')',
                '',
                '# and import the required package as usual anywhere in your code',
                'import ' + package,
                '',
                '# here you can place your code',
                ''
            ]
            code = '\n'.join(code_)
        return code
