# python-ironcad

<p align="center">
    <img src="https://www.ironcad.com/wp-content/uploads/2016/05/product_icon_ironcad.png" alt="IronCAD Logo">
</p>

A Python module for IronCAD automation and scripting.

## Installation

```powershell
pip install python-ironcad
```

In order for python to access the IRONCAD API, dll's from IRONCAD's install need to be registered system-wide. to do this, simply run the setup script:
```powershell
python -m python-ironcad
```

## Quick Start
import the package

```python
import python_ironcad
```

construct IronCAD object 
```python
IRONCAD = IronCAD()
```

if you want to attach to currently running IRONCAD process
```python
IRONCAD.attach()
IZBaseApp = IRONCAD.GetIZBaseApp()
IZDoc = IZBaseApp.ActiveDoc
```
if you want to launch new IRONCAD process
```python
IRONCAD.launch()
IZBaseApp = IRONCAD.GetIZBaseApp()
IZDoc = newdoc = IZBaseApp.CreateNewDoc(1, 0, 1, "", 1)
```

### get catalogs and entries
```python
# get catalog manager
CatalogMgr = IZBaseApp.CatalogMgr

# create list containing all catalog interfaces
catalogs = [CatalogMgr.Catalog(x) for x in range(CatalogMgr.Count)]

# print number of catalogs
print(f"{len(catalogs)} catalogs found")

for catalog in catalogs:
    print(f"\tCatalog: {catalog.Name}")
```

you can select a specific catalog by name
```python 
selected_catalog = None
selected_name = "Shapes"

for catalog in catalogs:
    if catalog.Name == selected_name:
        selected_catalog = catalog
        break
```

get a specific catalog entry
```python 
entries = [Selected_catalog.Entry(x) for x in range(Selected_catalog.EntryCount)]
selected_entry_name = "Slot"
selected_entry = None
for entry in entries:
    print(f"\tEntry: {entry.Name}")
    selected_entry = entry
```

drop to scene and get IZElement
```python
element = selected_entry.InsertElement()
```