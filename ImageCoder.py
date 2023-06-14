import cv2
from base64 import b64encode, b64decode
import os
import base64
import io
from matplotlib import pyplot as plt
import matplotlib.image as mpimg

def read_image(path):
    img = cv2.imread(path)
    # либо оставить jpg
    retval, buffer = cv2.imencode(os.path.splitext(path)[1], img)
    b64img = b64encode(buffer).decode("utf-8")
    return b64img


def save_image_from_base64(base64_string, output_path):
    with open(output_path, "wb") as file:
        file.write(b64decode(base64_string))


def show_b64_image(b64_image):
    i = base64.b64decode(b64_image)
    i = io.BytesIO(i)
    i = mpimg.imread(i, format='JPG')

    plt.imshow(i, interpolation='nearest')
    plt.show()
