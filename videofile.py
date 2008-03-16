##    Copyright (C) 2007 Ivan Garcia contact@ivangarcia.org
##    This program is free software; you can redistribute it and/or modify
##    it under the terms of the GNU General Public License as published by
##    the Free Software Foundation; either version 2 of the License, or
##    (at your option) any later version.
##
##    This program is distributed in the hope that it will be useful,
##    but WITHOUT ANY WARRANTY; without even the implied warranty of
##    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##    GNU General Public License for more details.
##
##    You should have received a copy of the GNU General Public License along
##    with this program; if not, write to the Free Software Foundation, Inc.,
##    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.


import os.path
import struct
from subdownloader import *

VIDEOS_EXT = ["avi","mpg","mpeg","wmv","divx","mkv","ogm","asf", "mov", "rm", "vob", "dv", "3ivx"]


class VideoFile(object):
    """Contains the class that represents a VideoFile (AVI,MPG,etc)
    and provides easy methods to retrieve its attributes (Sizebytes, HASH, FPS,etc)
    """
   
    def __init__(self, filepath):
        self._filepath = filepath
        self._size = os.path.getsize(filepath)
        self._hash = self.calculateOSDBHash()
        self._fps = 0
        self._osdb_info = {}
        self._subs = []
        self.nos_subs = []
    
    def getFilePath(self):
        return self._filepath
    
    def getFolderPath(self):
        return os.path.dirname(self._filepath)
    
    def getFileName(self):
        return os.path.basename(self._filepath)
    
    def getSize(self):
        return self._size
    
    def getHash(self):
        return self._hash
    
    def getFPS(self):
        return self._fps
    
    def setOsdbInfo(self,info):
        self._osdb_info = info
    
    def getOsdbInfo(self):
        return self._osdb_info
    
    def hasOsdbInfo(self):
        return len(self._osdb_info) != 0
    
    def hasMovieName(self):
        try: return self._osdb_info["MovieName"] != ""
        except: return False
    
    def getMovieName(self):
        return self._osdb_info["MovieName"]
    
    def hasMovieNameEng(self):
        try: return self._osdb_info["MovieNameEng"] != ""
        except: return False
    
    def getMovieNameEng(self):
        return self._osdb_info["MovieNameEng"]
    
    def hasSubtitles(self):
        return len(self._subs) != 0
    
    def setSubtitles(self,subs):
        if len(self._subs):
            # we might have set other subtitles before
            for sub in subs:
                for _sub in self._subs:
                    if sub.getHash() == _sub.getHash():
                        subs.pop(subs.index(sub))
            self.addSubtitle(subs)
        else:
            self._subs = subs
        
    def addSubtitle(self, sub):
        if isinstance(sub, list):
            self._subs + sub
        else:
            self._subs.append(sub)
        
    def getSubtitle(self, hash):
        """returns the subtitle by its hash if any"""
        for sub in self.getSubtitles():
            if sub.getHash() == hash:
                return sub
        return None
    
    def getSubtitles(self):
        return self._subs
        
    def hasSubtitles(self):
        return len(self._subs) != 0
        
    def getOneSubtitle(self):
        return self._subs[0]
        
    def getOnlineSubtitles(self):
        subs = []
        for sub in self.getSubtitles():
            if sub.isOnline(): subs.append(sub)
        return subs
    
    def getTotalSubtitles(self):
        try: return len(self._osdb_info)
        except: return len(self._subs)
        
    def getTotalOnlineSubtitles(self):
        return len(self.getOnlineSubtitles())
        
    def setNOSSubtitle(self, sub):
        """ transfer a subtitle from general list to 'not on server'
        """
        self.nos_subs.append(sub)
        self._subs.pop(self._subs.index(sub))
        
    def remNOSSubtitle(self, sub):
        """removes a subtitle from NOS list"""
        self.nos_subs.pop(self.nos_subs.index(sub))
        
    def getNOSSubtitles(self):
        return self.nos_subs
        
    def hasNOSSubtitles(self):
        return len(self.nos_subs) != 0
    
    def calculateOSDBHash(self):
        try:
            longlongformat = 'LL'  # signed long, unsigned long
            bytesize = struct.calcsize(longlongformat)

            filesize = os.path.getsize(self._filepath)
            hash = filesize
            f = file(self._filepath, "rb")
            #print struct.calcsize(longlongformat)
            if filesize < 65536 * 2:
                return "SizeError"
            
            for x in range(65536/bytesize):
                buffer = f.read(bytesize)
                (l2, l1)= struct.unpack(longlongformat, buffer)
                l_value = (long(l1) << 32) | long(l2)
                hash += l_value
                hash = hash & 0xFFFFFFFFFFFFFFFF #to remain as 64bit number
                #if x < 20 : print "%016x" % hash
                
            
            f.seek(max(0,filesize-65536),0)
            for x in range(65536/bytesize):
                buffer = f.read(bytesize)
                (l2, l1) = struct.unpack(longlongformat, buffer)
                l_value = (long(l1) << 32) | long(l2)
                hash += l_value
                hash = hash & 0xFFFFFFFFFFFFFFFF
        
            f.close()
            returnedhash =  "%016x" % hash
            return returnedhash
            
        except(IOError):
            return "IOError"