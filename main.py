from image_utils import load_image, edge_detection
from PIL import Image
from skimage.filters import median
from skimage.morphology import ball

image = load_image('lena.jpg')
image = median(image, ball(3))
edge = edge_detection(image)
edge_binary = edge > 50
image = Image.fromarray(array)
image.save('lena_edges.png')
