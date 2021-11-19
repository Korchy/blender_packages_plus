# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/blender_packages_plus

from bpy.props import BoolProperty, PointerProperty, StringProperty, EnumProperty
from bpy.types import PropertyGroup, WindowManager
from bpy.utils import register_class, unregister_class


class PACK_PLUS_Props(PropertyGroup):

    package_name: StringProperty(
        name='Package name',
        default=''
    )

    no_deps: BoolProperty(
        name='With no dependencies',
        default=False
    )

    only_binary: BoolProperty(
        name='Do not use source packages',
        default=False
    )

    source: EnumProperty(
        name='Use the /USER or /BLENDER directory',
        items=[
            ('USER', '/USER', 'Use /USER directory', '', 0),
            ('BLENDER', '/BLENDER', 'Use /BLENDER directory', '', 1),
            ('EXTERNAL', 'EXTERNAL', 'Type the required external path', '', 2)
        ],
        default='USER'
    )

    target: StringProperty(
        subtype='DIR_PATH',
        name='External path to install packages',
        default=''
    )


def register():
    register_class(PACK_PLUS_Props)
    WindowManager.pack_plus_props = PointerProperty(type=PACK_PLUS_Props)


def unregister():
    del WindowManager.pack_plus_props
    unregister_class(PACK_PLUS_Props)
