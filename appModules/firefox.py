# developer_toolkit.py
# Web developer utilities for obtaining visual layout and location information for elements and controls on the screen. If none present, use object.IA2UniqueID.
# Todo: 
# * put keyboard shortcuts in gesture objects.
# * Add keyboard shortcuts for size/locations of elements.
# * Remove detailed report feature.
# * Implement addon on/off toggle.
# * Remove element summary mode.

# Firefox module. See others as they become available.
# Copyright 2019 Andy Borka. Licensed under GPL2.

import appModuleHandler
import config
import addonHandler
import ui
import api
from scriptHandler import script
from scriptHandler import getLastScriptRepeatCount
from eventHandler import executeEvent
from virtualBuffers.gecko_ia2 import Gecko_ia2

class AppModule(appModuleHandler.AppModule):

	scriptCategory = "Developer toolkit"

	### Scripts.
	@script(description = _("Enables or disables Developer toolkit features."),
		gesture = "kb:alt+windows+k")
	def script_ToggleFeatures(self, gesture):
		if addonHandler.config.conf["developertoolkit"]["isEnabled"]:
			addonHandler.config.conf["developertoolkit"]["isEnabled"] = False
			self.__ToggleGestures()
			ui.message("Developer toolkit disabled.")
		elif not addonHandler.config.conf["developertoolkit"]["isEnabled"]:
			addonHandler.config.conf["developertoolkit"]["isEnabled"] = True
			self.__ToggleGestures()
			ui.message("Developer toolkit enabled.")

	# Helper function: Display detailed report in a virtual window.
	def __displayDetailedReport__(self):
		focus = api.getFocusObject() # The object we are inspecting.
		# Test to see if focused object is a web element.
		if focus.treeInterceptor is None:
			message = self.__formatMessage__('No report is available.', None)
			ui.message(message)
		else:
			attributes = focus.IA2Attributes # The IAccessible2 attributes such as tag, margins...
			objectLocation = self.__getSizeAndPosition__(focus) # The size and location of our focus.
			title = self.__formatMessage__('', focus) # The report's title.
			lines = [] # Lines of text in the report.
			lines += [title]
			if objectLocation is not None:
				lines += ["<table>"]
				lines += ["<thead>"]
				lines += ["<tr><header>Size and location</header></tr>"]
				lines += ["<tr><th>Left</th><th>Top</th><th>Right</th><th>Bottom</th><th>Height</th><th>Width</th></tr>"]
				lines += ["</thead>"]
				lines += ["<tbody>"]
				lines += ["<tr><td>%d</td><td>%d</td><td>%d</td><td>%d</td><td>%d</td><td>%d</td></tr>" % (
					objectLocation['left'], objectLocation['top'], objectLocation['right'], objectLocation['bottom'], objectLocation['height'], objectLocation['width'])]
				lines += ["</tbody>"]
				lines += ["</table>"]
			else:
				lines += ["No object information is available at this time."]
			message = ''.join(lines)
		ui.browseableMessage(message, isHtml = True)

	# Helper function: Speak a summary of the control such as height, width, child count and if there are other siblings.
	def __speakObjectSummary__(self):
		focus = api.getFocusObject()
		# Check to see if the focused object is a web element.
		if focus.treeInterceptor is None:
			summary = self.__formatMessage__('No report is available', None)
			ui.message(summary)
		# Give the report.
		else:
			objectLocation = self.__getSizeAndPosition__(focus)
			childCount = focus.childCount
			# Workaround for obtaining sibling count.
			if focus == focus.treeInterceptor.rootNVDAObject:
				siblingCount = 0
			else:
				siblingCount = focus.parent.childCount - 1
			summary = "Object has %d children and %d more siblings. It is %d pixels wide and %d pixels high." % (
				childCount, siblingCount, objectLocation['width'], objectLocation['height'])
			ui.message(summary)

	# Helper function: Returns a tuple with an object's size and position information.
	def __getSizeAndPosition__(self, object):
		if object is not None and hasattr(object, 'location'):
			return {
				'left':object.location.left,
				'top':object.location.top,
				'right':object.location.right,
				'bottom':object.location.bottom,
				'topLeft':
					{'x':object.location.topLeft.x,
					'y':object.location.topLeft.y,},
				'topRight':
					{'x':object.location.topRight.x,
					'y':object.location.topRight.y,},
				'bottomLeft':
					{'x':object.location.bottomLeft.x,
					'y':object.location.bottomLeft.y,},
				'topRight':
					{'x':object.location.topRight.x,
					'y':object.location.topRight.y,},
				'bottomRight':
					{'x':object.location.bottomRight.x,
					'y':object.location.bottomRight.y,},
				'center':
					{'x':object.location.center.x,
					'y':object.location.center.y,},
				'height':object.location.height,
				'width':object.location.width,
			}
		else:
			return None

	# Helper function: Gets an identifier from an object.
	def __getIdentifier__(self, object):
		if 'id' in object.IA2Attributes:
			identifier =  object.IA2Attributes['id']
		else:
			identifier = object.IA2UniqueID
		return identifier

	# Helper function: Format the messages developer toolkit sends to the user.
	def __formatMessage__(self, prefix, object):
		# Build an error message.
		if object is None:
			message = prefix
		# Check for no tag because it may indicate a compliance problem.
		elif 'tag' not in object.IA2Attributes or object.IA2Attributes is None:
			identifier = self.__getIdentifier__(object) # the object's ID
			message = "%s: This object has no tag (%s)" % (
				prefix,
				str(identifier))
		else:
			identifier = self.__getIdentifier__(object) # the object's ID
			message = "%s: %s (%s)" % (
				prefix,
				object.IA2Attributes['tag'],
				str(identifier))
		return message

	### Scripts...
	@script(description = _("Speaks the focused element's HTML attributes. Press twice quickly to place in a virtual buffer."))
	def script_HtmlAttributes(self, gesture):

		focus = api.getFocusObject()
		attributes = []

		# Make sure we have a Firefox virtual buffer.
		if focus.IA2Attributes and isinstance(focus.treeInterceptor, Gecko_ia2):

			# Split the attributes in key/value pairs.
			for key in focus.IA2Attributes:
				attributes += ["%s: %s" % (key, focus.IA2Attributes[key])]

			# Testing how many times the script runs.
			if getLastScriptRepeatCount() == 0:
				message = "\n".join(attributes)
				ui.message(message)
			elif getLastScriptRepeatCount() == 1:
				message = "\n".join(attributes)
				ui.browseableMessage("<pre>" + message + "</pre>", isHtml = True)

		# We are not in a virtual buffer.
		else:
			ui.message("No HTML attributes found!")


	@script(description = _("Moves focus to the document root."))
	def script_DocumentRoot(self, gesture):
		focus = api.getFocusObject()
		# Make sure focused object is a web element.
		if isinstance(focus.treeInterceptor, Gecko_ia2) and hasattr(focus, 'treeInterceptor'):
			tree = focus.treeInterceptor
		else:
			tree = None
		# Set focus to the root element.
		if tree is not None:
			api.setFocusObject(tree.rootNVDAObject)
			message = self.__formatMessage__('Document root', tree.rootNVDAObject)
			ui.message(message)
		else:
			message = self.__formatMessage__('No document root.', None)
			ui.message(message) 

	# Moves the developer toolkit focus to the parent of the current object.
	@script(
		description = _("Moves focus to the selected element's parent."),
	)
	def script_Parent(self, gesture):
		focus = api.getFocusObject()
		if (focus.parent is not None) and (focus.parent.treeInterceptor is not None):
			api.setFocusObject(focus.parent)
			message = self.__formatMessage__('Parent:', focus.parent)
			ui.message(message)
		else:
			message = self.__formatMessage__('No parent!', None)
			ui.message(message)

	# Move to next sibling in the tree.
	@script(
		description = _("Moves focus to the next sibling."),
	)
	def script_NextSibling(self, gesture):
		focus = api.getFocusObject()
		if (focus.next is not None) and (focus.treeInterceptor is not None):
			api.setFocusObject(focus.next)
			message = self.__formatMessage__('Next sibling:', focus.next)
			ui.message(message)
		else:
			message = self.__formatMessage__('No next sibling!', None)
			ui.message(message)

	# Set developer toolkit focus to the previous sibling.
	@script(
		description = _("Moves focus to the previous sibling."),
	)
	def script_PreviousSibling(self, gesture):
		focus = api.getFocusObject()
		if (focus.previous is not None) and (focus.treeInterceptor is not None):
			api.setFocusObject(focus.previous)
			message = self.__formatMessage__('Previous sibling:', focus.previous)
			ui.message(message)
		else:
			message = self.__formatMessage__('No previous sibling!', None)
			ui.message(message)

	# Set developer toolkit to the first child of an element.
	@script(
		description = _("Moves focus to the selected element's first child."),
	)
	def script_FirstChild(self, gesture):
		focus = api.getFocusObject()
		if focus.firstChild is not None and focus.treeInterceptor is not None:
			api.setFocusObject(focus.firstChild)
			message = self.__formatMessage__('First child:', focus.firstChild)
			ui.message(message)
		else:
			message = self.__formatMessage__('No children!', None)
			ui.message(message)


	@script(
		description = _("Moves focus to the selected element's last child."),
	)
	def script_LastChild(self, gesture):
		focus = api.getFocusObject()
		if focus.firstChild is not None and focus.treeInterceptor is not None:
			api.setFocusObject(focus.lastChild)
			message = self.__formatMessage__('Last child:', focus.lastChild)
			ui.message(message)
		else:
			message = self.__formatMessage__('No children!', None)
			ui.message(message)

	# Speak the object summary or display its details
	@script(
		description = _('Speak an object\'s summary. Press twice quickly to display its details.'),
		category = "Developer toolkit",
		gestures = ["kb:control+windows+numpad5",
			"kb(laptop):control+windows+k"])
	def script_reportObjectDetails(self, gesture):
		self.summaryModeGesture = gesture
		if getLastScriptRepeatCount() is 0:
			self.__speakObjectSummary__()
		else:
			self.__displayDetailedReport__()

	### Events
	def event_gainFocus(self,object,nextHandler):
		self.__ToggleGestures()
		nextHandler()

	### Gestures dictionary.
	__gestures__ = {
		"kb:leftArrow": "PreviousSibling",
		"kb:rightArrow": "NextSibling",
		"kb:upArrow": "Parent",
		"kb:downArrow": "FirstChild",
		"kb:end": "LastChild",
		"kb:control+home": "DocumentRoot",
		"kb:a": "HtmlAttributes",
	}

	### Internal functions.
	def __ToggleGestures(self):
		if addonHandler.config.conf["developertoolkit"]["isEnabled"]:
			self.bindGestures(self.__gestures__)
		elif not addonHandler.config.conf["developertoolkit"]["isEnabled"]:
			self.clearGestureBindings()
			self.bindGesture("kb:alt+windows+k", "ToggleFeatures")
