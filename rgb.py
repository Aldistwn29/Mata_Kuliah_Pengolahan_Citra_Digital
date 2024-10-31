import numpy as np
import imageio.v3 as img

image_path = "daun_singkong.jpeg"
image = img.imread(image_path)
if len(image.shape) < 3 or image.shape[2] != 3:
    print("Format Harus RGB")
    exit()

red = image[:,:,0]
green = image[:,:,1]
blue = image[:,:,2]

# Mengubah warna menjadi merah
image_red = np.zeros_like(image)
image_red[:,:,0] = red
img.imwrite("image_red_singkong.jpg", image_red)
print("Peroses Berhasil")

# Mengubah warna menjadi hijau
image_green = np.zeros_like(image)
image_green[:,:,1] = green
img.imwrite("image_green_singkong.jpg", image_green)
print("Peroses Berhasil")

# Mengubah warna menjadi biru
image_blue = np.zeros_like(image)
image_blue[:,:,2] = blue
img.imwrite("image_blue_singkong.jpg", image_blue)
print("Peroses Berhasil")

# print(image.shape)
# mengubah warna menjadi gray
gray = red * 0.299 + green * 0.587 + blue * 0.114
gray_rgb = np.zeros_like(image)
gray_rgb[:,:,0] = gray
gray_rgb[:,:,1] = gray
gray_rgb[:,:,2] = gray
# gray_scale = np.clip(gray, 0, 255).astype(np.uint8)
img.imwrite("image_gray_singkong.jpg", gray_rgb)
print("Peroses Berhasil")

threshold = 100
binary_image = np.where(gray > threshold, 255, 0).astype(np.uint8)
binary_rgb = np.zeros_like(image)
binary_rgb[:,:,0] = binary_image
binary_rgb[:,:,1] = binary_image
binary_rgb[:,:,2] = binary_image
img.imwrite("image_binary_singkong.jpg", binary_rgb)
print("Peroses Berhasil")
