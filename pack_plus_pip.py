# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/blender_packages_plus

import os
from .bpy_plus.file_system import Path
import site
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
                cmd_opts = []
                if no_deps:
                    cmd_opts.extend(['--no-deps'])
                if only_binary:
                    cmd_opts.extend(['--only-binary', 'all'])
                if user:
                    cmd_opts.extend(['--user'])
                    rez =
                # install package
                rez = cls.subprocess_call(
                    cmd_opts=cmd_opts
                )

            # a = subprocess.call(
            #     [Path.python(), '-m', 'pip', 'install', '--upgrade', 'scipy', '-t', target]
            # )
            # print('xxxxx')
            # print(a)
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

    @classmethod
    def ensure_site_packages(cls):
        # ensure site_packages
        site_packages_dir = site.getusersitepackages()
        if not os.path.exists(site_packages_dir):
            site_packages_dir = bpy.utils.user_resource('SCRIPTS', "site_package", create=True)
            site_packages_dir = os.path.join(Path.scripts(source='USER'))
            site.addsitedir(site_packages_dir)
        if site_packages_dir not in sys.path:
            sys.path.append(site_packages_dir)

    @staticmethod
    def subprocess_call(cmd_opts: list):
        # call subprocess
        cmd = [Path.python(), '-m']
        cmd.extend(cmd_opts)
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
        return rez
