#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# generated by wxGlade 0.4.1 on Wed Feb 21 01:02:39 2007

import wx
from preferences import PanelServers
from preferences import PanelPrefLangs
from preferences import PanelLogin
from preferences import PanelDirectories
from preferences import PanelMisc

import globals,os
import pickle,time
from xmlrpclib import Transport,Server
from extra.PyProgress import PyProgress as PP

class PanelOptions(wx.Panel):
    def __init__(self, *args, **kwds):
        # begin wxGlade: PanelOptions.__init__
        kwds["style"] = wx.TAB_TRAVERSAL
        wx.Panel.__init__(self, *args, **kwds)
        self.notebook = wx.Notebook(self, -1, style=wx.BK_DEFAULT)
        self.static_line_1 = wx.StaticLine(self, -1)
        self.button_ok = wx.Button(self, -1, _("Apply Changes"))
        self.button_cancel = wx.Button(self, -1, _("Cancel Changes"))

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: PanelOptions.__set_properties
        pass
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: PanelOptions.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_1.Add(self.notebook, 1, wx.EXPAND, 0)
        sizer_1.Add(self.static_line_1, 0, wx.EXPAND, 0)
        sizer_3.Add(self.button_ok, 0, wx.RIGHT|wx.ADJUST_MINSIZE, 4)
        sizer_3.Add(self.button_cancel, 0, wx.ADJUST_MINSIZE, 0)
        sizer_1.Add(sizer_3, 0, wx.ALIGN_RIGHT, 0)
        self.SetAutoLayout(True)
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        sizer_1.SetSizeHints(self)
        # end wxGlade
        self.InitializeComponents()
        
    def InitializeComponents(self):
        
        self.Bind(wx.EVT_BUTTON, self.OnButtonCancel, self.button_cancel)
        self.Bind(wx.EVT_BUTTON, self.OnButtonOK, self.button_ok)
        
        self.LoadPreferences()
	self.notebook.DeleteAllPages()
	self.notebook.AddPage(self.panel_login,_("Login"))
	self.notebook.AddPage(self.panel_server,_("Servers"))
	self.notebook.AddPage(self.panel_language,_("Language"))
	self.notebook.AddPage(self.panel_directories,_("Directories"))
	self.notebook.AddPage(self.panel_misc,_("Misc"))
	self.notebook.Refresh()
	self.notebook.Show()
	
	
        
    def LoadPreferences(self):
	globals.doing_login = False
        self.preferences_list =  globals.preferences_list

        self.panel_server = PanelServers.PanelServers(self.notebook, -1)
        #self.panel_server.Show()
        if self.preferences_list.has_key("server_osdb"):
            self.panel_server.combo_osdb_server.SetValue(self.preferences_list["server_osdb"])
	if self.preferences_list.has_key("proxyuser"):
            self.panel_server.text_proxyuser.SetValue(self.preferences_list["proxyuser"])
	if self.preferences_list.has_key("proxypass"):
            self.panel_server.text_proxypass.SetValue(self.preferences_list["proxypass"])
	if self.preferences_list.has_key("proxyserver"):
            self.panel_server.text_proxyserver.SetValue(self.preferences_list["proxyserver"])
	if self.preferences_list.has_key("proxyport"):
            self.panel_server.text_proxyport.SetValue(self.preferences_list["proxyport"])
            
            
	self.panel_language = PanelPrefLangs.PanelPrefLangs(self.notebook, -1)
        #self.panel_language.Hide()
	if self.preferences_list.has_key("app_language"):
	    lang_str = globals.sublanguages["languages_id_xxx"][globals.sublanguages["languages_xx2xxx"][globals.preferences_list["app_language"]]][1]
	    
	    self.panel_language.choice_app.SetStringSelection(lang_str)
	    
        if self.preferences_list.has_key("upload_language"):
	    lang_str = globals.sublanguages["languages_id_xxx"][globals.sublanguages["languages_xx2xxx"][globals.preferences_list["upload_language"]]][1]
	    self.panel_language.choice_upload.SetStringSelection(lang_str)
	    
	if self.preferences_list.has_key("language_upload_autodetect"):
	    self.panel_language.checkbox_autodetect_upload.SetValue(self.preferences_list["language_upload_autodetect"])
	    self.panel_language.OnCheckAutodetectUploadLang(wx.EVT_CHECKBOX)
	    
        if self.preferences_list.has_key("search_langs"):
	    if self.preferences_list["search_langs"] == "all":
		self.panel_language.checkbox_search_all_langs.SetValue(True)
		self.panel_language.scrolled_panel.Disable()
	    else:
		self.panel_language.checkbox_search_all_langs.SetValue(False)
		if self.preferences_list["search_langs"]:
		    for lang in self.preferences_list["search_langs"].split(","):
			self.panel_language.langs_checkboxes[lang].SetValue(True)
		self.panel_language.scrolled_panel.Enable()
		
		    
		
	    
        self.panel_login = PanelLogin.PanelLogin(self.notebook, -1)
        #self.panel_login.Hide()
        
        if self.preferences_list.has_key("username"):
            self.panel_login.text_username.SetValue(self.preferences_list["username"])
        if self.preferences_list.has_key("password"):
            self.panel_login.text_password.SetValue(self.preferences_list["password"])
	    
	self.panel_directories = PanelDirectories.PanelDirectories(self.notebook, -1)
        self.panel_directories.Hide()
        
        if self.preferences_list.has_key("download_radio1"):
            self.panel_directories.radio_btn_samedir.SetValue(self.preferences_list["download_radio1"])
	    self.panel_directories.radio_btn_folder.SetValue(not self.preferences_list["download_radio1"])
	if self.preferences_list.has_key("download_folder"):
            self.panel_directories.text_folder.SetValue(self.preferences_list["download_folder"])
	    
	self.panel_misc = PanelMisc.PanelMisc(self.notebook, -1)
        #self.panel_misc.Hide()
	if self.preferences_list.has_key("mplayer"):
            self.panel_misc.mplayerPath.SetValue(self.preferences_list["mplayer"])
	if self.preferences_list.has_key("vlc"):
            self.panel_misc.vlcPath.SetValue(self.preferences_list["vlc"])
                
                
    def OnButtonOK(self,evt):
        wx.BusyInfo("Saving Preferences,please wait...")
	do_login = False
        
	if self.panel_login.text_username.GetValue() != self.preferences_list["username"] \
	    or self.panel_login.text_password.GetValue() != self.preferences_list["password"] \
	    or self.panel_server.combo_osdb_server.GetValue() != self.preferences_list["server_osdb"] \
	    or self.panel_server.text_proxyuser.GetValue() != self.preferences_list["proxyuser"] \
	    or self.panel_server.text_proxypass.GetValue() != self.preferences_list["proxypass"] \
	    or self.panel_server.text_proxyserver.GetValue() != self.preferences_list["proxyserver"] \
	    or self.panel_server.text_proxyport.GetValue() != self.preferences_list["proxyport"]:
	    do_login = True
	   
            
        
	self.preferences_list = globals.preferences_list.copy()
	self.preferences_list["cwd"] = globals.preferences_list["cwd"]
	self.preferences_list["username"] = self.panel_login.text_username.GetValue()
	self.preferences_list["password"] = self.panel_login.text_password.GetValue()
	
	lang_str = lang_str = globals.sublanguages["languages_id_xxx"][globals.sublanguages["languages_xx2xxx"][globals.preferences_list["app_language"]]][1]
	if self.panel_language.choice_app.GetStringSelection() != lang_str:
	    lang_str = self.panel_language.choice_app.GetStringSelection()
	    lang_app_xxx = globals.sublanguages["languages_name2xxx"][lang_str] 
	    lang_app_xx = globals.sublanguages["languages_id_xxx"][lang_app_xxx][0]
		
	    self.download_lang = PP.PyProgress(None, -1, _("Downloading Language"),
                            _("Downloading %s language, it can take a while...") % lang_str,
                            style = wx.PD_CAN_ABORT)
	    
	    self.download_lang.CenterOnParent()
	    globals.Log("-----XMLRPC GetAvailableTranslations----\n")
	    self.download_lang.UpdatePulse()
	    try:
		list_translations = globals.xmlrpc_server.GetAvailableTranslations(globals.osdb_token)["data"]
		globals.Log(list_translations)
		self.download_lang.UpdatePulse()
		globals.new_translations_dates = {}
		for lang,array in list_translations.items():
			globals.new_translations_dates[lang] =  time.mktime(time.strptime(array["LastCreated"],"%Y-%m-%d %H:%M:%S"))
		
		self.download_lang.UpdatePulse()
		if globals.new_translations_dates.has_key(lang_app_xx):
		    result = True
		    if not globals.current_translations_dates.has_key(lang_app_xx):
				    result = globals.DownloadNewTranslations(lang_app_xx)
		    elif globals.current_translations_dates[lang_app_xx] < globals.new_translations_dates[lang_app_xx]:
				    result = globals.DownloadNewTranslations(lang_app_xx) 
		    
		    if result:
			wx.MessageBox(_("The new language will be displayed after restarting the program."))
		    else:
			error = _("Error retrieving new language from server.")
			wx.MessageBox(error)
			globals.Log(error)
		else:
		    wx.MessageBox(_("No translation available in %s. Please contact %s to help us.") % (lang_str,"admins@opensubtitles.org"))
	    except:
		pass
	    
		
	    self.download_lang.UpdatePulse()
	    self.download_lang.Destroy()

	if self.panel_language.checkbox_search_all_langs.IsChecked():
	    self.preferences_list["search_langs"] = "all"
	else:
	    langs = []
	    for xx,checkbox in self.panel_language.langs_checkboxes.items():
		if checkbox.IsChecked():
		    langs.append(xx)
	    self.preferences_list["search_langs"] = ",".join(langs)
	
	self.preferences_list["language_upload_autodetect"] = self.panel_language.checkbox_autodetect_upload.GetValue()
	
	lang_str = self.panel_language.choice_upload.GetStringSelection()
	lang_upload_xxx = globals.sublanguages["languages_name2xxx"][lang_str] 
	lang_upload_xx = globals.sublanguages["languages_id_xxx"][lang_upload_xxx][0]
	self.preferences_list["upload_language"] = lang_upload_xx
	
	lang_str = self.panel_language.choice_app.GetStringSelection()
	lang_app_xxx = globals.sublanguages["languages_name2xxx"][lang_str] 
	lang_app_xx = globals.sublanguages["languages_id_xxx"][lang_app_xxx][0]
	self.preferences_list["app_language"] = lang_app_xx
            
        

	self.preferences_list["server_osdb"] = self.panel_server.combo_osdb_server.GetValue()
	
	self.preferences_list["mplayer"] = self.panel_misc.mplayerPath.GetValue()
	self.preferences_list["vlc"] = self.panel_misc.vlcPath.GetValue()            
	
	self.preferences_list["proxyuser"] = self.panel_server.text_proxyuser.GetValue()
	self.preferences_list["proxypass"] = self.panel_server.text_proxypass.GetValue()
	self.preferences_list["proxyserver"] = self.panel_server.text_proxyserver.GetValue()
	self.preferences_list["proxyport"] = self.panel_server.text_proxyport.GetValue()
	
	self.preferences_list["download_radio1"] = self.panel_directories.radio_btn_samedir.GetValue()
	self.preferences_list["download_folder"] = self.panel_directories.text_folder.GetValue()
            
        globals.preferences_list = self.preferences_list
	
		
	try:
            pickle.dump(self.preferences_list,file(os.path.join(globals.sourcefolder,globals.preferences_filename),"wb"))
        except:
            wx.MessageBox(_("Error trying to save preferences in '%s'") % os.path.join(globals.sourcefolder,globals.preferences_filename),"Error")
	
        
    def OnButtonCancel(self,evt):
	#self.panel_directories.Destroy()
	#self.panel_language.Destroy()
	#self.panel_login.Destroy()
	#self.panel_server.Destroy()
	selection = self.notebook.GetSelection()
        self.InitializeComponents()
	self.notebook.SetSelection(selection)
# end of class PanelOptions


