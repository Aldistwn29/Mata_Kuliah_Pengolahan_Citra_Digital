import imageio.v3 as img
import numpy as np
import matplotlib.pyplot as plt

def Translasi(image, shiftX, shiftY):
    imgTranslasi = np.roll(image, shift=shiftY, axis=0) #Geser vertiskal
    imgTranslasi = np.roll(image, shift=shiftX, axis=1) #Geser horizontal

    # Mengisi bagian yang kosong dengan warna hitam
    if shiftY > 0:
        imgTranslasi[:shiftY, :] = 0 # Bagian atas jika geser ke bawah
    elif shiftY < 0:
        imgTranslasi[shiftY:, :] = 0 # Bagian bawah jika geser ke atas
    if shiftX > 0:
        imgTranslasi[:, :shiftX] = 0 # Bagian kiri jika geser ke kekanan
    elif shiftX < 0:
        imgTranslasi[:, shiftX:] = 0 # Bagian kanan jika geser ke kiri

    return imgTranslasi

image = img.imread("labubu.jpeg")
imgTranslasi = Translasi(image, shiftX=50, shiftY=-300)

plt.figure(figsize=(10,6))
plt.subplot(2,1,1)
plt.imshow(image)

plt.subplot(2,1,2)
plt.imshow(imgTranslasi)

plt.show()