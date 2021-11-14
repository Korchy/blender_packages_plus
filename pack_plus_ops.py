# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/blender_packages_plus

import bpy
from bpy.types import Operator
from bpy.utils import register_class, unregister_class
from .pack_plus import PackPlus


class PACK_PLUS_OT_install_pip(Operator):
    bl_idname = 'pack_plus.install_pip'
    bl_label = 'Install'
    bl_description = 'Install Python package with pip'
    bl_options = {'REGISTER'}

    def execute(self, context):
        props = context.window_manager.pack_plus_props
        # check privileges
        if PackPlus.is_admin() or context.window_manager.pack_plus_props.user:
            # install
            rez = PackPlus.install_pip(
                name=props.package_name,
                no_deps=props.no_deps,
                only_binary=props.only_binary,
                user=props.user
            )
            bpy.ops.pack_plus.messagebox(
                'INVOKE_DEFAULT',
                message=('Successfully installed' if rez else 'ERROR! See details in the System Console.')
            )
        else:
            bpy.ops.pack_plus.messagebox(
                'INVOKE_DEFAULT',
                message='You have not Administrative privileges' + '\n'
                         + 'It may cause errors during installation' + '\n'
                         + 'Run Blender as Administrator!'
            )
        return {'FINISHED'}

    @classmethod
    def poll(cls, context):
        return bool(context.window_manager.pack_plus_props.package_name)


class PACK_PLUS_OT_uninstall_pip(Operator):
    bl_idname = 'pack_plus.uninstall_pip'
    bl_label = 'Uninstall'
    bl_description = 'Uninstall Python package with pip'
    bl_options = {'REGISTER'}

    def execute(self, context):
        props = context.window_manager.pack_plus_props
        # check privileges
        if PackPlus.is_admin() or context.window_manager.pack_plus_props.user:
            # uninstall
            rez = PackPlus.uninstall_pip(
                name=props.package_name
            )
            bpy.ops.pack_plus.messagebox(
                'INVOKE_DEFAULT',
                message=('Successfully uninstalled' if rez else 'ERROR! See details in the System Console.')
            )
        else:
            bpy.ops.pack_plus.messagebox(
                'INVOKE_DEFAULT',
                message='You have not Administrative privileges' + '\n'
                         + 'It may cause errors during installation' + '\n'
                         + 'Run Blender as Administrator!'
            )
        return {'FINISHED'}

    @classmethod
    def poll(cls, context):
        return bool(context.window_manager.pack_plus_props.package_name)

    def invoke(self, context, event):
        package_name = context.window_manager.pack_plus_props.package_name
        if PackPlus.is_installed(name=package_name)[0]:
            return context.window_manager.invoke_props_dialog(self, width=200)
        else:
            bpy.ops.pack_plus.messagebox(
                'INVOKE_DEFAULT',
                message=('Package: ' + package_name + ' is not installed!')
            )
            return {'CANCELLED'}

    def draw(self, context):
        layout = self.layout
        layout.label(text='Are you sure?')


class PACK_PLUS_OT_check(Operator):
    bl_idname = 'pack_plus.check'
    bl_label = 'Check'
    bl_description = 'Check Python package'
    bl_options = {'REGISTER'}

    def execute(self, context):
        props = context.window_manager.pack_plus_props
        rez = PackPlus.is_installed(
            name=props.package_name
        )
        bpy.ops.pack_plus.messagebox(
            'INVOKE_DEFAULT',
            message='Package: ' + props.package_name +
                    '\n' + 'Installed: ' + ('Yes' if rez[0] else 'No') +
                    ('\n' + 'Version: ' + rez[1] if rez[1] else '') +
                    ('\n' + 'Installed in: ' + PackPlus.source(package=props.package_name) if rez[0] else '')
        )
        return {'FINISHED'}

    @classmethod
    def poll(cls, context):
        return bool(context.window_manager.pack_plus_props.package_name)


def register():
    register_class(PACK_PLUS_OT_install_pip)
    register_class(PACK_PLUS_OT_uninstall_pip)
    register_class(PACK_PLUS_OT_check)


def unregister():
    unregister_class(PACK_PLUS_OT_check)
    unregister_class(PACK_PLUS_OT_uninstall_pip)
    unregister_class(PACK_PLUS_OT_install_pip)
