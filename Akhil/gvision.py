# This is a billed project under Google Cloud suite. Its free for first 1000 pages/month

import os, io
from google.cloud import vision
import pandas as pd
#from google.cloud.vision import types

os.environ['GOOGLE_APPLICATION_CREDENTIALS']= #project json api key
client = vision.ImageAnnotatorClient()

FILE_NAME = #File name
FOLDER_PATH = #Folder Path

with io.open(os.path.join(FOLDER_PATH,FILE_NAME),'rb') as image_file :
    content = image_file.read()

image = vision.Image(content=content)
response = client.text_detection(image=image)
print(response)