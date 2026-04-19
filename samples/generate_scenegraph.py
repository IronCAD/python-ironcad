import python_ironcad
from python_ironcad import ICAPI
import json

IRONCAD = python_ironcad.IronCAD()
IRONCAD.attach()
IZBase : ICAPI.IZBaseApp = IRONCAD.GetIZBaseApp()

# get the top shape of the document
document: ICAPI.IZDoc = IZBase.ActiveDoc
scenedoc: ICAPI.IZSceneDoc = document.QueryInterface(ICAPI.IZSceneDoc)
topelement: ICAPI.IZElement = scenedoc.GetTopElement()

# recurse collecting all elements
scenegraph = {}

def collect_sub_elements(element: ICAPI.IZElement):
    # queryinterface here to make sure every input is a true element
    try:
        element: ICAPI.IZElement = element.QueryInterface(ICAPI.IZElement)
    except Exception as e:
        return
    # you could do ret = {element.Name: element}
    # if you wanted an easily traversable dictionary that stored element pointers
    # I am just using Id here to make it json serializable
    ret = {element.Name: element.Id}
    try:
        if element.GetChildrenCount() > 0:
            ret["children"] = []
            elementarray: ICAPI.IZArray = element.GetChildrenZArray()
            for index in range(elementarray.Count()):
                ret["children"].append(collect_sub_elements(elementarray.Get(index)))
    except Exception as e:
        pass
    return ret

scenegraph = collect_sub_elements(topelement)

print(json.dumps(scenegraph, indent=1))

"""
example output generated from a tank made with the included tank catalog:
{
 "": 1,
 "children": [
  {
   "Stainless Steel Tank": 2,
   "children": [
    {
     "Sheet Metal Loft1": 3,
     "children": [
      {
       "2D Profile2": 4
      },
      {
       "2D Profile3": 5
      },
      {
       "": 6
      }
     ]
    }
   ]
  },
  {
   "Tank Lid Ring": 7,
   "children": [
    {
     "Turn1": 8,
     "children": [
      {
       "": 9
      }
     ]
    },
    {
     "H Cylinder": 10,
     "children": [
      {
       "2D Profile1": 11
      }
     ]
    },
    {
     "Circular Pattern4": 12
    }
   ]
  },
  {
   "Tank Lid": 13,
   "children": [
    {
     "Cylinder": 14,
     "children": [
      {
       "2D Profile1": 15
      }
     ]
    },
    {
     "H Cylinder": 16,
     "children": [
      {
       "2D Profile1": 17
      }
     ]
    },
    {
     "Circular Pattern36": 18
    }
   ]
  },
  {
   "Leg Assembly": 53,
   "children": [
    {
     "Steel": 54,
     "children": [
      {
       "Block": 55,
       "children": [
        {
         "2D Profile1": 56
        }
       ]
      },
      {
       "Blend1": 57
      },
      {
       "Shell1": 58
      }
     ]
    },
    {
     "Pattern28": 59
    },
    {
     "Steel": 60,
     "children": [
      {
       "Block": 61,
       "children": [
        {
         "2D Profile1": 62
        }
       ]
      },
      {
       "Blend1": 63
      },
      {
       "Shell1": 64
      }
     ]
    },
    {
     "Steel": 65,
     "children": [
      {
       "Block": 66,
       "children": [
        {
         "2D Profile1": 67
        }
       ]
      },
      {
       "Blend1": 68
      },
      {
       "Shell1": 69
      }
     ]
    },
    {
     "Leg Cap": 70,
     "children": [
      {
       "Slab": 71,
       "children": [
        {
         "2D Profile1": 72
        }
       ]
      },
      {
       "Scale1": 73
      }
     ]
    },
    {
     "Leg Cap": 74,
     "children": [
      {
       "Slab": 75,
       "children": [
        {
         "2D Profile1": 76
        }
       ]
      },
      {
       "Scale1": 77
      }
     ]
    },
    {
     "Leg Cap": 78,
     "children": [
      {
       "Slab": 79,
       "children": [
        {
         "2D Profile1": 80
        }
       ]
      },
      {
       "Scale1": 81
      }
     ]
    }
   ]
  },
  {
   "Base Pads": 82,
   "children": [
    {
     "Base Pad": 83,
     "children": [
      {
       "Slab": 84,
       "children": [
        {
         "2D Profile1": 85
        }
       ]
      }
     ]
    },
    {
     "Pattern9": 86
    },
    {
     "Base Pad": 87,
     "children": [
      {
       "Slab": 88,
       "children": [
        {
         "2D Profile1": 89
        }
       ]
      }
     ]
    },
    {
     "Base Pad": 90,
     "children": [
      {
       "Slab": 91,
       "children": [
        {
         "2D Profile1": 92
        }
       ]
      }
     ]
    }
   ]
  },
  {
   "Pattern28": 93
  },
  {
   "Base Pads": 94,
   "children": [
    {
     "Base Pad": 95,
     "children": [
      {
       "Slab": 96,
       "children": [
        {
         "2D Profile1": 97
        }
       ]
      }
     ]
    },
    {
     "Pattern9": 98
    },
    {
     "Base Pad": 99,
     "children": [
      {
       "Slab": 100,
       "children": [
        {
         "2D Profile1": 101
        }
       ]
      }
     ]
    },
    {
     "Base Pad": 102,
     "children": [
      {
       "Slab": 103,
       "children": [
        {
         "2D Profile1": 104
        }
       ]
      }
     ]
    }
   ]
  },
  {
   "Base Pads": 105,
   "children": [
    {
     "Base Pad": 106,
     "children": [
      {
       "Slab": 107,
       "children": [
        {
         "2D Profile1": 108
        }
       ]
      }
     ]
    },
    {
     "Pattern9": 109
    },
    {
     "Base Pad": 110,
     "children": [
      {
       "Slab": 111,
       "children": [
        {
         "2D Profile1": 112
        }
       ]
      }
     ]
    },
    {
     "Base Pad": 113,
     "children": [
      {
       "Slab": 114,
       "children": [
        {
         "2D Profile1": 115
        }
       ]
      }
     ]
    }
   ]
  },
  {
   "Part3": 116,
   "children": [
    {
     "Extrude": 117,
     "children": [
      {
       "2D Profile1": 118
      }
     ]
    }
   ]
  }
 ]
}
"""

