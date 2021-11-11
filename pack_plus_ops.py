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
        PackPlus.install(
            name=''
        )
        return {'FINISHED'}


def register():
    register_class(PACK_PLUS_OT_install)


def unregister():
    unregister_class(PACK_PLUS_OT_install)
