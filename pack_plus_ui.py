# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/blender_packages_plus

from bpy.types import Panel
from bpy.utils import register_class, unregister_class


class PACK_PLUS_PT_panel(Panel):
    bl_idname = 'PACK_PLUS_PT_panel'
    bl_label = 'Pack+'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Pack+'

    def draw(self, context):
        self.layout.operator(
            operator='pack_plus.install',
            icon='IMPORT'
        )


def register():
    register_class(PACK_PLUS_PT_panel)


def unregister():
    unregister_class(PACK_PLUS_PT_panel)
