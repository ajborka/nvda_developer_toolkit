#from __future__ import unicode_literals
import wx
from wx.adv import EditableListBox
import gui
from gui import guiHelper
import ui
import config

### Dialogs
class DtkSettingsPanel(gui.SettingsPanel):
	title = u"Developer toolkit"
	def makeSettings(self, settingsSizer):
		self.isEnabled = config.conf["developertoolkit"]["isEnabled"]
		self.isDetailedMessages = config.conf["developertoolkit"]["isDetailedMessages"]
		sHelper = gui.guiHelper.BoxSizerHelper(self, sizer = settingsSizer)
		self.formattingAttributes = sHelper.addItem(wx.adv.EditableListBox(self, wx.ID_ANY, u"Included formatting attributes:", style = wx.adv.EL_DEFAULT_STYLE|wx.adv.EL_ALLOW_NEW|wx.adv.EL_ALLOW_EDIT|wx.adv.EL_ALLOW_DELETE))
		self.formattingAttributes.GetNewButton().SetLabel(u"New attribute")
		self.formattingAttributes.GetDelButton().SetLabel(u"Delete attribute")
		self.formattingAttributes.GetEditButton().SetLabel(u"Rename attribute")
		self.formattingAttributes.GetUpButton().SetLabel(u"Move up")
		self.formattingAttributes.GetDownButton().SetLabel(u"Move down")
		self.formattingAttributes.SetStrings(config.conf["developertoolkit"]["fontInfo"])
		self.colorDisplay = sHelper.addLabeledControl(u"Color display format:", wx.Choice, choices = ['RGB', 'Hex', 'Name'])
		self.colorDisplay.SetSelection(config.conf["developertoolkit"]["displayColorFormat"])
		# Enable or disable the addon.
		self.isEnabledToggleButton = sHelper.addItem(wx.ToggleButton(self, label = u"Enable Developer toolkit features"))
		self.isEnabledToggleButton.SetValue(self.isEnabled)
		self.isDetailedMessagesToggleButton = sHelper.addItem(wx.ToggleButton(self, label = u"Messages are detailed."))
		self.isDetailedMessagesToggleButton.SetValue(self.isDetailedMessages)

	def onSave(self):
		config.conf["developertoolkit"]["isEnabled"] = self.isEnabledToggleButton.GetValue()
		config.conf["developertoolkit"]["isDetailedMessages"] = self.isDetailedMessagesToggleButton.GetValue()
		config.conf["developertoolkit"]["fontInfo"] = self.formattingAttributes.GetStrings()
		config.conf["developertoolkit"]["displayColorFormat"] = self.colorDisplay.GetSelection()
