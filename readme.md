# Py to Exe
pyinstaller --clean --optimize=2 --noconfirm --onefile --name="DisableServices" disable_useless_services.py
pyinstaller --clean --optimize=2 --noconfirm --onedir --name="DisableServices1" disable_useless_services.py
pyinstaller DisableServices.spec