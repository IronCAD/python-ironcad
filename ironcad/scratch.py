from core import IronCAD
import inspect

IRONCAD = IronCAD()
# attach process
IRONCAD.attach()

IZBaseApp = IRONCAD.get_baseapp()

# get and print all docs
docs = IZBaseApp.GetAllOpenDocs()
print(docs)