
import urllib.request
import bz2, wget, os

url = 'http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2'

filename = wget.download(url)

print("Uncompressing...")
zipfile = bz2.BZ2File(filename)
data = zipfile.read() # get the decompressed data
zipfile.close()

newfile = filename[:-4] # assuming the filepath ends with .bz2
open(newfile, 'wb').write(data) # write a uncompressed file

print("cleaning up")
os.remove(filename)

print("done")
