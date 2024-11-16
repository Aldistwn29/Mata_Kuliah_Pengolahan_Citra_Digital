import numpy as np
import cv2
import matplotlib.pyplot as plt


# Fungsi high pass filter
def high_pass_filter(image):
    karnel = np.array([[0, -1, 0],
                      [-1, 4, -1],
                      [0, -1, 0]])
    return cv2.filter2D(image, -1, karnel)

# Fungsi low pass filter
def low_pass_filter(image):
    return cv2.GaussianBlur(image, (5, 5), 0)

# Fungsi hight boost
def high_boost(image, boost_factor=1.5):
    high_pass = high_pass_filter(image)
    bosst_image = cv2.addWeighted(image, boost_factor, high_pass, 1, 0)
    return bosst_image

# Fungsi untuk menapilkan gambar
def show_image(images, titles, figsize=(18, 12)):
    rows = (len(images) + 3) // 4
    plt.figure(figsize=figsize)
    for i,(img, title) in enumerate(zip(images, titles)):
        plt.subplot(rows, 4, i + 1)
        if len(img.shape) == 3:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        plt.imshow(img, cmap='gray' if len(img.shape) == 2 else None)
        plt.title(title)
    plt.tight_layout()
    plt.show()

image_color = cv2.imread('paprika.jpg')
image_gray = cv2.cvtColor(image_color, cv2.COLOR_BGR2GRAY)
# Menggunakan filter pada gambar berwarna
low_pass_filtered = low_pass_filter(image_color)
high_pass_filtered = high_pass_filter(image_color)
high_boosted = high_boost(image_color)

# Menerapkan filter pada gambar berwarna gray
low_pass_filtered_gray = low_pass_filter(image_gray)
high_pass_filtered_gray = high_pass_filter(image_gray)
high_boosted_gray = high_boost(image_gray)

# menampilkan gambar
show_image(
    images=[image_color, low_pass_filtered, high_pass_filtered, high_boosted,
            image_gray, low_pass_filtered_gray, high_pass_filtered_gray, high_boosted_gray],
    titles=['Gambar asil berwarn', 'loww pass berwarna', 'hight pas berwarna', 'hight boost berwarna',
            'Gambar asli gray', 'loww pass gray', 'hight pass gray', 'hight bosst gray'],
    figsize=(18, 6)
)
