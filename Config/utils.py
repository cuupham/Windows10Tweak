import sys
import ctypes
import subprocess
import winreg as reg


def run_as_admin():
    if not ctypes.windll.shell32.IsUserAnAdmin():
        try:
            ctypes.windll.shell32.ShellExecuteW(
                None, "runas", sys.executable, " ".join(sys.argv), None, 1
            )
        except Exception as e:
            print(f"Yêu cầu quyền admin thất bại: {e}")
        sys.exit(0)


def disable_service(service_name: str):
    try:
        subprocess.run(
            f"sc config {service_name} start= disabled", shell=True, check=True
        )
        print(f"\"{service_name}\": DISABLED SUCCESSFULLY")

    except subprocess.CalledProcessError as e:
        print(
            f"[ERROR] \"{service_name}\" CAN'T DISABLED: {e}. Trying Registry Method..."
        )
        try:
            reg_path = r"SYSTEM\CurrentControlSet\Services" + "\\" + service_name
            key = reg.OpenKey(reg.HKEY_LOCAL_MACHINE, reg_path, 0, reg.KEY_SET_VALUE)
            reg.SetValueEx(
                key, "Start", 0, reg.REG_DWORD, 4
            )  # Set service start type to Disabled
            reg.CloseKey(key)
            print(f"\"{service_name}\": DISABLED SUCCESSFULLY using Registry")
        except Exception as e:
            raise Exception(
                f"[ERROR] Failed to disable {service_name} using both 'sc' and Registry: {e}"
            )


def is_service_exists(service_name):
    try:
        result = subprocess.run(
            ["sc", "query", service_name],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        return "SERVICE_NAME" in result.stdout
    except Exception as e:
        print(f"Có lỗi xảy ra khi check: {e}")
        return False
