from ctypes import *
from os import path
import feedparser
from datetime import datetime
import urllib

SPI_SETDESKWALLPAPER = 0x14
SPIF_UPDATEINIFILE   = 0x1

#SystemParametersInfo = windll.user32.SystemParametersInfoA
#SystemParametersInfo(SPI_SETDESKWALLPAPER, 0, "C:\\Users\\Public\\Pictures\\background1024x768.bmp", SPIF_UPDATEINIFILE);

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
background_url.split(".")

for i in background_url:
   print i
#urllib.urlretrieve(i
