# shared.py
# Shared library for Developer toolkit.
# A part of Developer toolkit.
# Copyright 2019 Andy Borka. Released under GPL. See License for details.

from __future__ import unicode_literals
import api
import config
from controlTypes import roleLabels
from controlTypes import stateLabels
import globalPluginHandler
import ui
from virtualBuffers import VirtualBuffer

isWebElement = lambda theObject: isinstance(theObject.treeInterceptor, VirtualBuffer)
developerToolkitIsEnabled = lambda : config.conf["developertoolkit"]["isEnabled"]
isDetailedMessages = lambda : config.conf["developertoolkit"]["isDetailedMessages"]
hasLocation = lambda theObject: hasattr(theObject, 'location')
isFocusAncestor = lambda a: a in api.getFocusAncestors()

def getSizeAndPosition(descendant, ancestor):
	# The relative parent isn't an ancestor of the descendant.
	if descendant and not isFocusAncestor(ancestor) and hasLocation(descendant):
		dtk = list(filter(lambda p: isinstance(p, globalPluginHandler.globalPlugins.developerToolkit.GlobalPlugin), globalPluginHandler.runningPlugins))[0]
		dtk.relativeParent = api.getDesktopObject()
		return {
			'left':descendant.location.left,
			'top':descendant.location.top,
			'right':descendant.location.right,
			'bottom':descendant.location.bottom,
						'bottom-bottom':ancestor.location.bottom - descendant.location.bottom,
			'right-right':ancestor.location.right - descendant.location.right,

			'height':descendant.location.height,
			'width':descendant.location.width,
		}
	# The relative parent is an ancestor of the descendant.
	if descendant and isFocusAncestor(ancestor) and hasLocation(descendant):
		return {
			'left':descendant.location.left - ancestor.location.left,
			'top':descendant.location.top - ancestor.location.top,
			'right':descendant.location.right - ancestor.location.left,
			'bottom':descendant.location.bottom - ancestor.location.top,
			'bottom-bottom':ancestor.location.bottom - descendant.location.bottom,
			'right-right':ancestor.location.right - descendant.location.right,
			'height':descendant.location.height,
			'width':descendant.location.width,
		}


def copyToClipboard(ObjectToCopy):
	if api.copyToClip(ObjectToCopy):
		message = "Copied to clipboard."
		ui.message(message)
	else:
		message = "Copy faildd."
		ui.message(message)

def getRoleLabel(theObject):
	key =theObject.role
	return roleLabels[key]

def SpeakSizeAndLocationHelper(locationAttribute, descendant, ancestor):
	attribute = getSizeAndPosition(descendant, ancestor)[locationAttribute]
	if isDetailedMessages():
		return "{} pixels.".format(attribute)
	else:
		return "{}".format(attribute)

def NavigateTo(relationship, theObject):
	if theObject:
		api.setFocusObject(theObject)
		if isDetailedMessages():
			return "{}: {}".format(theObject.name, getRoleLabel(theObject))
		else:
			return "{}".format(theObject.name)
	else:
		# child relationship doesn't fit the typical plural form of the other relationships.
		if relationship == "child":
			return "No more children."
		else:
			return "No more {}s.".format(relationship)
