#!/usr/bin/python3
"""Module UTF-8 Validation"""


def validUTF8(data):
    """method that determines if a given data set
    represents a valid UTF-8 encoding"""

    try:
        arr = [i & 255 for i in data]
        bytes(arr).decode("UTF-8")
        return True
    except Exception:
        return False
