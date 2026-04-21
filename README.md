# python-ironcad

<p align="center">
    <img src="https://www.ironcad.com/wp-content/uploads/2016/05/product_icon_ironcad.png" alt="IronCAD Logo">
</p>

A Python module for IronCAD automation and scripting. This package exposes IRONCAD's entire API to python.

## Installation

```powershell
pip install python-ironcad
```

In order for python to access the IRONCAD API, dll's from IRONCAD's install need to be registered system-wide. to do this, simply run the setup script:
```powershell
python -m python_ironcad
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
IZDoc = IZBaseApp.ActiveDoc # get currently open document
```
if you want to launch new IRONCAD process
```python
IRONCAD.launch()
IZBaseApp = IRONCAD.GetIZBaseApp()
IZDoc = IZBaseApp.CreateNewDoc(1, 0, 1, "", 1) # create a new document
```
Please refer to [samples](https://github.com/IronCAD/python-ironcad/tree/main/samples) for more in-depth examples

# tips
### help() function to find member methods and data
to inspect all members of a given object, use help(object)
![help function](https://github.com/IronCAD/python-ironcad/blob/main/docs/images/help.png?raw=true)

### intellisense in Visual Studio Code
if you want to use intellisense to see object members, you can use python type hints. (this also works in pycharm)

![Intellisense](https://github.com/IronCAD/python-ironcad/blob/main/docs/images/intellisense.png?raw=true)

# known issues
- INOVATE is currently not supported 
- Some methods that use VARIANT type don't work 
- currently only targets the most recent installed version of IRONCAD