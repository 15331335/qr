#! /usr/bin/env python
import os
import datetime
from pyzbar.pyzbar import decode
from PIL import Image

timestamp = str(datetime.datetime.now().microsecond)
filetype = ".png"
filename = timestamp + filetype

os.system("screencapture -i " + filename)

try:
  result = decode(Image.open(filename))
except IOError:
  pass
else:
  if len(result) >= 1:
    for i in result:
      os.system("open -a /Applications/Safari.app " + i.data)

  try:
    os.remove(filename)
  except OSError:
    pass
