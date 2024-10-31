import matplotlib.pyplot as plt
import numpy as np
import imageio as image

def brightness(image, factor):
    img_bright = image.astype(np.float32)
    img_bright += factor
    img_bright = np.clip(img_bright, 0, 255)
    return img_bright.astype(np.uint8)

image_path = 'D://aldisetiawan//Semester 5//Pengolahan Citra Digital//image_pemandangan.jpeg'
image = image.imread(image_path)

img_bright = brightness(image, 50)

plt.figure(figsize=(10,10))
plt.subplot(1,2,1)
plt.imshow(image)

plt.subplot(1,2,2)
plt.imshow(img_bright)

plt.show()

