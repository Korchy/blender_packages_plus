# Packages plus

Blender 3D add-on for installing and managing additional Python packages.

Add-on functionality
-
With the add-on, you can install packages from the PyPi repository.

To install the required package directly to Blender - specify the package name in the "Package Name" field, select "/BLENDER" in the installation destination field and press the "Install" button. The specified package will be installed into the Blender installation directory.

<img src="https://b3d.interplanety.org/wp-content/upload_content/2021/11/preview_03_1200x600-1-560x280.jpg"><p>

With this type of installation, the package will be available everywhere in Blender - when you write a script in a Text Editor, and in the Python Console using the common "import" command.

    import numba

You can also install the required Python package into the user home directory. This is usually the preferred way. In this case, the package does not affect the current Blender installation, can be called from any version of Blender installed on your computer. However, such a package cannot be included with just the single "import" statement. To get the code for importing such a package to your script - press the "Code" button in the add-on panel.

You need to execute the code for including the package in your script only once and then import the package anywhere with the same standard "import" command.

The add-on can detect whether the package is already installed in your system and show the location of its installation. Specify the name of the package and press the "Check" button in the add-on panel.

<img src="https://b3d.interplanety.org/wp-content/upload_content/2021/11/preview_01_1200x600-1-560x280.jpg"><p>

To uninstall a package, specify its name and press the "Uninstall" button.

Attention!
-
The add-on is for advanced users! Installing and managing Python packages can damage your Blender installation and even your operating system!

Add-on web-page
-
For more information see:

https://b3d.interplanety.org/en/blender-add-on-packages-plus/

Current add-on version
-
1.0.0.

Blender versions
-
2.93, 3.0

Location and call
-
The “3D Viewport” window – N panel – “P+” tab.

The “Text Editor” window – N panel – “P+” tab.

Installation
-
- Download the *.zip archive with the add-on distributive.
- The “Preferences” window — Add-ons — Install… — specify the downloaded archive.

Version history
-
1.0.0.
- This release.
