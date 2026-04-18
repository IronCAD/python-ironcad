from comtypes import client
from ctypes import wintypes
from core import IronCAD

IRONCAD = IronCAD()
IRONCAD.attach()

IZBaseApp = IRONCAD.get_baseapp()

help(IZBaseApp)