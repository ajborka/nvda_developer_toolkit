# Developer toolkit: Helps blind and visually impaired developers create appealing user interfaces.
# __init__.py: global plugin startup code.
# Copyright 2019 Andy Borka. Licensed under GPL2.

import addonHandler
import globalPluginHandler
import config
import gui
from gui import guiHelper
import wx
import ui
from . import dialogs
from scriptHandler import script
import appModuleHandler


confspeck = {
	"isEnabled": "boolean(default = True)",
	"isElementLoggingEnabled": "boolean(default = False)",
}
config.conf.spec["developertoolkit"] = confspeck


### global plugin
class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	def __init__(self):
		super(GlobalPlugin, self).__init__()
		self.menu = gui.mainFrame.sysTrayIcon.preferencesMenu
		self.addonMenu = self.menu.Append(wx.ID_ANY,
			# Text displayed on addon main menu.
			_("&Developer toolkit"),
			# Tooltip for menu item.
			_("Developer toolkit settings"))
		gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.onAddonMenu, self.addonMenu)

	def onAddonMenu(self, evt):
		gui.mainFrame.prePopup()
		d = dialogs.AddonSettingsDialog(gui.mainFrame)
		d.Show()
		gui.mainFrame.postPopup()

