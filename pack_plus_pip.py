# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/blender_packages_plus

from .bpy_plus.file_system import Path
import subprocess


class Pip:

    @classmethod
    def install(cls, package, no_deps=False, only_binary=False, user=False):
        # install new package by name with pip
        rez = False
        if package:
            # ensure pip before install
            rez = cls.ensure_pip()
            # install package
            opts = []
            if no_deps:
                opts.extend(['--no-deps'])
            if only_binary:
                opts.extend(['--only-binary', 'all'])
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
            cmd=['ensurepip']
        )
        if rez:
            rez = cls.subprocess_call(
                cmd=['pip', 'install', '--upgrade', 'pip']
            )
        return rez

    @staticmethod
    def subprocess_call(cmd: list):
        # call subprocess
        cmd_ = [Path.python(), '-m']
        cmd_.extend(cmd)
        try:
            output = subprocess.check_output(
                cmd_,
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
