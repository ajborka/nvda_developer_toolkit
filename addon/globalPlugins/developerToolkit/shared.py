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
isParentOf = lambda c, p: c in p.recursiveDescendants

def getSizeAndPosition(theObject):
	if theObject is not None and hasLocation(theObject):
		return {
			'left':theObject.location.left,
			'top':theObject.location.top,
			'right':theObject.location.right,
			'bottom':theObject.location.bottom,
			'topLeft':
				{'x':theObject.location.topLeft.x,
				'y':theObject.location.topLeft.y,},
			'topRight':
				{'x':theObject.location.topRight.x,
			'y':theObject.location.topRight.y,},
			'bottomLeft':
				{'x':theObject.location.bottomLeft.x,
				'y':theObject.location.bottomLeft.y,},
			'topRight':
				{'x':theObject.location.topRight.x,
				'y':theObject.location.topRight.y,},
			'bottomRight':
				{'x':theObject.location.bottomRight.x,
				'y':theObject.location.bottomRight.y,},
			'center':
				{'x':theObject.location.center.x,
				'y':theObject.location.center.y,},
			'height':theObject.location.height,
			'width':theObject.location.width,
		}
	else:
		return None

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

def SpeakSizeAndLocationHelper(locationAttribute, theObject):
	attribute = getSizeAndPosition(theObject)[locationAttribute]
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
