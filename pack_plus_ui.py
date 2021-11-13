# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/blender_packages_plus

from bpy.types import Panel
from bpy.utils import register_class, unregister_class


class PACK_PLUS_PT_panel_packages(Panel):
    bl_idname = 'PACK_PLUS_PT_panel_packages'
    bl_label = 'Packages +'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'P+'
    bl_order = 0

    def draw(self, context):
        layout = self.layout
        props = context.window_manager.pack_plus_props
        # package
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


class PACK_PLUS_PT_panel_pip(Panel):
    bl_idname = 'PACK_PLUS_PT_panel_pip'
    bl_label = 'PIP'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'P+'
    bl_order = 1

    def draw(self, context):
        layout = self.layout
        props = context.window_manager.pack_plus_props
        # install
        layout.separator()
        layout.prop(
            data=props,
            property='no_deps'
        )
        layout.prop(
            data=props,
            property='only_binary'
        )
        layout.prop(
            data=props,
            property='user'
        )
        layout.operator(
            operator='pack_plus.install_pip',
            icon='IMPORT'
        )


def register():
    register_class(PACK_PLUS_PT_panel_packages)
    register_class(PACK_PLUS_PT_panel_pip)


def unregister():
    unregister_class(PACK_PLUS_PT_panel_pip)
    unregister_class(PACK_PLUS_PT_panel_packages)
