import ctypes
import sys
import winreg
import subprocess
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
    
if not is_admin():
    # Relaunch as admin
    inp = input("python-ironcad setup requires admin privileges. Do you want to continue? (y/n): ")
    if inp.lower() != 'y':
        sys.exit()
    ctypes.windll.shell32.ShellExecuteW(
        None, "runas", sys.executable, " ".join(sys.argv), None, 1
    )
    sys.exit()

def get_ironcad_install_dir(version):
    try:
        key_path = fr"SOFTWARE\IronCAD\IRONCAD\{version}.0"
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path) as key:
            install_dir, _ = winreg.QueryValueEx(key, "InstallDir")
            return install_dir
    except FileNotFoundError:
        return None

if __name__ == "__main__":
    # Your main code here
    print("Running with admin privileges")
    for i in range(35, 25, -1):
        install_dir = get_ironcad_install_dir(i)
        if install_dir:
            print(f"IRONCAD {i}.0 InstallDir: {install_dir}")
            ironcad_version = i
            break
    if install_dir is None:
        print("No supported IRONCAD version found")
        inp = input("Press Enter to exit...")
        exit(1)
    print("IRONCAD installation directory found. Proceeding with setup...")


    print("Registering COM components...")
    procs = []
    procs.append(subprocess.run(["Regsvr32", f"{install_dir}bin\\3iICApiIronCADApp.dll", "/s"], cwd=install_dir))
    print("Registered 3iICApiIronCADApp.dll")
    procs.append(subprocess.run(["Regsvr32", f"{install_dir}bin\\3iICApiDrawing.dll", "/s"], cwd=install_dir))
    print("Registered 3iICApiDrawing.dll")
    procs.append(subprocess.run(["Regsvr32", f"{install_dir}bin\\3iICApiCore.dll", "/s"], cwd=install_dir))
    print("Registered 3iICApiCore.dll")
    procs.append(subprocess.run(["Regsvr32", f"{install_dir}bin\\3iICApiBase.dll", "/s"], cwd=install_dir))
    print("Registered 3iICApiBase.dll")

    for i in procs:
        if i.returncode != 0:
            print("Error registering COM component. Please check the output above for details.")
            inp = input("Press Enter to exit...")
            exit(1)
    print("All COM components registered successfully.")
    inp = input("Setup completed successfully. Press Enter to exit...")

