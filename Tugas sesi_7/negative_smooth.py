import imageio
import numpy as np
from scipy import ndimage
import matplotlib.pyplot as plt

image = imageio.imread('tumor_otak.jpg')
img_negative = 255 - image
smoothed_image = ndimage.uniform_filter(img_negative, size=3)

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Image original')
plt.axis('off')

# gambar negatif
plt.subplot(1, 2, 2)
plt.imshow(smoothed_image, cmap='gray')
plt.title('image negative')
plt.axis('off')

plt.tight_layout()
plt.show()

print(image.shape) 
