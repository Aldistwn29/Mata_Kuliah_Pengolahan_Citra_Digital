import matplotlib.pyplot as plt
import numpy as np
import imageio as image

# path gambar
image_path = 'D://aldisetiawan//Semester 5//Pengolahan Citra Digital//image_negatif.jpeg'
# gambar negatif
img_negatif = image.imread(image_path)
r_neg = img_negatif[:,:,0]

hist_neg, rbins = np.histogram(r_neg, bins=256, range=[0,256])

# gambar positif
img_positif =  255 - img_negatif
r_pos = img_positif[:,:,0]
hist_pos, rbins = np.histogram(r_pos, bins=256, range=[0,256])

# Menamapilkan gambar
plt.figure(figsize=(10,10))
plt.subplot(2,2,1)
plt.imshow(img_negatif)

plt.subplot(2,2,2)
plt.imshow(img_positif)

plt.subplot(2,2,3)
plt.plot(hist_neg)

plt.subplot(2,2,4)
plt.plot(hist_pos)

plt.show()
print(img_negatif.shape)
