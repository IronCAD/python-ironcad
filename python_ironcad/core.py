import comtypes
import winreg
import comtypes.client
import ctypes

IRONCAD_MAX_VERSION = 35



def get_ironcad_install_dir(version):
    try:
        key_path = fr"SOFTWARE\IronCAD\IRONCAD\{version}.0"
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path) as key:
            install_dir, _ = winreg.QueryValueEx(key, "InstallDir")
            return install_dir
    except FileNotFoundError:
        return None


ironcad_version = "Unknown"

for i in range(IRONCAD_MAX_VERSION, 25, -1):
    install_dir = get_ironcad_install_dir(i)
    if install_dir:
        print(f"IRONCAD {i}.0 InstallDir: {install_dir}")
        ironcad_version = i
        break

if install_dir is None:
    raise Exception("No supported IRONCAD version found")

comtypes.client.GetModule(f"{install_dir}\\bin\\ICApiIronCAD.tlb")

import comtypes.gen.ICAPIIRONCADLib as ICAPI

print(f"Using IRONCAD version: {ironcad_version}")
print("Extracting API from type library, this may take a while...")

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
    
    def GetIZBaseApp(self):
        try:
            return self.get_baseapp()
        except Exception as e:

            print("""
\033[91mError getting BaseApp interface. This usually means the API is not properly registered.\033[0m
to register the API please run the setup script:
    >> python -m python_ironcad
If this doesn't work, you can manually register the COM components using regsvr32:
    >> regsvr32 "<IRONCAD install path>\\bin\\3iICApiIronCADApp.dll"
    >> regsvr32 "<IRONCAD install path>\\bin\\3iICApiDrawing.dll"
    >> regsvr32 "<IRONCAD install path>\\bin\\3iICApiCore.dll"
    >> regsvr32 "<IRONCAD install path>\\bin\\3iICApiBase.dll"
the default install path is usually "C:\\Program Files\\IronCAD\\<version>\\" but may vary depending on your installation. 
Make sure to run the command prompt as administrator when registering the COM components. 
""")

            raise Exception(f"Error in GetIZBaseApp: {e}")

    def GetOldAutomationInterface(self):
        return self.get_ironcadapp()


