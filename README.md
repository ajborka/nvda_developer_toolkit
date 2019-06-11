# Contact information

You can subscribe to the developer toolkit addon list at nvda-developer-toolkit+subscribe@groups.io. There you can provide feedback, make feature requests, and make requests for support while using the addon.

# Documentation

The NVDA developer toolkit assists blind and visually impaired developers with the difficult task of creating appealing visual layouts for any web development project. At the moment, it provides the following features.

## Object location (in pixels)

*   left edge
*   top edge
*   right edge
*   bottom edge
*   top-left corner (coming soon)
*   top-right corner (coming soon)
*   bottom-left corner (coming soon)
*   bottom-right corner (coming soon)
*   absolute center (coming soon)
*   height
*   width

## Navigation

Navigate the accessibility tree while viewing a live page in the browser with navigation features such as 'move to document root', 'next sibling', 'previous sibling', 'first child', and 'move to parent'. When moving to a new object on the page, developer toolkit will announce the provided tag and the HTML id attribute associated with the object. If an id attribute is not present, developer toolkit will use the IA2 unique ID found in the system. In the event a tag is not present such as text directly typed into a div or other tags, developer toolkit will alert you about a missing tag associated with the text. Pressing a shortcut key will have NVDA speak a summary of the focused objects. Currently, the summary includes child count, sibling count, height and width. Pressing the speak summary shortcut twice quickly will bring up a detailed report of the control in a virtual buffer. At the moment, it only shows the focused object's size and position. Other information will be added in future updates. NVDA will announce a message indicating that navigation in the DOM is not possible when outside of the page content. Such places include Firefox menus and other dialogs.

## Browser compatibility

At this time, developer toolkit will only work with Firefox because it provides the most detailed information about the DOM.

## Keyboard shortcuts

The developer toolkit makes use of the keyboard combination CONTROL+WINDOWS as its modifyer key. Any shortcuts listed must include the toolkit modifyer key to work properly

## Desktop shortcuts (see below for laptop shortcuts)

*   numpad2: Move to the first child of the focused element.
*   numpad4: Move to the previous sibling of the focused element.
*   numpad5: Speak a short summary of the focused element. Press twice quickly to obtain a detailed report.
*   numpad6: Move to the next sibling of the focused element.
*   numpad8: Move to the parent of the focused element.
*   numpad9: Move to the root element of the document.

## Laptop shortcuts

*   comma (,): Move to the first child of the focused element.
*   j: Move to the previous sibling of the focused element.
*   k: Speak a short summary of the focused element. Press twice quickly to obtain a detailed report.
*   l: Move to the next sibling of the focused element.
*   i: Move to the parent of the focused element.
*   o: Move to the root element of the document.