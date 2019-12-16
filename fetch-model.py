#!./env/python

import urllib.request
import bz2, wget, os

url = 'http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2'

print("Downloading %s ..."%url,flush=True)
filename = wget.download(url)

print("Uncompressing...",flush=True)
zipfile = bz2.BZ2File(filename)
data = zipfile.read() # get the decompressed data
zipfile.close()

newfile = filename[:-4] # assuming the filepath ends with .bz2
open(newfile, 'wb').write(data) # write a uncompressed file

print("Cleaning up...",flush=True)
os.remove(filename)

print("done")
