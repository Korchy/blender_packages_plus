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
            ('USER', '/USER', 'use /USER directory', '', 0),
            ('BLENDER', '/BLENDER', 'use /BLENDER directory', '', 1)
        ],
        default='USER'
    )


def register():
    register_class(PACK_PLUS_Props)
    WindowManager.pack_plus_props = PointerProperty(type=PACK_PLUS_Props)


def unregister():
    del WindowManager.pack_plus_props
    unregister_class(PACK_PLUS_Props)
