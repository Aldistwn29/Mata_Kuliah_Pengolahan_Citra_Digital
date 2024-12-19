import imageio as img
import numpy as np
import matplotlib.pyplot as plt

def localThres(image, block_size=15, c=10):
    imgPad = np.pad(image, pad_width=1, mode='constant', constant_values=0)
    threshold = np.zeros_like(image)

    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            local_area = imgPad[i:i+block_size, j:j+block_size]
            local_mean = np.mean(local_area)
            threshold[i,j] = 255 if image[i,j] > (local_mean - c) else 0
    return threshold

image = img.imread("labubu.jpeg", mode='F')
threshold_img = localThres(image)

plt.figure(figsize=(10,6))
plt.subplot(2,2,1)
plt.imshow(image, cmap='gray')

plt.subplot(2,2,2)
plt.imshow(threshold_img, cmap='gray')

plt.tight_layout()
plt.show()
