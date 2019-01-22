#! /usr/bin/env python
import os
import datetime
from pyzbar.pyzbar import decode
from PIL import Image

# baidu ocr api
from aip import AipOcr
import pyperclip

APP_ID = '******'
API_KEY = '******'
SECRET_KEY = '******'

options = {}
options["language_type"] = "CHN_ENG"
options["detect_direction"] = "false"
options["detect_language"] = "true"
options["probability"] = "false"

def get_file_content(filePath):
  with open(filePath, 'rb') as fp:
    return fp.read()

timestamp = str(datetime.datetime.now().microsecond)
filetype = ".png"
filename = timestamp + filetype

os.system("screencapture -i " + filename)

# qr
try:
  result = decode(Image.open(filename))
except IOError:
  pass
else:
  if len(result) >= 1:
    for i in result:
      os.system("open -a /Applications/Safari.app " + i.data)

  # ocr
  else:
    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
    image = get_file_content(filename)
    result = client.basicGeneral(image, options)
    result_str = ""
    for i in range(result["words_result_num"]):
      result_str = result_str + result["words_result"][i]["words"]
    pyperclip.copy(result_str)

  try:
    os.remove(filename)
  except OSError:
    pass
