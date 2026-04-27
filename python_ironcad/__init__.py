import comtypes.tools.tlbparser
import comtypes.automation
import python_ironcad.modified_tlbparser
import ctypes
comtypes.tools.tlbparser.Parser.make_type = python_ironcad.modified_tlbparser.Parser.make_type
comtypes.automation._vartype_to_ctype[13] = ctypes.c_ulonglong


from .core import IronCAD, ICAPI