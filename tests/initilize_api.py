import python_ironcad
from test_utils import print_green_dot, print_fail, print_success

def test_attach_and_get_baseapp():
    print("\nRunning test: Attach to IRONCAD and get BaseApp interface\n")
    try:
        IRONCAD = python_ironcad.IronCAD()
        print("    Created IronCAD instance", end="")
        print_green_dot()
        IRONCAD.attach()
        print("    Attached to IRONCAD process", end="")
        print_green_dot()
        # IRONCAD.launch() # to start a new instance
        # IRONCAD.launch()
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
            print_success("Successfully attached to IRONCAD and obtained BaseApp interface.")
            return True
    except Exception as e:
        print_fail(f"Unexpected error: {e}")
        return False

def test_get_old_automation_interface():
    print("\nRunning test: Get old automation interface\n")
    try:
        IRONCAD = python_ironcad.IronCAD()
        print("    Created IronCAD instance", end="")
        print_green_dot()
        IRONCAD.attach()
        print("    Attached to IRONCAD process", end="")
        print_green_dot()
        try:
            old_interface = IRONCAD.GetOldAutomationInterface()
            print("    Called GetOldAutomationInterface()", end="")
            print_green_dot()
        except Exception as e:
            print_fail(f"Error getting old automation interface {type(e)}: {e}")
            return False
        if old_interface is None:
            print_fail("Failed to get old automation interface. Make sure IRONCAD is running and the API is properly registered.")
            return False
        else:
            print_success("Successfully obtained old automation interface.")
            return True
    except Exception as e:
        print_fail(f"Unexpected error: {e}")
        return False
