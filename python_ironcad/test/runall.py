from python_ironcad.test.initilize_api import test_attach_and_get_baseapp, test_get_old_automation_interface
from python_ironcad.test.scenetests import test_create_new_scene

TESTS = [
    ("Attach to IRONCAD and get BaseApp interface", test_attach_and_get_baseapp),
    ("Get old automation interface", test_get_old_automation_interface),
    ("Create new scene", test_create_new_scene)
]

def run_all_tests():
    print("\n====================")
    print("Running all tests...")
    print("====================\n")
    passed = 0
    failed = 0
    for name, test_func in TESTS:
        print(f"Test: {name}")
        result = test_func()
        if result:
            passed += 1
        else:
            failed += 1
        print("\n--------------------\n")
    print(f"\nSummary: {passed} passed, {failed} failed, {passed+failed} total.")
    if failed == 0:
        print("\033[92mALL TESTS PASSED\033[0m\n")
    else:
        print("\033[91mSOME TESTS FAILED\033[0m\n")

if __name__ == "__main__":
    run_all_tests()
