import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("tumor_otak.jpg")

# menentukan nilai penambahan untuk kecerahan
brigheness = -100
brigheness_2 = 100

# mencerahkan citra dengan menambahkan nilai konstanta
brightened_img = cv2.convertScaleAbs(image, alpha=1, beta=brigheness)
brightened_img_2 = cv2.convertScaleAbs(image, alpha=1, beta=brigheness_2)

# menampilkan hasil
plt.figure(figsize=(10, 5))

plt.subplot(1, 3, 1)
plt.imshow(image)
plt.title('Image original')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(brightened_img)
plt.title('image brighter 1')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(brightened_img_2)
plt.title('image brighter 2')
plt.axis('off')

plt.tight_layout()
plt.show()