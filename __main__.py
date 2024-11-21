import sys
import logging

__versions__ = [
    3.8,
    3.9,
    3.10,
    3.11
]

if sys.version_info <= 3.8:
    logging.error(msg='Python version is too old, use a newer one.')
elif NameError:
    logging.error(msg="This is an issue with python.")
elif sys.getwindowsversion <= 8.1:
    logging.error(msg="This library does not support windows 8.1 or lower.")