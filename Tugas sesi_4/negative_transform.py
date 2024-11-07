import cv2 
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('tumor_otak.jpg')
img_neg =  255 - image

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(image)
plt.title('original')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(img_neg)
plt.title('negative Transfrom')
plt.axis('off')

plt.tight_layout()
plt.show()