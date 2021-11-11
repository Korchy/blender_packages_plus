# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/blender_packages_plus

from bpy.types import Panel
from bpy.utils import register_class, unregister_class


class PACK_PLUS_PT_panel_pip(Panel):
    bl_idname = 'PACK_PLUS_PT_panel_pip'
    bl_label = 'pip'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Pack+'

    def draw(self, context):
        layout = self.layout
        # package
        props = context.window_manager.pack_plus_props
        layout.label(text='Package name:')
        layout.prop(
            data=props,
            property='package_name',
            text=''
        )
        # check
        layout.separator()
        layout.operator(
            operator='pack_plus.check',
            icon='CHECKBOX_HLT'
        )
        # install
        layout.separator()
        layout.operator(
            operator='pack_plus.install',
            icon='IMPORT'
        )
        layout.prop(
            data=props,
            property='no_deps'
        )
        layout.prop(
            data=props,
            property='only_binary'
        )


def register():
    register_class(PACK_PLUS_PT_panel_pip)


def unregister():
    unregister_class(PACK_PLUS_PT_panel_pip)
