from PIL import Image
import numpy as np
from scipy.signal import convolve2d

def load_image(path):
    image = Image.open(path)
    image = np.array(image)
    return image

def edge_detection(image):
    gray = np.mean(image, axis=-1)
    dfdx = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    dfdy = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
    edge_x = convolve2d(gray, dfdx, mode='same', boundary='fill', fillvalue=0)
    edge_y = convolve2d(gray, dfdy, mode='same', boundary='fill', fillvalue=0)
    edge = np.sqrt(edge_x**2 + edge_y**2)
    return edge
