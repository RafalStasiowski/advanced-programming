import base64

import cv2
import numpy as np
from fastapi import File


def invert(file: File):
    image = cv2.imread(file.filename)
    image = ~image
    return image
