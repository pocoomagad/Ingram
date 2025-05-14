import os
import logging

loger = logging.getLogger(__name__)

def install_depends():
    try:
        os.system("poetry update --no-dev")
    except Exception as e:
        loger.error(e)
    finally:
        os.system("poetry install --no-dev")


def install_all_depends():
    try:
        os.system("poetry update")
    except Exception as e:
        loger.error(e)
    finally:
        os.system("poetry install")