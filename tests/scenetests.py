from python_ironcad import IronCAD
import ctypes
from test_utils import print_green_dot, print_fail, print_success

def test_create_new_scene():
    print("\nRunning test: Create new scene\n")
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