# dtkFirefox.py
# Web developer tools NVDA addon that helps blind/visually impaired developers create
# visually appealing user interfaces without sighted help.
# Firefox module. See others as they become available.
# Copyright 2019 Andy Borka. Licensed under GPL2.

import addonHandler
import api
import appModuleHandler
import config
from scriptHandler import getLastScriptRepeatCount
from scriptHandler import script
import ui
from virtualBuffers.gecko_ia2 import Gecko_ia2

class AppModule(appModuleHandler.AppModule):

	scriptCategory = _("Developer toolkit")

	### Scripts.
	@script(description = _("Enables or disables Developer toolkit features."))
	def script_ToggleFeatures(self, gesture):
		if addonHandler.config.conf["developertoolkit"]["isEnabled"]:
			addonHandler.config.conf["developertoolkit"]["isEnabled"] = False
			self.__ToggleGestures()
			ui.message("Developer toolkit disabled.")
		elif not addonHandler.config.conf["developertoolkit"]["isEnabled"]:
			addonHandler.config.conf["developertoolkit"]["isEnabled"] = True
			self.__ToggleGestures()
			ui.message("Developer toolkit enabled.")

	@script(description = _("Speaks the focused element's HTML attributes. Press twice quickly to place in a virtual buffer."))
	def script_HtmlAttributes(self, gesture):
		attributes = []
		focus = api.getFocusObject()
		# Make sure we have a Firefox virtual buffer.
		if focus.IA2Attributes and self.__isWebElement(focus):

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
	__developerToolkitGestures = {
		"kb:alt+windows+k": "ToggleFeatures",
		"kb:leftArrow": "PreviousSibling",
		"kb:rightArrow": "NextSibling",
		"kb:upArrow": "Parent",
		"kb:downArrow": "FirstChild",
		"kb:end": "LastChild",
		"kb:control+home": "DocumentRoot",
		"kb:a": "HtmlAttributes",
	}

	### Internal functions.

	def __isWebElement(self, object):

		if isinstance(object.treeInterceptor, Gecko_ia2):
			return True
		else:
			return False

	def __ToggleGestures(self):

		# Developer toolkit is enabled, bind gestures.
		if addonHandler.config.conf["developertoolkit"]["isEnabled"]:
			for key in self.__developerToolkitGestures:
				self.bindGesture(key, self.__developerToolkitGestures[key])

		# Developer toolkit is disabled, remove gestures.
		elif not addonHandler.config.conf["developertoolkit"]["isEnabled"]:
			for key in self.__developerToolkitGestures:
				try:
					self.removeGestureBinding(key)
				except KeyError:
					pass

			# Rebind features toggle because it was removed.
			self.bindGesture("kb:alt+windows+k", "ToggleFeatures")

	def __getSizeAndPosition(self, object):
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
