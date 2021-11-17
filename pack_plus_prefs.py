# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/blender_packages_plus

from bpy.types import AddonPreferences
from bpy.props import BoolProperty
from bpy.utils import register_class, unregister_class
from .pack_plus_ui import register_viewport, unregister_viewport, register_text_editor, unregister_text_editor


class PACK_PLUS_prefs(AddonPreferences):
    bl_idname = __package__

    panel_text_editor: BoolProperty(
        name='Panel in a Text Editor window',
        default=True,
        update=lambda self, context: self._panel_text_editor_update(
            self=self
        )
    )

    panel_viewport: BoolProperty(
        name='Panel in a 3D Viewport window',
        default=True,
        update=lambda self, context: self._panel_viewport_update(
            self=self
        )

    )

    def draw(self, context):
        layout = self.layout
        layout.prop(
            data=self,
            property='panel_text_editor',
            toggle=True
        )
        layout.prop(
            data=self,
            property='panel_viewport',
            toggle=True
        )

    @staticmethod
    def _panel_text_editor_update(self):
        if self.panel_text_editor:
            register_text_editor()
        else:
            unregister_text_editor()

    @staticmethod
    def _panel_viewport_update(self):
        if self.panel_viewport:
            register_viewport()
        else:
            unregister_viewport()


def register():
    register_class(PACK_PLUS_prefs)


def unregister():
    unregister_class(PACK_PLUS_prefs)
