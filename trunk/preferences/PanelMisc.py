#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# generated by wxGlade 0.4.1 on Thu Mar 22 10:28:57 2007

import wx
import globals
import os

class PanelMisc(wx.ScrolledWindow):
    def __init__(self, *args, **kwds):
        # begin wxGlade: PanelMisc.__init__
        kwds["style"] = wx.TAB_TRAVERSAL
        wx.ScrolledWindow.__init__(self, *args, **kwds)
        self.sizer_5_staticbox = wx.StaticBox(self, -1, _("Shell Context Menu (Only Windows):"))
        self.sizer_4_staticbox = wx.StaticBox(self, -1, _("Players paths:"))
        self.mplayerLabel = wx.StaticText(self, -1, _("Mplayer:"), style=wx.ALIGN_CENTRE)
        self.mplayerPath = wx.TextCtrl(self, -1, "")
        self.button_browser_mplayer = wx.Button(self, -1, _("Browse"))
        self.vlc_label = wx.StaticText(self, -1, _("VLC:      "), style=wx.ALIGN_CENTRE)
        self.vlcPath = wx.TextCtrl(self, -1, "")
        self.button_browser_vlc = wx.Button(self, -1, _("Browse"))
        self.button_install_shellmenu = wx.Button(self, -1, _("Install"))
        self.button_uninstall_shellmenu = wx.Button(self, -1, _("Uninstall"))

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: PanelMisc.__set_properties
        self.SetToolTipString(_("Specify Player Paths"))
        self.SetScrollRate(10, 10)
        self.vlcPath.SetSize((170, 26))
        # end wxGlade

    def __do_layout(self):
        self.Bind(wx.EVT_BUTTON,self.OnButtonBrowseMplayer,self.button_browser_mplayer)
        self.Bind(wx.EVT_BUTTON,self.OnButtonBrowseVLC,self.button_browser_vlc)
        self.Bind(wx.EVT_BUTTON,self.OnButtonInstallShell,self.button_install_shellmenu)
        self.Bind(wx.EVT_BUTTON,self.OnButtonUninstallShell,self.button_uninstall_shellmenu)
        # begin wxGlade: PanelMisc.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_5 = wx.StaticBoxSizer(self.sizer_5_staticbox, wx.HORIZONTAL)
        sizer_4 = wx.StaticBoxSizer(self.sizer_4_staticbox, wx.VERTICAL)
        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_2.Add(self.mplayerLabel, 0, wx.EXPAND|wx.ADJUST_MINSIZE, 0)
        sizer_2.Add(self.mplayerPath, 1, wx.EXPAND|wx.ADJUST_MINSIZE, 0)
        sizer_2.Add(self.button_browser_mplayer, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ADJUST_MINSIZE, 0)
        sizer_4.Add(sizer_2, 0, wx.EXPAND, 0)
        sizer_4.Add((20, 20), 0, wx.EXPAND|wx.ADJUST_MINSIZE, 0)
        sizer_3.Add(self.vlc_label, 0, wx.EXPAND|wx.ADJUST_MINSIZE, 0)
        sizer_3.Add(self.vlcPath, 1, wx.EXPAND|wx.ADJUST_MINSIZE, 0)
        sizer_3.Add(self.button_browser_vlc, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ADJUST_MINSIZE, 0)
        sizer_4.Add(sizer_3, 0, wx.EXPAND, 0)
        sizer_1.Add(sizer_4, 0, wx.EXPAND, 0)
        sizer_5.Add(self.button_install_shellmenu, 0, wx.ADJUST_MINSIZE, 0)
        sizer_5.Add((20, 0), 0, wx.ADJUST_MINSIZE, 0)
        sizer_5.Add(self.button_uninstall_shellmenu, 0, wx.ADJUST_MINSIZE, 0)
        sizer_1.Add(sizer_5, 0, wx.EXPAND, 0)
        self.SetAutoLayout(True)
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        sizer_1.SetSizeHints(self)
        # end wxGlade

    def OnButtonBrowseMplayer(self,evt):
        dlg = wx.FileDialog(
            self, message=_("Browse..."), defaultDir=globals.sourcefolder, 
            defaultFile="mplayer.exe", wildcard="ALL programs (*.exe)|*.exe", style=wx.OPEN |wx.CHANGE_DIR)
	
        if dlg.ShowModal() == wx.ID_OK:
	     self.mplayerPath.SetValue(dlg.GetPath())
	
	dlg.Destroy()
	     
    def OnButtonBrowseVLC(self,evt):
	dlg = wx.FileDialog(
            self, message=_("Browse..."), defaultDir=globals.sourcefolder, 
            defaultFile="vlc.exe", wildcard="ALL programs (*.exe)|*.exe", style=wx.OPEN |wx.CHANGE_DIR)
	
        if dlg.ShowModal() == wx.ID_OK:
	     self.vlcPath.SetValue(dlg.GetPath())
	
	dlg.Destroy()
    def OnButtonInstallShell(self,evt):
	if wx.Platform == '__WXMSW__':
	   executable = os.path.join(globals.sourcefolder,"install_shell.exe")
	   os.spawnve(os.P_NOWAIT, executable,['install_shell.exe'], os.environ)
    def OnButtonUninstallShell(self,evt):
	if wx.Platform == '__WXMSW__':
	   executable = os.path.join(globals.sourcefolder,"uninstall_shell.exe")
	   os.spawnve(os.P_NOWAIT, executable,['uninstall_shell.exe'], os.environ)
	    
# end of class PanelMisc

