import imageio as img
import numpy as np
import matplotlib.pyplot as plt

img = img.imread("D:/aldisetiawan/Semester 5/Pengolahan Citra Digital/Deteksi Tepi/lena.jpg", mode='F')

robertx = np.array([
    [1,0],
    [0,-1]
])

roberty = np.array([
    [0,1],
    [-1,0]
])

imgPad = np.pad(img, pad_width=1, mode='constant', constant_values=0)

Gx = np.zeros_like(img)
Gy = np.zeros_like(img)

for y in range(1, imgPad.shape[0]-1):
    for x in range(1, imgPad.shape[1]-1):
        region = imgPad[y-1:y+1, x-1:x+1]
        Gx[y-1,x-1] = (region * robertx).sum()
        Gy[y-1,x-1] = (region * roberty).sum()

G = np.sqrt(Gx**2 + Gy**2)
G = (G / G.max()) * 255
G = np.clip(G,0,255)
G = G.astype(np.uint8)

plt.figure(figsize=(10,10))
plt.subplot(2,2,1)
plt.imshow(img, cmap='gray')
plt.title('Gambar Original')

plt.subplot(2,2,2)
plt.imshow(Gx, cmap='gray')
plt.title('Gradien Gx (Robert x)')

plt.subplot(2,2,3)
plt.imshow(Gy, cmap='gray')
plt.title('Gradien Gy (Robert y)')

plt.subplot(2,2,4)
plt.imshow(G, cmap='gray')
plt.title('Magnitudo gradien G (Robert)')

plt.tight_layout()
plt.show()