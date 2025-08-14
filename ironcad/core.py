import comtypes 
import comtypes.client

comtypes.client.GetModule("C:\\Program Files\\IronCAD\\2026\\bin\\ICApiIronCAD.tlb")
import comtypes.gen.ICAPIIRONCADLib as ICAPI


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


    


if __name__ == "__main__":


    ironcad = IronCAD()

    ironcad.launch()
    
    baseapp = ironcad.get_baseapp()

    print(baseapp)


