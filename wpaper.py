from ctypes import *
from os import path
import feedparser
from datetime import datetime
import urllib      
import win32api

SPI_SETDESKWALLPAPER = 0x14
SPIF_UPDATEINIFILE   = 0x1
HTML_EXT_LEN = 5

SystemParametersInfo = windll.user32.SystemParametersInfoA

fd = feedparser.parse("http://wallpaperswide.com/rss/index.html")
#print fd.feed.title
#print fd.entries[0].title
#print fd.entries[0].link
#print fd.entries[0].published

toSort = fd.entries

toSort.sort(key=lambda i: datetime.strptime(i.published[:25], "%a, %d %b %Y %H:%M:%S"), reverse = True)
print "now after they are sorted"

#for i in toSort:
#   print i.published[:25]
background_url = toSort[0].link
#background_url = background_url.split(".")

print background_url[:len(background_url) - HTML_EXT_LEN]
#urllib.urlretrieve(
monitorWxH = str(windll.user32.GetSystemMetrics(0)) + "x" + str(windll.rser32.GetSystemMetrics(1))
saveLocation = "C:\\Users\\" + win32api.GetUserName() + "\\AppData\\Local\\Temp\\wp.jpg"
urllib.urlretrieve(background_url + monitorWxH + ".jpg", saveLocation)

SystemParametersInfo(SPI_SETDESKWALLPAPER, 0, "C:\\Users\\Public\\Pictures\\background1024x768.bmp", SPIF_UPDATEINIFILE);
