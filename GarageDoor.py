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


    
dev.set_configuration()
print(dev)
#dev.write(0x81, b'x')

dev.ctrl_transfer(0xc0, 0, 0, 0, 'x')

     
print("device found")    





