from scipy import ndimage
import imageio
import numpy as np
import matplotlib.pyplot as plt

image = imageio.imread('tumor_otak.jpg')
gray_image = np.array(image)
smoothed_image = ndimage.gaussian_filter(gray_image, sigma=1)

# fungsi peroses equalization
def hist_equalization(image):
    hist, bins = np.histogram(image.flatten(), bins=256, range=[0, 256])
    cdf = hist.cumsum()
    cdf_normalized = cdf * 255 / cdf[-1]
    equalization_image = np.interp(image.flatten(), bins[:-1], cdf_normalized)
    return equalization_image.reshape(image.shape).astype('uint8')

# equalization histogram
image_equalization = hist_equalization(smoothed_image)

# menyimpan gambar
imageio.imwrite('image_orignal.jpg', gray_image)
imageio.imwrite('image_smoothed.jpg', smoothed_image)
imageio.imwrite('image_equalization.jpg', image_equalization)

# plot hasil
plt.figure(figsize=(10, 5))
plt.subplot(2, 3, 1)
plt.imshow(gray_image, cmap='gray')
plt.title('original')
plt.axis('off')

plt.subplot(2, 3, 4)
plt.hist(gray_image.ravel(), bins=50, range=(0, 256), color='b')
plt.title('Histogram gambar asli')
plt.xlabel('Nilai pixel')
plt.ylabel('frekuensi')

plt.subplot(2, 3, 2)
plt.imshow(smoothed_image, cmap='gray')
plt.title('Gambar hasil smoothed')
plt.axis('off')

plt.subplot(2, 3, 5)
plt.hist(smoothed_image.ravel(), bins=50, range=(0, 256), color='b')
plt.title('Histogram Gambar Smoothed')
plt.xlabel('Nilai pixel')
plt.ylabel('frekuensi')

plt.subplot(2, 3, 3)
plt.imshow(image_equalization, cmap='gray')
plt.title('Gambar hasil ekualisasi')
plt.axis('off')

plt.subplot(2, 3, 6)
plt.hist(image_equalization.ravel(), bins=50, range=(0, 256), color='b')
plt.title('Histogram Gambar Equalization')
plt.xlabel('Nilai pixel')
plt.ylabel('frekuensi')

plt.tight_layout()
plt.show()

