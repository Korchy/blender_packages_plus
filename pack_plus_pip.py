# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/blender_packages_plus

from .bpy_plus.file_system import Path
import subprocess
import sys


class Pip:

    @classmethod
    def install(cls, package, no_deps=False, only_binary=False, user=False):
        # install new package by name with pip
        rez = False
        if package:
            # ensure pip before install
            rez = cls.ensure_pip()
            # install options
            if rez:
                cmd_opts = ['pip', 'install', '--upgrade', package]
                if no_deps:
                    cmd_opts.extend(['--no-deps'])
                if only_binary:
                    cmd_opts.extend(['--only-binary', 'all'])
                if user:
                    cmd_opts.extend(['--user'])
                    cls.ensure_user_site_packages()
                else:
                    cmd_opts.extend(['--target', Path.site_packages(source='SYSTEM')])
                # install package
                rez = cls.subprocess_call(
                    cmd_opts=cmd_opts
                )
        return rez

    @classmethod
    def uninstall(cls, package):
        # uninstall package by name with pip
        rez = False
        if package:
            # ensure pip before install
            rez = cls.ensure_pip()
            # uninstall package
            if rez:
                rez = cls.subprocess_call(
                    cmd_opts=['pip', 'uninstall', package, '--yes']
                )
        return rez

    @classmethod
    def ensure_pip(cls):
        # ensure pip before package installation
        rez = cls.subprocess_call(
            cmd_opts=['ensurepip']
        )
        if rez:
            rez = cls.subprocess_call(
                cmd_opts=['pip', 'install', '--upgrade', 'pip']
            )
        return rez

    @staticmethod
    def ensure_user_site_packages():
        # ensure user site_packages
        site_packages_dir = Path.site_packages(source='USER')
        if site_packages_dir not in sys.path:
            sys.path.append(site_packages_dir)

    @staticmethod
    def subprocess_call(cmd_opts: list):
        # call subprocess
        cmd = [Path.python(), '-m']
        cmd.extend(cmd_opts)
        # print(cmd)
        try:
            output = subprocess.check_output(
                cmd,
                stderr=subprocess.STDOUT,
                shell=True,
                universal_newlines=True
            )
            rez = True
            print(output)
        except subprocess.CalledProcessError as ex:
            print(ex.output)
            rez = False
        except Exception as ex:
            print(ex)
            rez = False
        return rez
