#! /usr/bin/env python
import os
import datetime
from pyzbar.pyzbar import decode
from PIL import Image

timestamp = str(datetime.datetime.now().microsecond)
filetype = ".png"
filename = timestamp + filetype

os.system("screencapture -i " + filename)
result = decode(Image.open(filename))

if len(result) == 1:
  os.system("open -a /Applications/Safari.app " + result[0].data)
elif len(result) > 1:
  print("Too many.")
  for i in result:
    print(i.data)

try:
  os.remove(filename)
except OSError:
  print("Nothing.")
