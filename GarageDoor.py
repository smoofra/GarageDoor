#!/usr/bin/env python3

import os
import sys

if sys.platform == "darwin":
    os.environ['DYLD_LIBRARY_PATH'] = os.environ.get('DYLD_LIBRARY_PATH', '') + ':/data/homebrew/lib'

import usb.core
import usb.util

dev = usb.core.find(idVendor=0x16c0, idProduct=0x05dc)

if ( dev is None or
     usb.util.get_string(dev, dev.iManufacturer) != 'larry@elder-gods.org' or
     usb.util.get_string(dev, dev.iProduct) != 'GarageDoor' ):
    print("device not found")
    sys.exit(1)
     
print("device found")    





