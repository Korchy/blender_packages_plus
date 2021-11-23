# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/blender_packages_plus

from . import pack_plus_message_box
from . import pack_plus_ops
from . import pack_plus_prefs
from . import pack_plus_props
from . import pack_plus_ui
from .addon import Addon

bl_info = {
    'name': 'Pack +',
    'category': 'All',
    'author': 'Nikita Akimov',
    'version': (1, 0, 0),
    'blender': (2, 93, 0),
    'location': '3D Viewport - N panel, Text Editor - N panel',
    'wiki_url': 'https://b3d.interplanety.org/en/blender-add-on-packages-plus/',
    'tracker_url': 'https://b3d.interplanety.org/en/blender-add-on-packages-plus/',
    'description': 'Add-on to simplify installing external Python packages to Blender'
}


def register():
    if not Addon.dev_mode():
        pack_plus_prefs.register()
        pack_plus_props.register()
        pack_plus_ops.register()
        pack_plus_ui.register()
        pack_plus_message_box.register()
    else:
        print('It seems you are trying to use the dev version of the '
              + bl_info['name']
              + ' add-on. It may work not properly. Please download and use the release version')


def unregister():
    if not Addon.dev_mode():
        pack_plus_message_box.unregister()
        pack_plus_ui.unregister()
        pack_plus_ops.unregister()
        pack_plus_props.unregister()
        pack_plus_prefs.unregister()


if __name__ == '__main__':
    register()
