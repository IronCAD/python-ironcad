import comtypes 
import comtypes.client

IRONCAD_VERSION = 2026

for i in range(IRONCAD_VERSION, 2019, -1):
    try:
        comtypes.client.GetModule(f"C:\\Program Files\\IronCAD\\{i}\\bin\\ICApiIronCAD.tlb")
        break
    except OSError:
        continue

import comtypes.gen.ICAPIIRONCADLib as ICAPI

print(f"Using IRONCAD version: {IRONCAD_VERSION}")

class ComWrapper:
    def __init__(self, comobject):
        self.comobject = comobject
    
    def get_com_object(self):
        return self.comobject


class IronCAD(ComWrapper):
    def __init__(self):
        self.comobject = None

    def attach(self):
        self.comobject = comtypes.client.GetActiveObject("IronCAD.Application")

    def launch(self, machine=None):
        self.comobject = comtypes.client.CreateObject("IronCAD.Application", machine=machine)

    def get_baseapp(self):
        if self.comobject == None:
            return None
        return self.comobject.ZIronCADApp.QueryInterface(ICAPI.IZBaseApp)

    def get_ironcadapp(self):
        if self.comobject == None:
            return None
        return self.comobject


