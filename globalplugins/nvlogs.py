# -*- coding: utf-8 -*-
import globalPluginHandler
import scriptHandler
import addonHandler
import ui
import wx
import gui
import logHandler

addonHandler.initTranslation()

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	def __init__(self):
		super().__init__()

	@scriptHandler.script(description=_("Show NVDA Log"), category=_("NVLogs"))
	def script_showLogs(self, gesture):
		wx.CallAfter(self.displayLog)

	def displayLog(self):
		log_content = logHandler.log.getLog()
		if not log_content:
			ui.message(_("Log is empty."))
			return
		dlg = wx.Dialog(gui.mainFrame, title=_("NVDA Log Viewer v5.0 - Volkan Ozdemir Software Services"), size=(600, 450), style=wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER)
		panel = wx.Panel(dlg)
		sizer = wx.BoxSizer(wx.VERTICAL)
		text_ctrl = wx.TextCtrl(panel, value=log_content, style=wx.TE_MULTILINE | wx.TE_READONLY)
		sizer.Add(text_ctrl, 1, wx.EXPAND | wx.ALL, 10)
		btn_sizer = wx.BoxSizer(wx.HORIZONTAL)
		close_btn = wx.Button(panel, wx.ID_CANCEL, label=_("Close"))
		close_btn.Bind(wx.EVT_BUTTON, lambda e: dlg.Destroy())
		btn_sizer.Add(close_btn, 0, wx.ALL, 5)
		sizer.Add(btn_sizer, 0, wx.ALIGN_RIGHT | wx.ALL, 10)
		panel.SetSizer(sizer)
		dlg.CenterOnScreen()
		dlg.ShowModal()
		dlg.Destroy()