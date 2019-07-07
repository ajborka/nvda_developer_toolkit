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
		self.isDetailedMessages = config.conf["developertoolkit"]["isDetailedMessages"]
		sHelper = gui.guiHelper.BoxSizerHelper(self, sizer = settingsSizer)
		# Enable or disable the addon.
		self.isEnabledToggleButton = sHelper.addItem(wx.ToggleButton(self, label = _('Enable Developer toolkit features')))
		self.isEnabledToggleButton.SetValue(self.isEnabled)
		self.isDetailedMessagesToggleButton = sHelper.addItem(wx.ToggleButton(self, label = _("Messages are detailed.")))
		self.isDetailedMessagesToggleButton.SetValue(self.isDetailedMessages)

	def onSave(self):
		config.conf["developertoolkit"]["isEnabled"] = self.isEnabledToggleButton.GetValue()
		config.conf["developertoolkit"]["isDetailedMessages"] = self.isDetailedMessagesToggleButton.GetValue()
		
