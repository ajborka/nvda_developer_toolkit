# shared.py
# Shared library for Developer toolkit.
# A part of Developer toolkit.
# Copyright 2019 Andy Borka. Released under GPL. See License for details.

from __future__ import unicode_literals
import api
import config
from controlTypes import roleLabels
from controlTypes import stateLabels
import ui
from virtualBuffers import VirtualBuffer

isWebElement = lambda theObject: isinstance(theObject.treeInterceptor, VirtualBuffer)
developerToolkitIsEnabled = lambda : config.conf["developertoolkit"]["isEnabled"]
isDetailedMessages = lambda : config.conf["developertoolkit"]["isDetailedMessages"]
hasLocation = lambda theObject: hasattr(theObject, 'location')
isFocusAncestor = lambda a: a in api.getFocusAncestors()

def getSizeAndPosition(descendant, ancestor):
	if descendant and not isFocusAncestor(ancestor) and hasLocation(descendant):
		return {
			'left':descendant.location.left,
			'top':descendant.location.top,
			'right':descendant.location.right,
			'bottom':descendant.location.bottom,
			'height':descendant.location.height,
			'width':descendant.location.width,
		}
	elif descendant and isFocusAncestor(ancestor) and hasLocation(descendant):
		return {
			'left':descendant.location.left - ancestor.location.left,
			'top':descendant.location.top - ancestor.location.top,
			'right':descendant.location.right - ancestor.location.left,
			'bottom':descendant.location.bottom - ancestor.location.top,
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
	if attribute > -1:
		if isDetailedMessages():
			return "{} pixels.".format(attribute)
		else:
			return "{}".format(attribute)
	else:
		return "{} not available.".format(locationAttribute)

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
