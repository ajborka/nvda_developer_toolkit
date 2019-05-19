# developer_toolkit.py
# Developer utilities for obtaining visual layout and location information for elements and controls on the screen.
# Copyright 2019 Andy Borka. Licensed under GPL2.



import globalPluginHandler
import ui
import api
from scriptHandler import script

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	@script(
		description = _("Obtain object location in pixels."),
		gesture = "kb:NVDA+shift+numpadDelete")
	def script_sayObjectLocation(self, gesture):
		"""Obtains the location and size of screen elements on the visible portion of the screen."""
		
		object = None # Start with an undefined object.
		
		# Determine if we should report the navigator object or the currently focused item.
		if api.getNavigatorObject() is not api.getFocusObject():
		# Get the navigator object.
			object = api.getNavigatorObject()
		else:
			# Get the focused object since the user didn't activate the navigator object.
			object = api.getFocusObject()
		
		# Sanity check for objects not visible on the active display.
		if (object.isInForeground) == False or (
			object.location.left == 0 and
			object.location.top == 0 and
			object.location.width ==0 and
			object.location.height == 0):
				ui.message("Object not visible.")
		else:
			ui.message("Left: %s. Top: %s. Width: %s. Height: %s." % (
				object.location.left,
				object.location.top,
				object.location.width,
				object.location.height))
