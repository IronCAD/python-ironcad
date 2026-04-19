from python_ironcad import IronCAD
import ctypes
from ctypes import wintypes
import comtypes.gen.ICAPIIRONCADLib as ICAPI
import comtypes.client
import time
IRONCAD = IronCAD()
IRONCAD.attach()

IZBaseApp = IRONCAD.get_baseapp()
IIronCADApp = IRONCAD.get_ironcadapp()
IIronCADApp.Visible = True
IronCADWindow = IIronCADApp.HWnd
izdoc = IZBaseApp.ActiveDoc
scenedoc = izdoc.QueryInterface(ICAPI.IZSceneDoc)

# SmartAssemblyExEvents lives in the IZDoc and is what we will be using to set up smart assembly drag and drop
Exevents = izdoc.SmartAssemblyExEvents

CatalogMgr = IZBaseApp.CatalogMgr

# create python list containing all catalog interfaces
catalogs = [CatalogMgr.Catalog(x) for x in range(CatalogMgr.Count)]
Selected_catalog = "TankAI"
Selected_catalog = next((cat for cat in catalogs if cat.Name == Selected_catalog), None)

entries = [Selected_catalog.Entry(x) for x in range(Selected_catalog.EntryCount)]

# collect all of the catalog entries needed
entryname = "Stainless Steel Tank Shell"
Shell = next((ent for ent in entries if ent.Name == entryname), None)
entryname = "Tank Flat Bottom"
bottom = next((ent for ent in entries if ent.Name == entryname), None)
entryname = "Tank Lid Ring"
ring = next((ent for ent in entries if ent.Name == entryname), None)
entryname = "Tank Leg Assembly"
leg = next((ent for ent in entries if ent.Name == entryname), None)
entryname = "Tank Leg Base Pads"
pads = next((ent for ent in entries if ent.Name == entryname), None)
entryname = "Tank Lid"
lid = next((ent for ent in entries if ent.Name == entryname), None)

# IZCatalogEntry.DropObject uses screen coordinates, but since we're setting specific objects to drop on, the actual coordinates don't matter
middle_screen = (0, 0) 

# start building
elem_shell = Shell.InsertElement()

# here we can see the connectors on the shell and get their ID's
for i in range(elem_shell.QueryInterface(ICAPI.IZConnectorMgr).GetConnectorsCount()):
    connectorID = elem_shell.QueryInterface(ICAPI.IZConnectorMgr).GetConnectorIDByIndex(i)
    connectorname = elem_shell.QueryInterface(ICAPI.IZConnectorMgr).GetConnectorNameByIndex(i)
    print(f"Connector {i}: ID = {connectorID}, Name = {connectorname}")

# this is the method that allows us to set up the next object that the catalogentries will be dropped on
Exevents.SetSmartAssemblyNextDroppedOnObj(elem_shell, -1)
scenedoc.Update()
scenedoc.Redraw()
leg.DropObject(*middle_screen) # these will be dropped on the tank shell because we set up the smart assembly drop target
bottom.DropObject(*middle_screen)
Exevents.ResetSmartAssemblyNextDroppedOnObjInfo() # reset the drop target info so future drops are not affected
Exevents.SetSmartAssemblyNextDroppedOnObj(elem_shell, 5) # here I change the attachment point to drop to
ring.DropObject(*middle_screen)
scenedoc.Update()
scenedoc.Redraw()

Exevents.ResetSmartAssemblyNextDroppedOnObjInfo() # reset the drop target info so future drops are not affected

ctypes.windll.user32.PostMessageW(IronCADWindow, 0x0111, 50103, 0) # ID for "Fit All In Window"