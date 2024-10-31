import numpy as np
import matplotlib.pyplot as plt
import imageio as img

path = "labubu.jpeg"
image = img.imread(path)

height, width = image.shape[:2]
horizontal = np.flip(image, axis=1)
vertical = np.flip(image, axis=0)
mirror_image = np.flip(image, axis=(0, 1))

plt.figure(figsize=(15,5))
plt.subplot(1,4,1)
plt.imshow(image)
plt.title("Original")

plt.subplot(1,4,2)
plt.imshow(horizontal)
plt.title("Horizontal Mirror")

plt.subplot(1,4,3)
plt.imshow(vertical)
plt.title("Vertical mirror")

plt.subplot(1,4,4)
plt.imshow(mirror_image)
plt.title("Horizontal and Vertical Mirror")

img.imwrite("miror_labubu.jpg",mirror_image)

plt.show()