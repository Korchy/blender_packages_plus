# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/blender_packages_plus

from bpy.types import Operator
from bpy.utils import register_class, unregister_class
from .pack_plus import PackPlus


class PACK_PLUS_OT_install(Operator):
    bl_idname = 'pack_plus.install'
    bl_label = 'Install'
    bl_description = 'Install Python package'
    bl_options = {'REGISTER'}

    def execute(self, context):
        props = context.window_manager.pack_plus_props
        PackPlus.install(
            name=props.package_name,
            no_deps=props.no_deps,
            only_binary=props.only_binary
        )
        return {'FINISHED'}

    @classmethod
    def poll(cls, context):
        return bool(context.window_manager.pack_plus_props.package_name)


class PACK_PLUS_OT_check(Operator):
    bl_idname = 'pack_plus.check'
    bl_label = 'Check'
    bl_description = 'Check Python package'
    bl_options = {'REGISTER'}

    def execute(self, context):
        props = context.window_manager.pack_plus_props
        PackPlus.check(
            name=props.package_name
        )
        return {'FINISHED'}

    @classmethod
    def poll(cls, context):
        return bool(context.window_manager.pack_plus_props.package_name)


def register():
    register_class(PACK_PLUS_OT_install)
    register_class(PACK_PLUS_OT_check)


def unregister():
    unregister_class(PACK_PLUS_OT_check)
    unregister_class(PACK_PLUS_OT_install)
