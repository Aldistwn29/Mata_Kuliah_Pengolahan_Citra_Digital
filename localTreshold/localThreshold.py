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

def besic_treshold(image, lv=150):
    threshold = np.where(image > lv, 255, 0)
    return threshold.astype(np.uint8)


image = img.imread("labubu.jpeg", mode='F')
besic_img = besic_treshold(image)
threshold_img = localThres(image)


plt.figure(figsize=(10,6))
plt.subplot(2,2,1)
plt.title('original image')
plt.imshow(image, cmap='gray')

plt.subplot(2,2,2)
plt.title('besic treshold')
plt.imshow(besic_img, cmap='gray')

plt.subplot(2,2,3)
plt.title('local treshold')
plt.imshow(threshold_img , cmap='gray')

plt.tight_layout()
plt.show()
