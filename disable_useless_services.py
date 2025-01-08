from Config.utils import run_as_admin, disable_service, is_service_exists
import json
import os


def get_list_useless_services(json_path: str) -> list:
    with open(json_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data["useless_services"]


if __name__ == "__main__":
    run_as_admin()

    try:
        json_path = "useless_services.json"
        if os.path.exists(json_path):
            list_useless_services = get_list_useless_services(json_path)
            for service_name in list_useless_services:
                if is_service_exists(service_name):
                    disable_service(service_name)
                else:
                    print(f"Can't find: {service_name}")
        else:
            print(f"File <{json_path}> not found")
    finally:
        os.system("pause")
