#!/usr/bin/env python3

import os
import sys
import time
import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--click', action='store_true')
parser.add_argument('--verbose', '-v', action='store_true')
args = parser.parse_args()

if not args.click:
    parser.error("huh?")

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
if args.verbose:
    print(dev)
    print("device found")
    print("on");

dev.ctrl_transfer(0x40, 0, 0, 0, b'1')

time.sleep(1)

if args.verbose:
    print("off");

dev.ctrl_transfer(0x40, 0, 0, 0, b'0')

print("clicked")

