from python_ironcad import IronCAD, ICAPI
import ctypes
from python_ironcad.test.test_utils import print_green_dot, print_fail, print_success
from comtypes.automation import VARIANT, VT_ARRAY, VT_I4, VT_R8
from comtypes import safearray

def test_create_new_scene():
    try:
        IRONCAD = IronCAD()
        print("    Created IronCAD instance", end="")
        print_green_dot()
        IRONCAD.attach()
        print("    Attached to IRONCAD process", end="")
        print_green_dot()
        try:
            IZBaseApp = IRONCAD.GetIZBaseApp()
            print("    Called get_baseapp()", end="")
            print_green_dot()
        except Exception as e:
            print_fail(f"Error getting BaseApp interface {type(e)}: {e}")
            return False
        if IZBaseApp is None:
            print_fail("Failed to get BaseApp interface. Make sure IRONCAD is running and the API is properly registered.")
            return False
        else:
            # create new scene
            print("    Creating new scene...", end="")
            print_green_dot()
            newdoc = IZBaseApp.CreateNewDoc(1, 0, 1, "", 1)
            if newdoc is None:
                print_fail("Failed to create new scene.")
                return False
            docname = newdoc.Name
            print(f"    Successfully created new scene: {docname}")
            try:
                print("    Closing the new scene...", end="")
                print_green_dot()
                newdoc.Close()
                print_success("Successfully closed the new scene.")
            except Exception as e:
                print_fail(f"Error closing the new scene {type(e)}: {e}")
                return False


            return True
        

    except Exception as e:
        print_fail(f"Unexpected error: {e}")
        return False
    
def test_add_profile():
    try:
        IRONCAD = IronCAD()
        print("    Created IronCAD instance", end="")
        print_green_dot()
        IRONCAD.attach()
        print("    Attached to IRONCAD process", end="")
        print_green_dot()
        try:
            IZBaseApp = IRONCAD.GetIZBaseApp()
            print("    Called get_baseapp()", end="")
            print_green_dot()
        except Exception as e:
            print_fail(f"Error getting BaseApp interface {type(e)}: {e}")
            return False
        if IZBaseApp is None:
            print_fail("Failed to get BaseApp interface. Make sure IRONCAD is running and the API is properly registered.")
            return False
        else:
            # create new scene
            print("    Creating new scene...", end="")
            print_green_dot()
            newdoc: ICAPI.IZDoc = IZBaseApp.CreateNewDoc(1, 0, 1, "", 1)
            print(f"    Querying for IZSceneDoc interface...", end="")
            print_green_dot()
            scenedoc: ICAPI.IZSceneDoc = newdoc.QueryInterface(ICAPI.IZSceneDoc)
            print(f"    Creating new profile in the scene...", end="")
            print_green_dot()
            profile: ICAPI.IZProfile = scenedoc.CreateProfile()

            print(f"    Adding circle to profile...", end="")
            print_green_dot()
            # perhaps I should add more helper functions to create safe arrays from python lists, etc. This is a bit cumbersome.
            coord_1 = (0.0, 0.0)
            DoubleArrayType = ctypes.c_double * len(coord_1)
            c_array1 = DoubleArrayType(*coord_1)
            circleid = profile.CreateCircleCOM(c_array1, 1, 0)
            print(f"    Created circle with ID: {circleid}")

            if newdoc is None:
                print_fail("Failed to create new scene.")
                return False
            if circleid is None:
                print_fail("Failed to create circle in profile.")
                return False
            docname = newdoc.Name
            print(f"    Successfully created new scene: {docname}")
            try:
                print("    Closing the new scene...", end="")
                print_green_dot()
                newdoc.Close()
                print_success("Successfully closed the new scene.")
            except Exception as e:
                print_fail(f"Error closing the new scene {type(e)}: {e}")
                return False


            return True
        

    except Exception as e:
        print_fail(f"Unexpected error: {e}")
        return False