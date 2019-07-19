# -*- coding: UTF-8 -*-
# Developer toolkit: Helps blind and visually impaired developers create appealing user interfaces.
# __init__.py: global plugin startup code.
# Copyright 2019 Andy Borka. Licensed under GPL2.

from __future__ import unicode_literals
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
import textInfos


confspeck = {
	"isEnabled": "boolean(default = False)",
	"isDetailedMessages": "boolean(default = True)",
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
		thisAddon = filter(lambda a: a.name == "developerToolkit", addonHandler.getAvailableAddons())[0]
		if shared.isDetailedMessages():
			message = "{}: {}".format(thisAddon.name, thisAddon.version)
		else:
			message = "{}".format(thisAddon.version)
		if getLastScriptRepeatCount() == 0:
			ui.message(message)
		elif getLastScriptRepeatCount() >= 1:
			shared.copyToClipboard(message)

	@script(description = _("Enables or disables Developer toolkit features."),
		gesture = "kb:alt+windows+k")
	def script_ToggleFeatures(self, gesture):
		if shared.developerToolkitIsEnabled():
			config.conf["developertoolkit"]["isEnabled"] = False
			self.__ToggleGestures()
			message = "Developer toolkit disabled."
			ui.message(message)
		else:
			config.conf["developertoolkit"]["isEnabled"] = True
			self.__ToggleGestures()
			message = "Developer toolkit enabled."
			ui.message(message)

	@script(_("Enables or disables detailed messages."))
	def script_ToggleDetailedMessages(self, gesture):
		if shared.isDetailedMessages():
			config.conf["developertoolkit"]["isDetailedMessages"] = False
			message = "Detailed messages disabled."
			ui.message(message)
		else:
			config.conf["developertoolkit"]["isDetailedMessages"] = True
			message = "Detailed messages enabled."
			ui.message(message)

	@script(description = _("Speaks the focused element's HTML attributes. Press twice quickly to copy to clipboard."))
	def script_SpeakHtmlAttributes(self, gesture):
		focus = api.getFocusObject()
		# Make sure we have a web element.
		if hasattr(focus, 'IA2Attributes') and focus.IA2Attributes and shared.isWebElement(focus):
			attributes = "\n".join("{}: {}".format(k, v) for k, v in sorted(focus.IA2Attributes.items()))
			# Testing how many times the script runs.
			if getLastScriptRepeatCount() == 0:
				ui.message(attributes)
			elif getLastScriptRepeatCount() >= 1:
				shared.copyToClipboard(attributes)
		# We are not in a virtual buffer.
		else:
			message = "Feature only available in web content."
			ui.message(message)

	@script(_("Speaks the position of the object's bottom edge. Press twice quickly to copy to clipboard."))
	def script_SpeakObjectBottomPosition(self, gesture):
		focus = api.getFocusObject()
		message = shared.SpeakSizeAndLocationHelper("bottom", focus)
		if getLastScriptRepeatCount() == 0:
			ui.message(message)
		elif getLastScriptRepeatCount() >= 1:
			shared.copyToClipboard(message)

	@script(_("Speaks the position of the object's left edge. Press twice quickly to copy to clipboard."))
	def script_SpeakObjectLeftPosition(self, gesture):
		focus = api.getFocusObject()
		message = shared.SpeakSizeAndLocationHelper("left", focus)
		if getLastScriptRepeatCount() == 0:
			ui.message(message)
		elif getLastScriptRepeatCount() >= 1:
			shared.copyToClipboard(message)

	@script(_("Speaks the position of the object's right edge. Press twice quickly to copy to clipboard."))
	def script_SpeakObjectRightPosition(self, gesture):
		focus = api.getFocusObject()
		message = shared.SpeakSizeAndLocationHelper("right", focus)
		if getLastScriptRepeatCount() == 0:
			ui.message(message)
		elif getLastScriptRepeatCount() >= 1:
			shared.copyToClipboard(message)

	@script(_("Speaks the position of the object's top edge. Press twice quickly to copy to clipboard."))
	def script_SpeakObjectTopPosition(self, gesture):
		focus = api.getFocusObject()
		message = shared.SpeakSizeAndLocationHelper("top", focus)
		if getLastScriptRepeatCount() == 0:
			ui.message(message)
		elif getLastScriptRepeatCount() >= 1:
			shared.copyToClipboard(message)

	@script(_("Speaks the number of children contained inside the focused object."))
	def script_SpeakChildCount(self, gesture):
		focus = api.getFocusObject()
		if shared.isDetailedMessages():
			message = "{} ({}) has {} children".format(focus.name, shared.getRoleLabel(focus), focus.childCount)
		elif not shared.isDetailedMessages():
			message = "{}".format(focus.childCount)
		if getLastScriptRepeatCount() == 0:
			ui.message(message)
		elif getLastScriptRepeatCount() >= 1:
			shared.copyToClipboard(message)

	@script(_("Speaks the focused object's height."))
	def script_SpeakObjectHeight(self, gesture):
		focus = api.getFocusObject()
		message = shared.SpeakSizeAndLocationHelper("height", focus)
		if getLastScriptRepeatCount() == 0:
			ui.message(message)
		elif getLastScriptRepeatCount() >= 1:
			shared.copyToClipboard(message)

	@script(_("Speaks the number of siblings for the focused object."))
	def script_SpeakSiblingCount(self, gesture):
		focus = api.getFocusObject()
		if focus.parent:
			siblingCount = focus.parent.childCount - 1
		elif not focus.parent:
			siblingCount = focus.childCount -1
		if shared.isDetailedMessages():
			message = "{} ({}) has {} siblings.".format(focus.name, shared.getRoleLabel(focus), siblingCount)
		elif not shared.isDetailedMessages():
			message = "{}".format(siblingCount)
		if getLastScriptRepeatCount() == 0:
			ui.message(message)
		elif getLastScriptRepeatCount() >= 1:
			shared.copyToClipboard(message)

	@script(_("Speaks the focused object's width."))
	def script_SpeakObjectWidth(self, gesture):
		focus = api.getFocusObject()
		message = shared.SpeakSizeAndLocationHelper("width", focus)
		if getLastScriptRepeatCount() == 0:
			ui.message(message)
		elif getLastScriptRepeatCount() >= 1:
			shared.copyToClipboard(message)

	@script(_("Gets the font information for an object."))
	def script_GetFontInfo(self, gesture):
		focus = api.getFocusObject()
		formatting = []
		if shared.isWebElement(focus):
			tree = focus.treeInterceptor
			info = tree.makeTextInfo(textInfos.POSITION_ALL)
			info.expand(textInfos.UNIT_CHARACTER)
			fields = info.getTextWithFields()
			for field in fields:
				if isinstance (field, textInfos.FieldCommand) and isinstance (field.field, textInfos.FormatField):
					for key in field.field:
						formatting += ["{}: {}".format(key, field.field[key])]
			message = '\n'.join(formatting)
			if getLastScriptRepeatCount() == 0:
				ui.message(message)
			elif getLastScriptRepeatCount() >= 1:
				shared.copyToClipboard(message)
		else:
			message = "Only available in web content."
			ui.message(message)


	@script(_("Moves to the object's top-most parent."))
	def script_MoveToTopParent(self, gesture):
		parents = filter(lambda p: not p.parent, api.getFocusAncestors())
		# This is not standard navigation because we jump to the top of the tree.
		if parents:
			message = shared.NavigateTo("parent", parents[0])
			ui.message(message)
		else:
			message = "No more parents."
			ui.message(message)

	@script(description = _("Moves to the focused object's parent."))
	def script_MoveToParent(self, gesture):
		focus = api.getFocusObject()
		message = shared.NavigateTo("parent", focus.parent)
		ui.message(message)
		

	@script(description = _("Moves focus to the next sibling."))
	def script_MoveToNextSibling(self, gesture):
		focus = api.getFocusObject()
		if focus.next:
			api.setFocusObject(focus.next)
			message = "{} ({})".format(focus.next.name, shared.getRoleLabel(focus.next))
			ui.message(message)
		else:
			message = "No more siblings."
			ui.message(message)

	@script(description = _("Moves focus to the previous sibling."))
	def script_MoveToPreviousSibling(self, gesture):
		focus = api.getFocusObject()
		if focus.previous:
			api.setFocusObject(focus.previous)
			message = "{} ({})".format(focus.previous.name, shared.getRoleLabel(focus.previous))
			ui.message(message)
		else:
			message = "No more siblings."
			ui.message(message)

	@script(_("Move to the focused object's first child."))
	def script_MoveToFirstChild(self, gesture):
		focus = api.getFocusObject()
		if focus.firstChild:
			api.setFocusObject(focus.firstChild)
			message = "{} ({})".format(focus.firstChild.name, shared.getRoleLabel(focus.firstChild))
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
		"kb:control+home": "MoveToTopParent",
		"kb:a": "SpeakHtmlAttributes",
		"kb:b": "SpeakObjectBottomPosition",
		"kb:c": "SpeakChildCount",
		"kb:control+d": "ToggleDetailedMessages",
		"kb:f": "GetFontInfo",
		"kb:h": "SpeakObjectHeight",
		"kb:l": "SpeakObjectLeftPosition",
		"kb:r": "SpeakObjectRightPosition",
		"kb:s": "SpeakSiblingCount",
		"kb:t": "SpeakObjectTopPosition",
		"kb:v": "SpeakVersion",
		"kb:w": "SpeakObjectWidth",
	}

