import comtypes 
import comtypes.client
import importlib
import os

import inspect
from comtypes import IUnknown

comtypes.client.GetModule("C:\\Program Files\\IronCAD\\2026\\bin\\ICApiIronCAD.tlb")
comtypes.client.GetModule("C:\\Program Files\\IronCAD\\2026\\bin\\IronCad.tlb")
import comtypes.gen.ICAPIIRONCADLib as ApiBase
import comtypes.gen.IronCAD as IronCADLib


class ComWrapper:
    def __init__(self, comobject):
        self.comobject = comobject
    
    def get_com_object(self):
        return self.comobject


class IronCAD(ComWrapper):
    def __init__(self):
        self.comobject = None
        # self.application.Visible = True

    def attach(self):
        self.comobject = comtypes.client.GetActiveObject("IronCAD.Application")

    def launch(self):
        self.comobject = comtypes.client.CreateObject("IronCAD.Application")

    def get_baseapp(self):
        if self.comobject == None:
            return None
        return self.comobject.ZIronCADApp.QueryInterface(ApiBase.IZBaseApp)
    
    def get_ironcadapp(self):
        if self.comobject == None:
            return None
        return self.comobject


    


if __name__ == "__main__":


    ironcad = IronCAD()

    ironcad.attach()
    
    baseapp = ironcad.get_baseapp()

    print(baseapp)


