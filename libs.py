import subprocess
import logging

parameters = [
    'install',
    'uninstall',
]

def pip(params, lib):
    if params == 'install':
        print(f"Installing {lib}.")
        subprocess.call(f"pip install {lib}")
    elif params == 'uninstall':
        print(f"Uninstalling {lib}.")
        subprocess.call(f"pip uninstall {lib}")
    elif lib == None:
        logging.error(msg='Missing parameter "lib".')
    elif params == None:
        logging.eror(msg='Missing parameter "params".')
    elif params not in parameters:
        logging.error(msg=f'Invalid parameter "{params}".')