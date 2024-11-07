import imageio
import numpy as np
from scipy import ndimage
import matplotlib.pyplot as plt

 # Baca gambar
image = imageio.v3.imread("tumor_otak.jpg", pilmode='L')

# Membuat histogram dari gambar
hist, bins = np.histogram(image.flatten(), bins=256, range=[0, 256])

# Hitung CDF
cdf = hist.cumsum()
cdf_normalized = cdf * cdf.max() / cdf.max()

# Menerapkan histogram equalization
cdf_m = np.ma.masked_equal(cdf, 0)
cdf_m = (cdf_m - cdf_m.min()) * 255 / (cdf_m.max() - cdf_m.min())
cdf = np.ma.filled(cdf_m, 0).astype('uint8')
image_equalized = cdf[image]

# Menghaluskan Gambar 
smoothed_image = ndimage.uniform_filter(image_equalized, size=3)

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Image original')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(smoothed_image, cmap='gray')
plt.title('image negative')
plt.axis('off')

plt.tight_layout()
plt.show()


