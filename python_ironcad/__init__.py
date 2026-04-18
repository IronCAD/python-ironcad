import comtypes.tools.tlbparser
import python_ironcad.modified_tlbparser
comtypes.tools.tlbparser.Parser.make_type = python_ironcad.modified_tlbparser.Parser.make_type

from .core import IronCAD, ICAPI