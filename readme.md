# Py to Exe
pyinstaller --clean --optimize=2 --noconfirm --onefile --name="DisableServices" disable_useless_services.py  
pyinstaller --clean --optimize=2 --noconfirm --onedir --name="DisableServices1" disable_useless_services.py  
pyinstaller --clean --noconfirm DisableServices.spec  

# In .spec
with open('DisableServices_version.txt') as version_file:
    txt_version = version_file.read().strip()

app_version_parts = txt_version.split('.')
major = int(app_version_parts[0])  # Phần chính
minor = int(app_version_parts[1])  # Phần phụ
patch = int(app_version_parts[2])  # Phần vá
patch += 1
if patch >= 20:
    patch = 0
    minor += 1
    if minor >= 20:
        minor = 0
        major += 1

app_version =f'{major}.{minor}.{patch}'
exe_name = f'DisableServices_v{app_version}'