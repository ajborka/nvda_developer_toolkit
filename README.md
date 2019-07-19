# Developer toolkit 2019
Developer toolkit (DTK) is an NVDA add-on that assists blind and visually impaired developers to independently create visually appealing user interfaces or web content. This is done by enabling DTK, navigating around the user interface or web content, then performing gestures to obtain information about the appearance, location, and size of the focused control. To enable or disable DTK, press alt+windows+k on your keyboard.
## 2019.1.2

* DTK will now report size and position values if they are 0.
* Navigation now honors the detailed messages setting.
* Made reporting of size/position information more concise.
* Stability improvements.


## 2019.1.1
* DTK will no longer attempt to load itself multiple times when announcing the version number.
* DTK features will be disabled on install. Previously, DTK features were enabled on install. This is different than enabling or disabling the add-on in the NVDA toolls>manage add-ons window.
* Messages presented to the user can now contain non-ascii characters.
* Pressing gestures such as a, b, c, f, h, l, r, s, t, v, and w no longer interupt NVDA speech when copying to the clipboard.

## 2019.1
* Fixed a compatibility problem where DTK declared a minimum NVDA version that hasn't been released yet.
## 2019.0 (initial stable release)
# Gestures
The following gestures are available when DTK is enabled.

* Alt+windows+k – Enable or disable DTK.
* Left arrow – Move to previous sibling.
* Right arrow – Move to next sibling.
* Up arrow – Move to parent.
* Down arrow – Move to first child.
* Control+home – Move to top-most parent.
* A – In web content, speak HTML attributes. Press twice quickly to copy to the clipboard.
* B – Speak the position of the object’s bottom edge. Press twice quickly to copy to the clipboard.
* C – Speak the number of children contained inside the object. Press twice quickly to copy to the clipboard.
* Control+d – Enable or disable detailed messages.
* F – In web content, speaks the object’s font and formatting information. Press twice quickly to copy to the clipboard.
* H – Speak the object’s height. Press twice quickly to copy to the clipboard.
* L – Speak the position of the object’s left edge. Press twice quickly to copy to the clipboard.
* R – Speak the position of the object’s right edge. Press twice quickly to copy to the clipboard.
* S – Speak the number of siblings relative to the object. Press twice quickly to copy to the clipboard.
* T – Speak the position of the object’s top edge. Press twice quickly to copy to the clipboard.
* V – Speak Developer toolkit version. Press twice quickly to copy to the clipboard.
* W – Speak the object’s width. Press twice quickly to copy to the clipboard.
#Notes
* DTK helps developers create user interfaces. This add-on is not an analytical tool for third-party user interfaces.
* When using Chrome, not all web elements will appear in the accessibility tree. To force an element to appear in the accessibility tree, give it a title attribute.
* When using Firefox, phantom elements may appear in the accessibility tree. For example, a text frame may appear as a text block’s container. These phantom elements are a part of Mozilla’s implementation of the accessibility tree.
* Edge has not been completely tested. Therefore, anything reported by the add-on should be considered with care.
* In web content, everything except a text block is a container. For instance, a paragraph (p tag) may have multiple elements inside.
* div tags are reported as a section in HTML5.
* To avoid names of web elements appearing as "None", always give elements a title attribute.
* Font information is only available in web content. This should be fixed in a future version.
* The add-on does not teach a user proper user interface/web content design concepts.
# Known issues
* Users are not automatically notified of the enabled/disabled state of the add-on's features when switching between windows.
* The margins of a control are only available in web content, and are browser dependent.
* The border and padding attributes are not available. This is a long-standing issue.
* There is no way to restrict DTK to a specific content type or application window.
* The font information when pressing F is messy, and will get fixed in a future version.
