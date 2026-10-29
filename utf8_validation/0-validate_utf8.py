#!/usr/bin/python3
"""Defines validUTF8, which checks if a list of bytes is valid UTF-8."""


def validUTF8(data):
    """Return True if data is a valid UTF-8 encoding, else return False.

    data is a list of integers, one per byte. Only the 8 least
    significant bits of each integer are used.
    """
    remaining = 0
    for number in data:
        byte = number & 0xFF
        if remaining == 0:
            if byte >> 7 == 0b0:
                continue
            elif byte >> 5 == 0b110:
                remaining = 1
            elif byte >> 4 == 0b1110:
                remaining = 2
            elif byte >> 3 == 0b11110:
                remaining = 3
            else:
                return False
        else:
            if byte >> 6 != 0b10:
                return False
            remaining -= 1
    return remaining == 0
