from Config.utils import run_as_admin, disable_service
import json
import os


def get_list_useless_services(json_path="useless_services.json"):
    with open(json_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data["useless_services"]


if __name__ == "__main__":
    run_as_admin()

    try:
        list_useless_services = get_list_useless_services()
        for service_name in list_useless_services:
            disable_service(service_name)
    finally:
        os.system("pause")
