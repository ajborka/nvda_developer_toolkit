# Developer toolkit
Developer toolkit (DTK) is an NVDA add-on that helps blind and visually impaired developers independently create visually appealing user interfaces and web content. It provides gestures that enable you to navigate through objects and obtain information about them, such as their size, position, and characteristics. To begin using DTK, place focus on a control, then press **ALT+WINDOWS+K**. To disable it, press **ALT+WINDOWS+K** again. When on the web, press **NVDA+SPACE** to put NVDA in Focus Mode and press NVDA+SHIFT+SPACE to disable Single Letter Navigation.

## Gestures

The following gestures are available when DTK is enabled.

* **ALT+WINDOWS+K** - Enable or disable DTK features.
* **LEFT ARROW** - Move to previous sibling.
* **RIGHT ARROW** - Move to next sibling.
* **UP ARROW** - Move to parent.
* **DOWN ARROW** - Move to first child.
* **CTRL+HOME** - Move to top-most parent.
* **A** - In web content, speak HTML attributes. Press twice quickly to copy to the clipboard.
* **B** - Speak the position of the object's bottom edge. Press twice quickly to copy to the clipboard.
* **SHIFT+B** - Speak the distance between the object's bottom edge and the relative parent's bottom edge. Press twice quickly to copy to the clipboard.
* **C** - Speak the number of children contained inside the object. Press twice quickly to copy to the clipboard.
* **control+c** - Switch between RGB, Hex, and Name color values.
* **CTRL+D** - Enable or disable detailed messages.
* **F** - In web content, speaks the object's font and formatting information. Press twice quickly to copy to the clipboard.
* **H** - Speak the object's height. Press twice quickly to copy to the clipboard.
* **L** - Speak the position of the object's left edge. Press twice quickly to copy to the clipboard.
* **n** - Speak the object's name. Press twice quickly to copy to the clipboard.
* **CTRL+P** - Set the relative parent for obtaining size/location of objects.
* **P** - Speak the relative parent's name. Press twice quickly to copy to the clipboard.
* **R** - Speak the position of the object's right edge. Press twice quickly to copy to the clipboard.
* **SHIFT+R** - Speak the distance between the object's right edge and the relative parent's right edge. Press twice quickly to copy to the clipboard.
* **S** - Speak the number of siblings relative to the object. Press twice quickly to copy to the clipboard.
* **T** - Speak the position of the object's top edge. Press twice quickly to copy to the clipboard.
* **V** - Speak Developer toolkit version. Press twice quickly to copy to the clipboard.
* **W** - Speak the object's width. Press twice quickly to copy to the clipboard.

## Notes

* When using the relative parent feature, DTK will set the relative parent to the desktop under the following conditions.
	* The focused object and the relative parent are the same.
	* The relative parent is not a direct ancestor of the focused object.
* DTK does not support the Edge web browser.
* Until NVDA provides font information from more sources, font information is only available in web content.

## Known issues

* DTK does not automatically notify you of the enabled or disabled state of its features when switching between configuration profiles.
* The customizable list of font attributes found in Developer toolkit settings may be cumbersome to use. This is a limitation found in NVDA's user interface library.

## Version history
### 2020.2

* Starting DTK retains the cursor’s current position in web content. If the object under the caret can’t gain focus, DTK will place focus on the first available ancestor.
* Removed legacy support for unicode strings.
* Removed the enable/disable Developer toolkit features setting from Developer toolkit settings dialog found in NVDA menu>preferences>settings. Users can still enable/disable features by pressing alt+windows+k.
* The formatting attributes obtained by pressing 'f' when Developer toolkit is enabled is now configurable in preferences>settings>Developer toolkit.
	* Add new formatting attributes by pressing the 'new attribute' button. Type in a name of a valid formatting attribute, press tab to put it in the list, then press escape to leave edit mode.
	* Remove an attribute by selecting it in the list, then pressing the 'delete attribute' button.
	* Rename an attribute by pressing the 'Rename attribute' button, typing a new name, pressing tab to put it in the list, then pressing escape to leave edit mode.
	* Move an attribute up in the list by selecting it and pressing the 'Move up' button. Repeat this until it reaches the desired location in the list.
	* Move an attribute down in the list by selecting it and pressing the 'Move down' button. Repeat this until it reaches the desired location in the list.
* Users now have the ability to change the way color values are displayed while obtaining formatting information. The setting is found in preferences>settings>Developer toolkit, then choosing a color display format. The color display format can also be changed by pressing control+c while Developer toolkit features are enabled.
	* **RGB** - Red Green Blue value. Defines a color through a red, green, blue color combination. Good for graphic art, especially non-web safe colors.
	* **Hex** - string starting with a '#' and followed by 6 characters consiting of 1-0 and A-F. Usually good for web content.
	* **Name** - The human readable value for the color. Good for general purpose usage and verifying other color value formats.

### 2020.1.1

* Improved unicode support.

### 2020.1.0

* Developers now have the ability to focus on smaller areas of their user interfaces by pressing CTRL+p to set a relative parent. Use a relative parent as a reference point when obtaining size and location information. To use this feature, enable DTK features, navigate to the object to use as a relative parent, then press CTRL+p. Then, return to your work as usual.
* Press the letter p while working in DTK to obtain the relative parent's name. Press twice quickly to copy to the clipboard.
* Use SHIFT+b to obtain the distance between the focused object's bottom edge and the relative paren'ts bottom edge. DTK features must be enable to use this feature.
* Use SHIFT+r to obtain the distance between the focused object's right edge and the relative paren'ts right edge. DTK features must be enable to use this feature.
* DTK now gracefully handles configuration profile switches.
* Removed '-preview' from the version number to avoid version number problems with add-on updater.

### 2020.0 preview

* Changed version number to 2020.0 preview to reflect the impending switch to Python 3.
* Added Python 3 compatibility.
* Added a new gesture, "n" that speaks the object's name. If one is not assigned, speaks the word 'None' as the object's name.
* DTK no longer adds duplicate settings panels in the NVDA settings window when reloading add-ons.

### 2019.1.2

* DTK will now report size and position values if they are 0.
* Navigation now honors the detailed messages setting.
* Made reporting of size/position information more concise.
* Stability improvements.

### 2019.1.1

* DTK will no longer attempt to load itself multiple times when announcing the version number.
* DTK features will be disabled on install. Previously, DTK features were enabled on install. This is different than enabling or disabling the add-on in the NVDA toolls>manage add-ons window.
* Messages presented to the user can now contain non-ascii characters.
* Pressing gestures such as a, b, c, f, h, l, r, s, t, v, and w no longer interupt NVDA speech when copying to the clipboard.

### 2019.1

* Fixed a compatibility problem where DTK declared a minimum NVDA version that hasn't been released yet.

### 2019.0 (initial stable release)

* Initial build with basic navigation.
