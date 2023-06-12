import cv2
from base64 import b64encode, b64decode
import os
def readImage(path):
    img = cv2.imread(path)
    # либо оставить jpg
    retval, buffer = cv2.imencode(os.path.splitext(path)[1], img)
    b64img = b64encode(buffer).decode("utf-8")
    return b64img

def save_image_from_base64(base64_string, output_path):
    with open(output_path, "wb") as file:
        file.write(b64decode(base64_string))
