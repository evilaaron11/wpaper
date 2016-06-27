from ctypes import *
from os import path
import feedparser
from datetime import datetime
import urllib      
import win32api

SPI_SETDESKWALLPAPER = 0x14
SPIF_UPDATEINIFILE   = 0x1
HTML_EXT_LEN = 6
SITE_URL = "http://wallpaperswide.com/"

SystemParametersInfo = windll.user32.SystemParametersInfoA

fd = feedparser.parse("http://wallpaperswide.com/rss/index.html")

toSort = fd.entries
toSort.sort(key=lambda i: datetime.strptime(i.published[:25], "%a, %d %b %Y %H:%M:%S"), reverse = True)

background_url = toSort[0].link
background_url= background_url[len(SITE_URL):len(background_url) - HTML_EXT_LEN] + "-"

monitorWxH = str(windll.user32.GetSystemMetrics(0)) + "x" + str(windll.user32.GetSystemMetrics(1))
saveLocation = "C:\\Users\\" + win32api.GetUserName() + "\\AppData\\Local\\Temp\\wp.jpg"

#print "Downloading wallpaper..."

urllib.urlretrieve(SITE_URL + "/download/" + background_url + monitorWxH + ".jpg", saveLocation)

#print "Wallpaper set to " + toSort[0].title
SystemParametersInfo(SPI_SETDESKWALLPAPER, 0, saveLocation, SPIF_UPDATEINIFILE);
