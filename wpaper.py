from ctypes import *
from os import path

SPI_SETDESKWALLPAPER = 0x14
SPIF_UPDATEINIFILE   = 0x1

SystemParametersInfo = windll.user32.SystemParametersInfoA
SystemParametersInfo(SPI_SETDESKWALLPAPER, 0, "C:\\Users\\Public\\Pictures\\background1024x768.bmp", SPIF_UPDATEINIFILE);
