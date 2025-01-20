import subprocess
import json
import os


def open_json(unused_srv_json: str):
    with open(unused_srv_json, "r") as file:
        return json.load(file)


def check_service_exists(service_name: str):
    try:
        # result =
        subprocess.run(
            ["sc", "query", service_name], capture_output=True, text=True, check=True
        )
        return True
    except subprocess.CalledProcessError as err:
        print(err)
        return False


def change_status_to_disable(service_name: str):
    try:
        subprocess.run(
            ["sc", "config", service_name, "start=", "disabled"],
            check=True,
            stdout=subprocess.DEVNULL,  # Không in thông báo khi thành công
            stderr=subprocess.PIPE,  # Đảm bảo chỉ in lỗi nếu có
        )
        print(f"{srv} has been disabled successfully")
    except subprocess.CalledProcessError as err:
        print(err)


if __name__ == "__main__":
    # unused_srv_json = "unused_services.json"
    unused_srv_json = r"DisableServices\unused_services.json"
    try:
        if unused_srv_list := open_json(unused_srv_json):
            for srv in unused_srv_list:
                if check_service_exists(srv):
                    change_status_to_disable(srv)
    except Exception as e:
        print(f"Exception: {e}")
    finally:
        os.system("pause")
