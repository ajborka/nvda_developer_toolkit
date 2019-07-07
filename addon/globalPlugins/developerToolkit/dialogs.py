import wx
import gui
from gui import guiHelper
import ui
import config

### Dialogs
class DtkSettingsPanel(gui.SettingsPanel):
	title = _('Developer toolkit')
	def makeSettings(self, settingsSizer):
		self.isEnabled = config.conf["developertoolkit"]["isEnabled"]
		self.isElementLoggingEnabled = config.conf["developertoolkit"]["isElementLoggingEnabled"]
		sHelper = gui.guiHelper.BoxSizerHelper(self, sizer = settingsSizer)
		# Enable or disable the addon.
		self.isEnabledToggleButton = sHelper.addItem(wx.ToggleButton(self, label = _('Enable Developer toolkit features')))
		self.isEnabledToggleButton.SetValue(self.isEnabled)
		self.isElementLoggingEnabledToggleButton = sHelper.addItem(wx.ToggleButton(self, label = _("Enable element logging")))
		self.isElementLoggingEnabledToggleButton.SetValue(self.isElementLoggingEnabled)

	def onSave(self):
		config.conf["developertoolkit"]["isEnabled"] = self.isEnabledToggleButton.GetValue()
		config.conf["developertoolkit"]["isElementLoggingEnabled"] = self.isElementLoggingEnabledToggleButton.GetValue()
		
