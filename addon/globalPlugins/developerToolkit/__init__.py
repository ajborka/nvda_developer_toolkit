# Developer toolkit: Helps blind and visually impaired developers create appealing user interfaces.
# __init__.py: global plugin features.
# Copyright 2019 - 2020 Andy Borka. Licensed under GPL2.

import addonHandler
import globalPluginHandler
from globalCommands import GlobalCommands as commands
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
	"fontInfo": "string_list(default= list('font-family', 'font-size', 'color', 'background-color'))",
	"displayColorFormat": "integer(min = 0, max = 2, default = 0)",
}
config.conf.spec["developertoolkit"] = confspeck


### global plugin
class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	scriptCategory = u"Developer toolkit"
	# Make the most reasonable choice by default.
	relativeParent = api.getDesktopObject()

	def __init__(self):
		super(GlobalPlugin, self).__init__()
		config.post_configProfileSwitch.register(
			self.handleConfigProfileSwitch)
		gui.settingsDialogs.NVDASettingsDialog.categoryClasses.append(
			dialogs.DtkSettingsPanel)

	def terminate(self):
		gui.settingsDialogs.NVDASettingsDialog.categoryClasses.remove(
			dialogs.DtkSettingsPanel)

	@script(description=u"Speaks The addon's version number. Press twice quickly to copy to the clipboard.")
	def script_SpeakVersion(self, gesture):
		thisAddon = list(filter(
			lambda a: a.name == "developerToolkit", addonHandler.getAvailableAddons()))[0]
		if shared.isDetailedMessages():
			message = u"{}: {}".format(thisAddon.name, thisAddon.version)
		else:
			message = u"{}".format(thisAddon.version)
		if getLastScriptRepeatCount() == 0:
			ui.message(message)
		elif getLastScriptRepeatCount() >= 1:
			shared.copyToClipboard(message)

	@script(description=u"Enables or disables Developer toolkit features.",
			gesture="kb:alt+windows+k")
	def script_ToggleFeatures(self, gesture):
		focus = api.getNavigatorObject()
		if shared.developerToolkitIsEnabled():
			config.conf["developertoolkit"]["isEnabled"] = False
			self.__ToggleGestures()
			message = u"Developer toolkit disabled."
			ui.message(message)
		else:
			config.conf["developertoolkit"]["isEnabled"] = True
			if shared.isWebElement(focus):
				shared.NavigateTo(None, focus)
			self.__ToggleGestures()
			message = u"Developer toolkit enabled."
			ui.message(message)

	@script(description=u"Enables or disables detailed messages.")
	def script_ToggleDetailedMessages(self, gesture):
		if shared.isDetailedMessages():
			config.conf["developertoolkit"]["isDetailedMessages"] = False
			message = u"Detailed messages disabled."
			ui.message(message)
		else:
			config.conf["developertoolkit"]["isDetailedMessages"] = True
			message = u"Detailed messages enabled."
			ui.message(message)

	@script(description=u"Speaks the focused element's HTML attributes. Press twice quickly to copy to clipboard.")
	def script_SpeakHtmlAttributes(self, gesture):
		focus = api.getFocusObject()
		# Make sure we have a web element.
		if hasattr(focus, 'IA2Attributes') and focus.IA2Attributes and shared.isWebElement(focus):
			attributes = u"\n".join("{}: {}".format(k, v)
									for k, v in sorted(focus.IA2Attributes.items()))
			# Testing how many times the script runs.
			if getLastScriptRepeatCount() == 0:
				ui.message(attributes)
			elif getLastScriptRepeatCount() >= 1:
				shared.copyToClipboard(attributes)
		# We are not in a virtual buffer.
		else:
			message = u"Feature only available in web content."
			ui.message(message)

	@script(description=u"Speaks the position of the object's bottom edge. Press twice quickly to copy to clipboard.")
	def script_SpeakObjectBottomPosition(self, gesture):
		focus = api.getFocusObject()
		message = shared.SpeakSizeAndLocationHelper(
			u"bottom", focus, self.relativeParent)
		if getLastScriptRepeatCount() == 0:
			ui.message(message)
		elif getLastScriptRepeatCount() >= 1:
			shared.copyToClipboard(message)

	@script(description=u"Speaks the position of the object's left edge. Press twice quickly to copy to clipboard.")
	def script_SpeakObjectLeftPosition(self, gesture):
		focus = api.getFocusObject()
		message = shared.SpeakSizeAndLocationHelper(
			u"left", focus, self.relativeParent)
		if getLastScriptRepeatCount() == 0:
			ui.message(message)
		elif getLastScriptRepeatCount() >= 1:
			shared.copyToClipboard(message)

	@script(description=u"Speaks the position of the object's right edge. Press twice quickly to copy to clipboard.")
	def script_SpeakObjectRightPosition(self, gesture):
		focus = api.getFocusObject()
		message = shared.SpeakSizeAndLocationHelper(
			u"right", focus, self.relativeParent)
		if getLastScriptRepeatCount() == 0:
			ui.message(message)
		elif getLastScriptRepeatCount() >= 1:
			shared.copyToClipboard(message)

	@script(description=u"Speaks the object's right edge location relative to the relative parent's right edge.")
	def script_SpeakObjectRightPositionToRelativeParentRightPosition(self, gesture):
		focus = api.getFocusObject()
		message = shared.SpeakSizeAndLocationHelper(
			u"right-right", focus, self.relativeParent)
		if getLastScriptRepeatCount() == 0:
			ui.message(message)
		elif getLastScriptRepeatCount() >= 1:
			shared.copyToClipboard(message)

	@script(description=u"Speaks the object's bottom edge relative to the relative parent's bottom edge.")
	def script_SpeakObjectBottomPositionToRelativeParentBottomPosition(self, gesture):
		focus = api.getFocusObject()
		message = shared.SpeakSizeAndLocationHelper(
			u"bottom-bottom", focus, self.relativeParent)
		if getLastScriptRepeatCount() == 0:
			ui.message(message)
		elif getLastScriptRepeatCount() >= 1:
			shared.copyToClipboard(message)

	@script(description=u"Speaks the position of the object's top edge. Press twice quickly to copy to clipboard.")
	def script_SpeakObjectTopPosition(self, gesture):
		focus = api.getFocusObject()
		message = shared.SpeakSizeAndLocationHelper(
			u"top", focus, self.relativeParent)
		if getLastScriptRepeatCount() == 0:
			ui.message(message)
		elif getLastScriptRepeatCount() >= 1:
			shared.copyToClipboard(message)

	@script(description=u"Speaks the number of children contained inside the focused object.")
	def script_SpeakChildCount(self, gesture):
		focus = api.getFocusObject()
		if shared.isDetailedMessages():
			message = u"{} ({}) has {} children".format(
				focus.name, shared.getRoleLabel(focus), focus.childCount)
		elif not shared.isDetailedMessages():
			message = u"{}".format(focus.childCount)
		if getLastScriptRepeatCount() == 0:
			ui.message(message)
		elif getLastScriptRepeatCount() >= 1:
			shared.copyToClipboard(message)

	@script(description = u"Speaks the object's role or control type.")
	def script_SpeakRole(self, gesture):
		focus = api.getFocusObject()
		label = shared.getRoleLabel(focus)
		if not label:
			mesage = u"Role or control type not available!"
		else:
			if shared.isDetailedMessages():
				mesage = u"Role: {}".format(label)
			else:
				mesage = u"{}".format(label)
		if getLastScriptRepeatCount() == 0:
			ui.message(mesage)
		elif getLastScriptRepeatCount() >= 1:
			shared.copyToClipboard(mesage)

	@script(description = u"Speaks the object's control states. Press twice quickly to copy to the clipboard.")
	def script_SpeakStates(self, gesture):
		focus = api.getFocusObject()
		controlStates = shared.getStateLabels(focus)
		if len(controlStates) == 0:
			message = u"The control's states are not available!"
		elif len(controlStates) >= 1:
			message = u"\n".join(controlStates)
		if getLastScriptRepeatCount() == 0:
			ui.message(message)
		elif getLastScriptRepeatCount() >= 1:
			shared.copyToClipboard(message)
			
	@script(description=u"Changes the way color values are displayed.")
	def script_ChangeColorValueFormat(self, gesture):
		"""Changes the way color values are displayed.
		Options include: 0 for RGB, 1 for Hex, and 2 for Name."""
		if shared.colorAsRGB():
			config.conf["developertoolkit"]["displayColorFormat"] = 1
			mesage = u"Display color values as Hex."
		elif shared.colorAsHex():
			config.conf["developertoolkit"]["displayColorFormat"] = 2
			mesage = u"Display color values as Name."
		elif shared.colorAsName():
			config.conf["developertoolkit"]["displayColorFormat"] = 0
			mesage = u"Display color values as RGB."
		ui.message(mesage)

	@script(description=u"Speaks the focused object's height.")
	def script_SpeakObjectHeight(self, gesture):
		focus = api.getFocusObject()
		message = shared.SpeakSizeAndLocationHelper(
			u"height", focus, self.relativeParent)
		if getLastScriptRepeatCount() == 0:
			ui.message(message)
		elif getLastScriptRepeatCount() >= 1:
			shared.copyToClipboard(message)

	@script(description=u"Speaks the number of siblings for the focused object.")
	def script_SpeakSiblingCount(self, gesture):
		focus = api.getFocusObject()
		if focus.parent:
			siblingCount = focus.parent.childCount - 1
		elif not focus.parent:
			siblingCount = focus.childCount - 1
		if shared.isDetailedMessages():
			message = u"{} ({}) has {} siblings.".format(
				focus.name, shared.getRoleLabel(focus), siblingCount)
		elif not shared.isDetailedMessages():
			message = u"{}".format(siblingCount)
		if getLastScriptRepeatCount() == 0:
			ui.message(message)
		elif getLastScriptRepeatCount() >= 1:
			shared.copyToClipboard(message)

	@script(description=u"Speaks the focused object's width.")
	def script_SpeakObjectWidth(self, gesture):
		focus = api.getFocusObject()
		message = shared.SpeakSizeAndLocationHelper(
			u"width", focus, self.relativeParent)
		if getLastScriptRepeatCount() == 0:
			ui.message(message)
		elif getLastScriptRepeatCount() >= 1:
			shared.copyToClipboard(message)

	@script(description=u"Reports formatting information for an object.")
	def script_GetFontInfo(self, gesture):
		focus = api.getFocusObject()
		formatting = []
		if shared.isWebElement(focus):
			info = focus.makeTextInfo(textInfos.POSITION_CARET)
			info.expand(textInfos.UNIT_CHARACTER)
			fields = info.getTextWithFields()
			for field in fields:
				if isinstance(field, textInfos.FieldCommand) and isinstance(field.field, textInfos.FormatField):
					for key in config.conf["developertoolkit"]["fontInfo"]:
						try:
							if shared.isDetailedMessages():
								# Specialized color formatting rules.
								if shared.isColor(field.field[key]):
									if shared.colorAsName():
										formatting.append(u"{}: {}".format(
											key, field.field[key].name))
									elif shared.colorAsHex():
										formatting.append(u"{}: #{:02x}{:02x}{:02x}".format(
											key, field.field[key].red, field.field[key].green, field.field[key].blue))
									elif shared.colorAsRGB():
										formatting .append(
											u"{}: {}".format(key, field.field[key]))
								# There are no more specialized formatting rules to apply.
								else:
									formatting .append(
										u"{}: {}".format(key, field.field[key]))
							# Formatting rules to apply when detailed messages is disabled.
							else:
								# Specialized rules to apply when the formatting fields have True/False values such as bold, italic, underline.
								if shared.isBool(field.field[key]):
									if field.field[key] == True:
										formatting.append(u"{}".format(key))
									else:
										pass
								# The formatting rules for color values.
								elif shared.isColor(field.field[key]):
									if shared.colorAsName():
										formatting.append(
											u"{}".format(field.field[key].name))
									elif shared.colorAsHex():
										formatting.append(u"#{:02x}{:02x}{:02x}".format(
											field.field[key].red, field.field[key].green, field.field[key].blue))
									elif shared.colorAsRGB():
										formatting.append(u"RGB({}, {}, {})".format(
											field.field[key].red, field.field[key].green, field.field[key].blue))
								# There are no more formatting rules to follow.
								else:
									formatting.append(
										u"{}".format(field.field[key]))
						except KeyError:
							pass
			message = u"\n".join(formatting)
			if getLastScriptRepeatCount() == 0:
				ui.message(message)
			elif getLastScriptRepeatCount() >= 1:
				shared.copyToClipboard(message)
		else:
			message = u"Only available in web content."
			ui.message(message)

	@script(description=u"Speaks the object's name. Press twice quickly to copy to the clipboard.")
	def script_SpeakName(self, gesture):
		focus = api.getFocusObject()
		if shared.isDetailedMessages():
			message = u"Name: {}".format(focus.name)
		else:
			message = u"{}".format(focus.name)
		if getLastScriptRepeatCount() == 0:
			ui.message(message)
		elif getLastScriptRepeatCount() >= 1:
			shared.copyToClipboard(message)

	@script(description=u"Moves to the object's top-most parent.")
	def script_MoveToTopParent(self, gesture):
		parents = list(filter(lambda p: not p.parent, api.getFocusAncestors()))
		# This is not standard navigation because we jump to the top of the tree.
		if parents:
			message = shared.NavigateTo(u"parent", parents[0])
			ui.message(message)
		else:
			message = u"No more parents."
			ui.message(message)

	@script(description = u'Moves to the relative parent.')
	def script_MoveToRelativeParent(self, gesture):
		message = shared.NavigateTo(u'parent', self.relativeParent)
		ui.message(message)

	@script(description=u"Moves to the focused object's parent.")
	def script_MoveToParent(self, gesture):
		focus = api.getFocusObject()
		message = shared.NavigateTo(u"parent", focus.parent)
		ui.message(message)

	@script(description=u"Moves focus to the next sibling.")
	def script_MoveToNextSibling(self, gesture):
		focus = api.getFocusObject()
		message = shared.NavigateTo(u"sibling", focus.next)
		ui.message(message)

	@script(description=u"Moves focus to the previous sibling.")
	def script_MoveToPreviousSibling(self, gesture):
		focus = api.getFocusObject()
		message = shared.NavigateTo(u"sibling", focus.previous)
		ui.message(message)

	@script(description=u"Move to the focused object's first child.")
	def script_MoveToFirstChild(self, gesture):
		focus = api.getFocusObject()
		message = shared.NavigateTo(u"child", focus.firstChild)
		ui.message(message)

	def __ToggleGestures(self):
		if shared.developerToolkitIsEnabled():
			for key in self.__developerToolkitGestures:
				self.bindGesture(key, self.__developerToolkitGestures[key])
		else:
			for key in self.__developerToolkitGestures:
				try:
					self.removeGestureBinding(key)
				except KeyError:
					pass
			# Rebind features toggle because it was removed.
			self.bindGesture("kb:alt+windows+k", "ToggleFeatures")

	def handleConfigProfileSwitch(self):
		if shared.developerToolkitIsEnabled():
			config.conf["developertoolkit"]["isEnabled"] = True
			self.__ToggleGestures()
		else:
			config.conf["developertoolkit"]["isEnabled"] = False
			self.__ToggleGestures()

	@script(description=u"Sets the relative parent to use in obtaining an object's position.")
	def script_SetRelativeParent(self, gesture):
		self.relativeParent = api.getFocusObject()
		if self.relativeParent:
			message = u"Set to {}".format(self.relativeParent.name)
		ui.message(message)

	@script(description=u"Speaks the relative parent's name.")
	def script_SpeakRelativeParentName(self, gesture):
		if self.relativeParent:
			if shared.isDetailedMessages():
				message = u"{} ({})".format(
					self.relativeParent.name, shared.getRoleLabel(self.relativeParent))
			else:
				message = u"{}".format(self.relativeParent.name)
		else:
			message = u"Name not available."
		if getLastScriptRepeatCount() == 0:
			ui.message(message)
		elif getLastScriptRepeatCount() >= 1:
			shared.copyToClipboard(message)

	__developerToolkitGestures = {
		"kb:alt+windows+k": "ToggleFeatures",
		"kb:leftArrow": "MoveToPreviousSibling",
		"kb:rightArrow": "MoveToNextSibling",
		"kb:upArrow": "MoveToParent",
		"kb:downArrow": "MoveToFirstChild",
		"kb:home": "MoveToRelativeParent",
		"kb:control+home": "MoveToTopParent",
		"kb:a": "SpeakHtmlAttributes",
		"kb:b": "SpeakObjectBottomPosition",
		"kb:shift+b": "SpeakObjectBottomPositionToRelativeParentBottomPosition",
		"kb:c": "SpeakChildCount",
		"kb:control+c": "ChangeColorValueFormat",
		"kb:control+d": "ToggleDetailedMessages",
		"kb:f": "GetFontInfo",
		"kb:h": "SpeakObjectHeight",
		"kb:l": "SpeakObjectLeftPosition",
		"kb:n": "SpeakName",
		"kb:control+p": "SetRelativeParent",
		"kb:p": "SpeakRelativeParentName",
		"kb:r": "SpeakObjectRightPosition",
		"kb:shift+r": "SpeakObjectRightPositionToRelativeParentRightPosition",
		"kb:alt+r": "SpeakRole",
		"kb:s": "SpeakSiblingCount",
		"kb:shift+s": "SpeakStates",
		"kb:t": "SpeakObjectTopPosition",
		"kb:v": "SpeakVersion",
		"kb:w": "SpeakObjectWidth",
	}
