# Developer toolkit
Developer toolkit (DTK) is an NVDA add-on that assists blind and visually impaired developers with independently creating visually appealing user interfaces or web content. This is done by enabling DTK, navigating around the user interface or web content, then performing gestures to obtain information about the appearance, location, and size of the focused control. To enable or disable DTK, press alt+windows+k on your keyboard. To continue using the computer normally, disable DTK before performing normal tasks.
## Gestures
The following gestures are available when DTK is enabled.

* Alt+windows+k - Enable or disable DTK features.
* Left arrow - Move to previous sibling.
* Right arrow - Move to next sibling.
* Up arrow - Move to parent.
* Down arrow - Move to first child.
* Control+home - Move to top-most parent.
* A - In web content, speak HTML attributes. Press twice quickly to copy to the clipboard.
* B - Speak the position of the object’s bottom edge. Press twice quickly to copy to the clipboard.
* C - Speak the number of children contained inside the object. Press twice quickly to copy to the clipboard.
* Control+d - Enable or disable detailed messages.
* F - In web content, speaks the object’s font and formatting information. Press twice quickly to copy to the clipboard.
* H - Speak the object’s height. Press twice quickly to copy to the clipboard.
* L - Speak the position of the object’s left edge. Press twice quickly to copy to the clipboard.
* n - Speak the object's name. Press twice quickly to copy to the clipboard.
* R - Speak the position of the object’s right edge. Press twice quickly to copy to the clipboard.
* S - Speak the number of siblings relative to the object. Press twice quickly to copy to the clipboard.
* T - Speak the position of the object’s top edge. Press twice quickly to copy to the clipboard.
* V - Speak Developer toolkit version. Press twice quickly to copy to the clipboard.
* W - Speak the object’s width. Press twice quickly to copy to the clipboard.

## Notes

* Edge has not been completely tested. Therefore, anything reported by the add-on should be considered with care.
* To avoid names of web elements appearing as "None", always give elements a title attribute.
* Font information is only available in web content. This should be fixed in a future version.

## Known issues

* Users are not automatically notified of the enabled/disabled state of the add-on's features when switching between configuration profiles.
* There is no way to restrict DTK to a specific content type or application window.
* The font information when pressing F is messy, and will get fixed in a future version.

## Version history
### 2020.1.0

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
