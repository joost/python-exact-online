import base64
import os
import requests

def getFileName(path):
    return os.path.basename(path)

def encodeFileToB64(path):
    f = open(path, 'rb')
    fRead = f.read()
    fEncode = base64.encodebytes(fRead)
    fString = fEncode.decode('utf-8')
    return fString

def getUrlFileName(url):
    return url.split('/')[-1]

def encodeURLToB64(url):
    response = requests.get(url)
    attachmentB64 = base64.encodebytes(response.content).decode('utf-8')
    return attachmentB64