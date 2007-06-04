#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# generated by wxGlade 0.4cvs on Sat Jun 24 19:43:45 2006
#Copyright (C) IVAN GARCIA capiscuas@gmail.com

#This program is free software; you can redistribute it and/or
#modify it under the terms of the GNU General Public License
#as published by the Free Software Foundation; either version 2
#of the License, or (at your option) any later version.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with this program; if not, write to the Free Software
#Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

import wx
import SubDownloaderFrame
import globals,sys
import os
from extra.AdvancedSplash import AdvancedSplash as AS
from extra.PyProgress import PyProgress as PP
import pickle,time
from Connection import Connection

#from traceback import format_tb
import __builtin__,gettext,locale


class MainApp(wx.App):
    
    def LoadPreferences(self):
	#LOAD PREFERENCES FILE
		try:
			globals.preferences_list =  pickle.load(file(os.path.join(globals.sourcefolder,globals.preferences_filename),"rb"))		
		except:
			a = 4 #nothing
			#Default preferences
		
		try:
			globals.sublanguages =  pickle.load(file(os.path.join(globals.sourcefolder,"conf/.sublanguages"),"rb"))		
		except:
			globals.sublanguages = {}
			globals.sublanguages["total_subtitles_languages"] = 0
			self.SetDefaultSubLanguages()
			
		try:
			globals.current_translations_dates =  pickle.load(file(os.path.join(globals.sourcefolder,"conf/.translations"),"rb"))		
		except:
			globals.current_translations_dates = {}
			
		
		
		self.GetLocaleLanguage()
		
        #Setting all the initial configuration with their default values if not value loaded from the pickle load
		self.DefaultValue("upload_language",globals.language_system_id)
		if len(globals.preferences_list["upload_language"]) != 2:
		    globals.preferences_list["upload_language"] = globals.language_system_id
		    
		self.DefaultValue("language_upload_autodetect",True)
		
		self.DefaultValue("app_language",globals.language_system_id)
		if len(globals.preferences_list["app_language"]) != 2:
		    globals.preferences_list["app_language"] = globals.language_system_id
		    
		self.DefaultValue("search_langs","all")
				
			
		self.DefaultValue("show_tips",True)
		
		self.DefaultValue("server_osdb","http://www.opensubtitles.org/xml-rpc")
		self.DefaultValue("username","")
		self.DefaultValue("password","")
		self.DefaultValue("proxyuser","")
		self.DefaultValue("proxypass","")
		self.DefaultValue("proxyserver","")
		self.DefaultValue("proxyport","")
		self.DefaultValue("cwd",os.getcwd())
		vlc_default_path = os.path.join(os.getenv("ProgramFiles",""),"VideLan","VLC","vlc.exe")
		mplayer_default_path = os.path.join(os.getenv("ProgramFiles",""),"Mplayer","mplayer.exe")
		self.DefaultValue("vlc",vlc_default_path)
		self.DefaultValue("mplayer",mplayer_default_path)
		self.DefaultValue("download_radio1",True)
		self.DefaultValue("no_show_update_version",globals.version)

			
		if not globals.preferences_list.has_key("no_show_update_version"):
				globals.preferences_list["no_show_update_version"] = globals.version

		self.DefaultValue("imdb_list",[])
		img = wx.Bitmap(os.path.join(globals.sourcefolder,"images/splash.png"), wx.BITMAP_TYPE_PNG)
		globals.splash = wx.SplashScreen(img, wx.SPLASH_CENTRE_ON_SCREEN|wx.SPLASH_NO_TIMEOUT,0, None, -1)
		self.SetupAppLang()
		connection = Connection()
		globals.connection = connection
		globals.connection.Create()
		ok,msg = globals.connection.Login()
		
		if not ok:
		    wx.MessageBox(msg)
		    globals.Log(msg)
		else:
		    globals.Log(msg)
		    self.GetAvailableTranslations()
		    if os.path.exists(os.path.join(globals.sourcefolder,"conf","first_run")):
			os.remove(os.path.join(globals.sourcefolder,"conf","first_run"))
			self.ChooseInitialLanguage()
		
	
		
    def GetLocaleLanguage(self):
	#GETTING LOCALE PARAMETER
	l= locale.getdefaultlocale()[0]
	globals.language_system_id = "en"
	if l:
	    l = l.split ( '_' ) # i [get fr,FR]
	    if len(l):
		xx_id = l[0]
		globals.language_system_id_xx = xx_id
		if globals.sublanguages["languages_id_xxx"].has_key(xx_id):
		   globals.language_system_id = xx_id
    
    def DefaultValue(self,key,value):
		try:
			a = globals.preferences_list[key] 
		except:
			globals.preferences_list[key] = value
		a = 3

    def GetAvailableTranslations(self):
	globals.Log("-----XMLRPC GetAvailableTranslations----\n")

	list_translations = globals.xmlrpc_server.GetAvailableTranslations(globals.osdb_token)["data"]	
	globals.new_translations_dates = {}
	for lang,array in list_translations.items():
		globals.new_translations_dates[lang] =  time.mktime(time.strptime(array["LastCreated"],"%Y-%m-%d %H:%M:%S"))
    def ChooseInitialLanguage(self):
	
	languages = []
	for lang in globals.new_translations_dates.keys():
	    languages_xxx = globals.sublanguages["languages_xx2xxx"][lang]
	    languages.append(globals.sublanguages["languages_id_xxx"][languages_xxx][1])
		
	#languages = globals.sublanguages["languages_name2xxx"].keys()
	languages.sort()
	dlg_choose_lang = wx.SingleChoiceDialog(
	    None, 'Choose Interface Language:', 'Interface Language',languages,wx.OK)
	
	local_language = globals.ConvertLang_xx2name(globals.preferences_list["app_language"])
	dlg_choose_lang.SetSelection(languages.index(local_language))
	if dlg_choose_lang.ShowModal() == wx.ID_OK:
	   lang_str = dlg_choose_lang.GetStringSelection()
	   lang_xx = globals.sublanguages["languages_id_xxx"][globals.sublanguages["languages_name2xxx"][lang_str]][0]
	   if lang_xx != "en":
		self.download_lang = PP.PyProgress(None, -1, _("Downloading Language"),
		    _("Downloading %s language, it can take a while...") % lang_str,
		    style = wx.PD_CAN_ABORT)
    
		self.download_lang.CenterOnParent()
		self.download_lang.UpdatePulse()
		result = globals.DownloadNewTranslations(lang_xx)
		self.download_lang.UpdatePulse()
		self.download_lang.Destroy()
		
	   self.SetupAppLang()
	   globals.preferences_list["app_language"] = lang_xx

	dlg_choose_lang.Destroy()
    def SetDefaultSubLanguages(self):
		languages_id_xxx= {
			"alb":["sq","Albanian"],
			"arm":["hy","Armenian"],
			"ass":["ay","Assyrian"],
			"bos":["bs","Bosnian"],
			"bul":["bg","Bulgarian"],
			"hrv":["hr","Croatian"],
			"cze":["cs","Czech"],
			"dan":["da","Danish"],
			"dut":["nl","Dutch"],
			"eng":["en","English"],
			"est":["et","Estonian"],
			"fin":["fi","Finnish"],
			"fre":["fr","French"],
			"ger":["de","German"],
			"ell":["gr","Greek"],
			"heb":["he","Hebrew"],
			"hun":["hu","Hungarian"],
			"chi":["zh","Chinese"],
			"ita":["it","Italian"],
			"jpn":["ja","Japanese"],
			"kaz":["kk","Kazakh"],
			"lav":["lv","Latvian"],
			"nor":["no","Norwegian"],
			"pol":["pl","Polish"],
			"por":["pt","Portuguese"],
			"pob":["pb","Brazilian"],
			"rum":["ro","Romanian"],
			"rus":["ru","Russian"],
			"scc":["sr","Serbian"],
			"slo":["sk","Slovak"],
			"slv":["sl","Slovenian"],
			"spa":["es","Spanish"],
			"swe":["sv","Swedish"],
			"tha":["th","Thai"],
			"tur":["tr","Turkish"],
			"ukr":["uk","Ukrainian"],
			"cat":["ca","Catalan"],
			"vie":["vi","Vietnamese"]
			}
			
		languages_name2xxx = {}
		for xxx,[xx,name] in languages_id_xxx.items():
		  languages_name2xxx[name] = xxx
		  
		
		  
		languages_xx2xxx = {}
		for xxx,[xx,name] in languages_id_xxx.items():
		  languages_xx2xxx[xx] = xxx
		
		globals.sublanguages["languages_id_xxx"] = languages_id_xxx
		globals.sublanguages["languages_name2xxx"] = languages_name2xxx
		globals.sublanguages["languages_xx2xxx"] = languages_xx2xxx

		
    def SetupAppLang(self):
	lang_app_xx = globals.preferences_list["app_language"]
	try:  
	    isTrans = gettext.translation(domain = "subdownloader",localedir = globals.sourcefolder+"/locale",languages=[lang_app_xx],fallback=True)  
	except IOError:  
	    isTrans = False  
	
	if isTrans:  
		# needed for the _ in the __init__ plugin (menuentry traduction)
		__builtin__._ = lambda s : gettext.translation("subdownloader",globals.sourcefolder+"/locale",languages=[lang_app_xx],fallback=True).ugettext(s)  
	else:  
		__builtin__._ = lambda x : x  

    def ManageArguments(self):
	if len(sys.argv) != 1:
	    
	    status_before = ""
	    error_syntax = False
	    stop_running = False

	    activated_gui = False
	    activated_search = False
	    activated_upload = False
	    list_of_paramfiles = False

	    for param in sys.argv[1:]:
		if status_before == "":
		    if param == "--gui":
			if activated_gui:
			    error_syntax = True
			    stop_running = True
			    break
			activated_gui = True
			continue
			
		    if param == "--search":
			if activated_search or activated_upload:
			    error_syntax = True
			    stop_running = True
			    break
			activated_search = True
			status_before  = param
			continue
		    if param == "--upload":
			if activated_search or activated_upload:
			    error_syntax = True
			    stop_running = True
			    break
			activated_upload = True
			status_before  = param
			continue

		    else:
			if os.path.exists(param):
			    status_before = "--search"
			    list_of_paramfiles = True
			    activated_gui = True
			else:
			    error_syntax = True
			    stop_running = True
			    break
		    
		if status_before == "--search":
			cachefile = ".cachesearch"
		elif status_before == "--upload":
			cachefile = ".cacheupload"
			
		globals.param_function = status_before
	       
		if activated_gui:
		    if os.path.exists(os.path.join(globals.sourcefolder,cachefile)):
			f = open(os.path.join(globals.sourcefolder,cachefile),"aw")
			f.write(param)
			f.write("\n")
			f.close()
			if not list_of_paramfiles:
			    stop_running = True
		    else:
			#We create the file and launch the GUI
			f = open(os.path.join(globals.sourcefolder,cachefile),"w")
			f.write(param)
			f.write("\n")
			f.close()
		else:
		     globals.param_files = [param]
		
	
	    if error_syntax:
		print "Error Syntax:"
		print "Parameters:" 
		print "--search"
		print "--upload"
		
	    if stop_running:
		sys.exit(0)
	else:	    
		if os.path.exists(os.path.join(globals.sourcefolder,".cachesearch")):
		    os.remove(os.path.join(globals.sourcefolder,".cachesearch"))
		
		if os.path.exists(os.path.join(globals.sourcefolder,".cacheupload")):
		    os.remove(os.path.join(globals.sourcefolder,".cacheupload"))
		    
    def OnInit(self):
	globals.sourcefolder = os.path.dirname(sys.argv[0])
	self.ManageArguments()
	self.LoadPreferences()
	self.SetupAppLang()
	
	wx.InitAllImageHandlers()

	self.SubDownloaderWindow = SubDownloaderFrame.MainFrame(self,None, -1, "")
	#self.SetTopWindow(self.SubDownloaderWindow)

	self.SubDownloaderWindow.Show()
	self.SubDownloaderWindow.CenterOnScreen()
	
        return 1
    
    # end of class MainApp

    
if __name__ == "__main__":

	SubDownloaderApp = MainApp(0)
	SubDownloaderApp.MainLoop()
	
           
	    