#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# generated by wxGlade 0.4cvs on Tue Aug 29 03:50:20 2006

import wx
import os,globals
import wx.lib.hyperlink as hl

class PanelLogin(wx.Panel):
    def __init__(self, *args, **kwds):
        # begin wxGlade: PanelLogin.__init__
        kwds["style"] = wx.TAB_TRAVERSAL
        wx.Panel.__init__(self, *args, **kwds)
        self.sizer_1_staticbox = wx.StaticBox(self, -1, _("Login:"))
        self.label_1_copy = wx.StaticText(self, -1, _("If you don't have a user account, please"))
        self.link_already = hl.HyperLinkCtrl(self, -1, _("Register for free"), URL="http://www.opensubtitles.org/newuser")
        self.static_line_1 = wx.StaticLine(self, -1)
        self.label_1 = wx.StaticText(self, -1, _("Username:"))
        self.text_username = wx.TextCtrl(self, -1, "")
        self.label_2 = wx.StaticText(self, -1, _("Password:"))
        self.text_password = wx.TextCtrl(self, -1, "", style=wx.TE_PASSWORD)
        self.button_login = wx.Button(self, -1, _("Login"))

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: PanelLogin.__set_properties
        self.link_already.SetMinSize((83, 23))
        self.text_username.SetMinSize((100, 27))
        self.text_password.SetMinSize((100, 27))
        # end wxGlade

    def __do_layout(self):
        self.Bind(wx.EVT_BUTTON,self.OnButtonLogin,self.button_login)
        # begin wxGlade: PanelLogin.__do_layout
        sizer_1 = wx.StaticBoxSizer(self.sizer_1_staticbox, wx.VERTICAL)
        grid_sizer_1 = wx.FlexGridSizer(3, 2, 5, 5)
        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        sizer_2.Add(self.label_1_copy, 0, wx.EXPAND|wx.ADJUST_MINSIZE, 0)
        sizer_2.Add(self.link_already, 0, wx.EXPAND, 0)
        sizer_1.Add(sizer_2, 0, wx.EXPAND, 0)
        sizer_1.Add(self.static_line_1, 0, wx.BOTTOM|wx.EXPAND, 30)
        grid_sizer_1.Add(self.label_1, 0, wx.ADJUST_MINSIZE, 0)
        grid_sizer_1.Add(self.text_username, 0, wx.ADJUST_MINSIZE, 0)
        grid_sizer_1.Add(self.label_2, 0, wx.ADJUST_MINSIZE, 0)
        grid_sizer_1.Add(self.text_password, 0, wx.ADJUST_MINSIZE, 0)
        sizer_1.Add(grid_sizer_1, 0, wx.LEFT|wx.EXPAND, 0)
        sizer_1.Add(self.button_login, 0, wx.TOP|wx.ADJUST_MINSIZE, 4)
        self.SetAutoLayout(True)
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        sizer_1.SetSizeHints(self)
        # end wxGlade
    def OnButtonLogin(self,evt):
        globals.preferences_list["username"] = self.text_username.GetValue()
        globals.preferences_list["password"] = self.text_password.GetValue()
        ok,msg = globals.connection.Login(usecookie = False)
	if not ok:
	    wx.MessageBox(msg)
	    globals.Log(msg)
	else:
	    globals.Log(msg)
	    
        version = "SubDownloader " +globals.version
	if globals.disable_osdb:
		message = version + " : "+ _("Not Connected")
	elif globals.logged_as:
		message = version +" : "+ _("Connected as %s") % globals.logged_as
	else:
		message = version +" : "+ _("Connected anonymously")
	globals.subdownloaderframe.SetTitle(message)

# end of class PanelLogin


