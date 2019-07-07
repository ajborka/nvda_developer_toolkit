# Developer toolkit: Helps blind and visually impaired developers create appealing user interfaces.
# __init__.py: global plugin startup code.
# Copyright 2019 Andy Borka. Licensed under GPL2.

import addonHandler
import globalPluginHandler
import config
import gui
from scriptHandler import getLastScriptRepeatCount
from scriptHandler import script
import wx
import ui
from . import dialogs
from . import shared
import api


confspeck = {
	"isEnabled": "boolean(default = True)",
	"isDetailedMessages": "boolean(default = False)",
}
config.conf.spec["developertoolkit"] = confspeck


### global plugin
class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	scriptCategory = _("Developer toolkit")

	def __init__(self):
		super(GlobalPlugin, self).__init__()
		gui.settingsDialogs.NVDASettingsDialog.categoryClasses.append(dialogs.DtkSettingsPanel)

	@script(_("Speaks The addon's version number. Press twice quickly to copy to the clipboard."))
	def script_SpeakVersion(self, gesture):
		thisAddon = addonHandler.Addon
		for addon in addonHandler.getAvailableAddons():
			if addon.name == "developerToolkit":
				thisAddon = addon
		if shared.isDetailedMessages():
			message = u"{}: {}".format(thisAddon.name, thisAddon.version)
		elif not shared.isDetailedMessages():
			message = u"{}".format(thisAddon.version)
		if getLastScriptRepeatCount() == 0:
			ui.message(message)
		elif getLastScriptRepeatCount() == 1:
			shared.copyToClipboard(message)


	@script(description = _("Enables or disables Developer toolkit features."),
		gesture = "kb:alt+windows+k")
	def script_ToggleFeatures(self, gesture):
		if shared.developerToolkitIsEnabled():
			config.conf["developertoolkit"]["isEnabled"] = False
			self.__ToggleGestures()
			ui.message("Developer toolkit disabled.")
		elif not shared.developerToolkitIsEnabled():
			config.conf["developertoolkit"]["isEnabled"] = True
			self.__ToggleGestures()
			ui.message("Developer toolkit enabled.")

	@script(_("Enables or disables detailed messages."))
	def script_ToggleDetailedMessages(self, gesture):
		if shared.isDetailedMessages():
			config.conf["developertoolkit"]["isDetailedMessages"] = False
			ui.message(_("Detailed messages disabled."))
		elif not shared.isDetailedMessages():
			config.conf["developertoolkit"]["isDetailedMessages"] = True
			ui.message(_("Detailed messages enabled."))


	@script(description = _("Speaks the focused element's HTML attributes. Press twice quickly to copy to clipboard."))
	def script_SpeakHtmlAttributes(self, gesture):
		attributes = []
		focus = api.getFocusObject()
		# Make sure we have a web element.
		if hasattr(focus, 'IA2Attributes') and focus.IA2Attributes and shared.isWebElement(focus):
			# Split the attributes in key/value pairs.
			for key in focus.IA2Attributes:
				attributes += ["%s: %s" % (key, focus.IA2Attributes[key])]
			# Testing how many times the script runs.
			if getLastScriptRepeatCount() == 0:
				message = "\n".join(attributes)
				ui.message(message)
			elif getLastScriptRepeatCount() == 1:
				message = "\n".join(attributes)
				shared.copyToClipboard(message)
		# We are not in a virtual buffer.
		else:
			ui.message("Feature only available in web content.")

	@script(_("Speaks the position of the object's bottom edge."))
	def script_SpeakObjectBottomPosition(self, gesture):
		focus = api.getFocusObject()
		if hasattr(focus, 'location'):
			bottomEdge = shared.getSizeAndPosition(focus)["bottom"]
			message = u"{} ({})'s bottom edge is {} pixels from top edge of window.".format(focus.name, shared.getRoleLabel(focus), bottomEdge)
		if getLastScriptRepeatCount() == 0:
			ui.message(message)
		elif getLastScriptRepeatCount() == 1:
			shared.copyToClipboard(message)



	@script(_("Speaks the number of children contained inside the focused object."))
	def script_SpeakChildCount(self, gesture):
		focus = api.getFocusObject()
		message = "{} ({}) has {} children".format(focus.name, shared.getRoleLabel(focus), focus.childCount)
		if getLastScriptRepeatCount() == 0:
			ui.message(message)
		elif getLastScriptRepeatCount() == 1:
			shared.copyToClipboard(message)

	@script(_("Speaks the focused object's height."))
	def script_SpeakObjectHeight(self, gesture):
		focus = api.getFocusObject()
		height = shared.getSizeAndPosition(focus)["height"]
		message = ""
		try:
			message = _("{} ({}) is {} pixels high.".format(focus.name, shared.getRoleLabel(focus), height))
		except UnicodeEncodeError:
			message = "Height not available."
		if getLastScriptRepeatCount() == 0:
			ui.message(message)
		elif getLastScriptRepeatCount() == 1:
			shared.copyToClipboard(message)

	@script(_("Speaks the number of siblings for the focused object."))
	def script_SpeakSiblingCount(self, gesture):
		focus = api.getFocusObject()
		if focus.parent:
			siblingCount = focus.parent.childCount - 1
		elif not focus.parent:
			siblingCount = focus.childCount -1
		message = _("{} ({}) has {} siblings.".format(focus.name, shared.getRoleLabel(focus), siblingCount))
		if getLastScriptRepeatCount() == 0:
			ui.message(message)
		elif getLastScriptRepeatCount() == 1:
			shared.copyToClipboard(message)

	@script(_("Speaks the focused object's width."))
	def script_SpeakObjectWidth(self, gesture):
		focus = api.getFocusObject()
		width = shared.getSizeAndPosition(focus)["width"]
		message = ""
		try:
			message = _("{} ({}) is {} pixels wide.".format(focus.name, shared.getRoleLabel(focus), width))
		except UnicodeEncodeError:
			message = "Width not available."
		if getLastScriptRepeatCount() == 0:
			ui.message(message)
		elif getLastScriptRepeatCount() == 1:
			shared.copyToClipboard(message)


	@script(description = _("Moves to the focused object's parent."))
	def script_MoveToParent(self, gesture):
		focus = api.getFocusObject()
		if focus.parent:
			api.setFocusObject(focus.parent)
			message = _("{} ({})".format(focus.parent.name, shared.getRoleLabel(focus.parent)))
			ui.message(message)
		elif not focus.parent:
			message = "No more parents."
			ui.message(message)

	@script(description = _("Moves focus to the next sibling."))
	def script_MoveToNextSibling(self, gesture):
		focus = api.getFocusObject()
		if focus.next:
			api.setFocusObject(focus.next)
			message = ""
			try:
				message = _("{} ({})".format(focus.next.name, shared.getRoleLabel(focus.next)))
			except UnicodeEncodeError:
				message = "Unknown control."
			ui.message(message)
		else:
			message = "No more siblings."
			ui.message(message)

	@script(description = _("Moves focus to the previous sibling."))
	def script_MoveToPreviousSibling(self, gesture):
		focus = api.getFocusObject()
		if focus.previous:
			api.setFocusObject(focus.previous)
			message= ""
			try:
				message = _("{} ({})".format(focus.previous.name, shared.getRoleLabel(focus.previous)))
			except UnicodeEncodeError:
				message = "Unknown control."
			ui.message(message)
		else:
			message = "No more siblings."
			ui.message(message)

	@script(_("Move to the focused object's first child."))
	def script_MoveToFirstChild(self, gesture):
		focus = api.getFocusObject()
		if focus.firstChild:
			api.setFocusObject(focus.firstChild)
			message = _("{} ({})".format(focus.firstChild.name, shared.getRoleLabel(focus.firstChild)))
			ui.message(message)
		else:
			message = "No more children."
			ui.message(message)



	def __ToggleGestures(self):
		# Developer toolkit is enabled, bind gestures.
		if shared.developerToolkitIsEnabled():
			for key in self.__developerToolkitGestures:
				self.bindGesture(key, self.__developerToolkitGestures[key])
		# Developer toolkit is disabled, remove gestures.
		elif not shared.developerToolkitIsEnabled():
			for key in self.__developerToolkitGestures:
				try:
					self.removeGestureBinding(key)
				except KeyError:
					pass
			# Rebind features toggle because it was removed.
			self.bindGesture("kb:alt+windows+k", "ToggleFeatures")



	__developerToolkitGestures = {
		"kb:alt+windows+k": "ToggleFeatures",
		"kb:leftArrow": "MoveToPreviousSibling",
		"kb:rightArrow": "MoveToNextSibling",
		"kb:upArrow": "MoveToParent",
		"kb:downArrow": "MoveToFirstChild",
		#"kb:end": "LastChild",
		#"kb:control+home": "DocumentRoot",
		"kb:a": "SpeakHtmlAttributes",
		"kb:b": "SpeakObjectBottomPosition",
		"kb:c": "SpeakChildCount",
		"kb:control+d": "ToggleDetailedMessages",
		"kb:h": "SpeakObjectHeight",
		"kb:s": "SpeakSiblingCount",
		"kb:v": "SpeakVersion",
		"kb:w": "SpeakObjectWidth",
	}

