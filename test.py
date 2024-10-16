import matplotlib.pyplot as plt
import numpy as np
import imageio 
import cv2

# memanggil gambar
path_gambar = 'C:/Users/Muhammad Sheva/Documents/aldi/wayang.jpeg'
img = imageio.imread(path_gambar )

# mengubuh ke grayscale
grayscale = np.dot(img[...,:3],[0.2989, 0.5870, 0.1140])
grayscale = np.clip(grayscale, 0, 255).astype(np.uint8)

histogram, bins = np.histogram(grayscale, bins=256, range=(0, 256))

total_pixels = np.sum(histogram)

domaint_intensity = np.argmax(histogram)
domaint_pixel_count = histogram[domaint_intensity]

print(f'jumlah pixel: {total_pixels}')
print(f'Intensitas Domain: {domaint_intensity} dengan {domaint_intensity} piksel')

# Menampilkan gambar
plt.figure(figsize=(16, 5))
plt.subplot(1,3,1)
plt.imshow(img)
plt.title('Sebelum')

plt.subplot(1,3,2)
plt.imshow(grayscale, cmap='gray')
plt.title('Sesudah')

plt.subplot(1,3,3)
plt.bar(range(256), histogram, width=1, color='gray')
plt.title('Histogram pada grayscale')
plt.xlabel('Intensitas pixel')
plt.ylabel('Frekuensi')

plt.annotate(f'Intensitas domain: {domaint_intensity}\nJumlah piksel: {domaint_pixel_count}',
             xy=(domaint_intensity, domaint_pixel_count),
             xytext=(domaint_intensity + 10, domaint_pixel_count + 1000),
             arrowprops=dict(facecolor='red', shrink=0.05))

plt.tight_layout()
plt.show()
