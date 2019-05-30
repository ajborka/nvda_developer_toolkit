# developer_toolkit.py
# Developer utilities for obtaining visual layout and location information for elements and controls on the screen.
# Copyright 2019 Andy Borka. Licensed under GPL2.



import globalPluginHandler
import ui
import api
import scriptHandler
from scriptHandler import script

class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	@script(
		description = _("Provides the location of the object's top edge. Press twice to place it in a virtual buffer."),
		gestures = ["kb:control+windows+numpad8",
		"kb(laptop):control+windows+i",])
	def script_getTopEdge(self, gesture):
		object = api.getNavigatorObject()
		message = "Top: " + str(object.location.top)
		if scriptHandler.getLastScriptRepeatCount() == 0:
			ui.message(message)
		elif scriptHandler.getLastScriptRepeatCount() == 1:
			ui.browseableMessage(message)

	@script(
		description = _("Provides the location of the object's right edge. Press twice to place it in a virtual buffer."),
		gestures = ["kb:control+windows+numpad4",
		"kb(laptop):control+windows+j",])
	def script_getLeftEdge(self, gesture):
		object = api.getNavigatorObject()
		message = "Left: " + str(object.location.left)
		if scriptHandler.getLastScriptRepeatCount() == 0:
			ui.message(message)
		elif scriptHandler.getLastScriptRepeatCount() == 1:
			ui.browseableMessage(message)

	@script(
		description = _("Provides the location of the object's right edge. Press twice to place it in a virtual buffer."),
		gestures = ["kb:control+windows+numpad6",
		"kb(laptop):control+windows+l",])
	def script_getRightEdge(self, gesture):
		object = api.getNavigatorObject()
		message = "Right: " + str(object.location.right)
		if scriptHandler.getLastScriptRepeatCount() == 0:
			ui.message(message)
		elif scriptHandler.getLastScriptRepeatCount() == 1:
			ui.browseableMessage(message)

	@script(
		description = _("Provides the location of the object's bottom edge. Press twice to place it in a virtual buffer."),
		gestures = ["kb:control+windows+numpad2",
		"kb(laptop):control+windows+,",])
	def script_getBottomEdge(self, gesture):
		object = api.getNavigatorObject()
		message = "Bottom: " + str(object.location.bottom)
		if scriptHandler.getLastScriptRepeatCount() == 0:
			ui.message(message)
		elif scriptHandler.getLastScriptRepeatCount() == 1:
			ui.browseableMessage(message)

	@script(
		description = _("Provides the left and top coordinates for the object's absolute center. Press twice to place it in a virtual buffer."),
		gestures = ["kb:control+windows+numpad5",
		"kb(laptop):control+windows+k",])
	def script_getCenterPoints(self, gesture):
		object = api.getNavigatorObject()
		message = "Center = Left: " + str(object.location.center.x) + ", top: " + str(object.location.center.y)
		if scriptHandler.getLastScriptRepeatCount() == 0:
			ui.message(message)
		elif scriptHandler.getLastScriptRepeatCount() == 1:
			ui.browseableMessage(message)

	@script(
		description = _("Provides the left and top coordinates for the object's top-left corner. Press twice to place it in a virtual buffer."),
		gestures = ["kb:control+windows+numpad7",
		"kb(laptop):control+windows+u",])
	def script_getTopLeftPoints(self, gesture):
		object = api.getNavigatorObject()
		message = "Top-left = Left: " + str(object.location.topLeft.x) + ", top: " + str(object.location.topLeft.y)
		if scriptHandler.getLastScriptRepeatCount() == 0:
			ui.message(message)
		elif scriptHandler.getLastScriptRepeatCount() == 1:
			ui.browseableMessage(message)

	@script(
		description = _("Provides the top-right coordinates for the object's top-right corner. Press twice to place it in a virtual buffer."),
		gestures = ["kb:control+windows+numpad9",
		"kb(laptop):control+windows+o",])
	def script_gettopRightPoints(self, gesture):
		object = api.getNavigatorObject()
		message = "Top-right = Top: " + str(object.location.topRight.y) + ", Right: " + str(object.location.topRight.x)
		if scriptHandler.getLastScriptRepeatCount() == 0:
			ui.message(message)
		elif scriptHandler.getLastScriptRepeatCount() == 1:
			ui.browseableMessage(message)

	@script(
		description = _("Provides the Bottom-left coordinates for the object's bottom-left corner. Press twice to place it in a virtual buffer."),
		gestures = ["kb:control+windows+numpad1",
		"kb(laptop):control+windows+m",])
	def script_getBottomLeftPoints(self, gesture):
		object = api.getNavigatorObject()
		message = "Bottom-left = Left: " + str(object.location.bottomLeft.x) + ", Bottom: " + str(object.location.bottomLeft.y)
		if scriptHandler.getLastScriptRepeatCount() == 0:
			ui.message(message)
		elif scriptHandler.getLastScriptRepeatCount() == 1:
			ui.browseableMessage(message)

	@script(
		description = _("Provides the Bottom-right coordinates for the object's Bottom-right corner. Press twice to place it in a virtual buffer."),
		gestures = ["kb:control+windows+numpad3",
		"kb(laptop):control+windows+.",])
	def script_getBottomRightPoints(self, gesture):
		object = api.getNavigatorObject()
		message = "Bottom-right = Left: " + str(object.location.bottomRight.x) + ", Bottom: " + str(object.location.bottomRight.y)
		if scriptHandler.getLastScriptRepeatCount() == 0:
			ui.message(message)
		elif scriptHandler.getLastScriptRepeatCount() == 1:
			ui.browseableMessage(message)

	@script(
		description = _("Provides the object's height. Press twice to place it in a virtual buffer."),
		gestures = ["kb:control+windows+numpadPlus",
		"kb(laptop):control+windows+[",])
	def script_getHeight(self, gesture):
		object = api.getNavigatorObject()
		message = "Height: " + str(object.location.height)
		if scriptHandler.getLastScriptRepeatCount() == 0:
			ui.message(message)
		elif scriptHandler.getLastScriptRepeatCount() == 1:
			ui.browseableMessage(message)

	@script(
		description = _("Provides the object's width. Press twice to place it in a virtual buffer."),
		gestures = ["kb:control+windows+numpadEnter",
		"kb(laptop):control+windows+]",])
	def script_getWidth(self, gesture):
		object = api.getNavigatorObject()
		message = "Width: " + str(object.location.width)
		if scriptHandler.getLastScriptRepeatCount() == 0:
			ui.message(message)
		elif scriptHandler.getLastScriptRepeatCount() == 1:
			ui.browseableMessage(message)

