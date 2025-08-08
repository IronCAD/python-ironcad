import comtypes.client
import os
import importlib
import inspect

binpath = "C:\\Program Files\\IronCAD\\2026\\bin"

binfolder = os.listdir(binpath)

print(binfolder)


for i in binfolder:
    try:
        comtypes.client.GetModule(os.path.join(binpath, i))
        print(f"Loaded module: {i}")
    except Exception as e:
        print(f"Failed to load module {i}")

modules = []

for i in os.listdir(comtypes.gen.__path__[0]):
    if i[0] != "_":
        try:
            modules.append(importlib.import_module(f"comtypes.gen.{i.replace('.py', '')}"))
        except Exception as e:
            print(f"Failed to import module {i}: {e}")
        interfaces = []
        for name in dir(modules[-1]):
            obj = getattr(modules[-1], name)
            if inspect.isclass(obj) and issubclass(obj, comtypes.IUnknown):
                interfaces.append(name)

        # Print them
        print(f"COM interfaces in module: {modules[-1].__name__}")
        for interface in interfaces:
            try:
                print(" -", interface)
            except Exception as e:
                pass