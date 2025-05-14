import os

def install_depends():
    try:
        os.system("poetry install")
    except Exception as e:
        os.system("poetry update")

        