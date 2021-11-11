# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/blender_packages_plus

class PackPlus:

    @staticmethod
    def install(name, no_deps, only_binary):
        # install new package by name
        if name:
            print(name)

    @staticmethod
    def check(name):
        # check installed package
        if name:
            module = None
            try:
                module = __import__(name)
            except Exception as exception:
                print(repr(exception))
            if module:
                print(module.__version__)
