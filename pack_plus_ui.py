# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/blender_packages_plus

import bpy
from bpy.types import Panel
from bpy.utils import register_class, unregister_class


class PACK_PLUS_PT_panel_packages:
    bl_label = 'Packages +'
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
        # check/code
        layout.separator()
        row = layout.row()
        row.operator(
            operator='pack_plus.check',
            icon='CHECKBOX_HLT'
        )
        row.operator(
            operator='pack_plus.import_code',
            icon='SCRIPT'
        )


class PACK_PLUS_PT_panel_packages_viewport(Panel, PACK_PLUS_PT_panel_packages):
    bl_idname = 'PACK_PLUS_PT_panel_packages_viewport'
    bl_space_type = 'VIEW_3D'


class PACK_PLUS_PT_panel_packages_text(Panel, PACK_PLUS_PT_panel_packages):
    bl_idname = 'PACK_PLUS_PT_panel_packages_text'
    bl_space_type = 'TEXT_EDITOR'


class PACK_PLUS_PT_panel_pip:
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
            property='source',
            expand=True
        )
        row = layout.row()
        row.operator(
            operator='pack_plus.install_pip',
            icon='IMPORT'
        )
        row.operator(
            operator='pack_plus.uninstall_pip',
            icon='CANCEL'
        )


class PACK_PLUS_PT_panel_pip_viewport(Panel, PACK_PLUS_PT_panel_pip):
    bl_idname = 'PACK_PLUS_PT_panel_pip_viewport'
    bl_space_type = 'VIEW_3D'


class PACK_PLUS_PT_panel_pip_text(Panel, PACK_PLUS_PT_panel_pip):
    bl_idname = 'PACK_PLUS_PT_panel_pip_text'
    bl_space_type = 'TEXT_EDITOR'


def register_viewport():
    if bpy.context.preferences.addons[__package__].preferences.panel_viewport:
        register_class(PACK_PLUS_PT_panel_packages_viewport)
        register_class(PACK_PLUS_PT_panel_pip_viewport)


def register_text_editor():
    if bpy.context.preferences.addons[__package__].preferences.panel_text_editor:
        register_class(PACK_PLUS_PT_panel_packages_text)
        register_class(PACK_PLUS_PT_panel_pip_text)


def unregister_viewport():
    if hasattr(bpy.types, 'PACK_PLUS_PT_panel_pip_viewport'):
        unregister_class(PACK_PLUS_PT_panel_pip_viewport)
    if hasattr(bpy.types, 'PACK_PLUS_PT_panel_packages_viewport'):
        unregister_class(PACK_PLUS_PT_panel_packages_viewport)


def unregister_text_editor():
    if hasattr(bpy.types, 'PACK_PLUS_PT_panel_pip_text'):
        unregister_class(PACK_PLUS_PT_panel_pip_text)
    if hasattr(bpy.types, 'PACK_PLUS_PT_panel_packages_text'):
        unregister_class(PACK_PLUS_PT_panel_packages_text)


def register():
    register_viewport()
    register_text_editor()


def unregister():
    unregister_text_editor()
    unregister_viewport()
