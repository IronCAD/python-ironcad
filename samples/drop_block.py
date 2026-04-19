import python_ironcad
from python_ironcad import ICAPI

IRONCAD = python_ironcad.IronCAD()
IRONCAD.attach()
IZBase : ICAPI.IZBaseApp = IRONCAD.GetIZBaseApp()
print(IZBase)
catalogmgr : ICAPI.IZCatalogMgr = IZBase.CatalogMgr

# note: you need to have the starter catalog loaded for this to work
catalogs = [catalogmgr.Catalog(i) for i in range(catalogmgr.Count)]

starter_catalog : ICAPI.IZCatalog = next((c for c in catalogs if c.Name == "Starter"), None)

if starter_catalog is None:
    print("Starter Catalog not found.")
    exit(1)

entries = [starter_catalog.Entry(i) for i in range(starter_catalog.EntryCount)]
extrude : ICAPI.IZCatalogEntry = next((e for e in entries if e.Name == "Extrude"), None)

if extrude is None:
    print("Extrude Entry not found.")
    exit(1)

extrude.DropObject(0,0)

IZDocument : ICAPI.IZDoc = IZBase.ActiveDoc
IZSceneDoc : ICAPI.IZSceneDoc = IZDocument.QueryInterface(ICAPI.IZSceneDoc)
IZSceneDoc.Redraw()