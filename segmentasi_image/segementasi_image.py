import numpy as np
import matplotlib.pyplot as plt
from imageio import imread
from scipy.ndimage import sobel

# Load gambar
def load_image(image_path):
    image = imread(image_path, mode='F')
    return image

# Menerapkan deteksi sobel
def apply_sobel(image):
    sobel_x = sobel(image, axis=0)
    sobel_y = sobel(image, axis=1)
    sobel_magnitude = np.hypot(sobel_x, sobel_y)
    return sobel_magnitude

# treshoald image
def treshoald_image(image, treshoald):
    binary_image = image > treshoald
    return binary_image

def analyze_sobel_value(sobel_edege):
    min_val = np.min(sobel_edge)
    max_val = np.max(sobel_edge)
    mean_val = np.mean(sobel_edge)
    print(f"Min {min_val} Max {max_val} Mean {mean_val}")
    return mean_val

# Visualisasi
def analyze_visualisasi(original, sobel_edge, treshoalded):
    plt.figure(figsize=(15, 15))

    plt.subplot(2, 4, 1)
    plt.title("Original Image")
    plt.imshow(original, cmap='gray')
    plt.axis('off')

    plt.subplot(2, 4, 2)
    plt.title("Sobel Edge Detection")
    plt.imshow(sobel_edge, cmap='gray')
    plt.axis('off')

    plt.subplot(2, 4, 3)
    plt.title("Threshoald Image")
    plt.imshow(treshoalded, cmap='gray')
    plt.axis('off')

    plt.subplot(2, 4, 4)
    plt.title('Histogram of Sobel Intensitas')
    plt.hist(sobel_edge.ravel(), bins=256, color='blue', alpha=0.7)
    plt.xlabel('Intensitas Value')
    plt.ylabel('Frekuensi')

    plt.tight_layout()
    plt.show()


image_path = 'lena.jpg'
treshoald_value = 73.33

# menampilkan gambar dan perosesnya
original = load_image(image_path)
sobel_edge = apply_sobel(original)
# treshoald_value = analyze_sobel_value(sobel_edge) * 0.6
treshoalded_image = treshoald_image(sobel_edge, treshoald_value)


# Menapilkan visulisai
analyze_visualisasi(original, sobel_edge, treshoalded_image)
# plot_histogram(sobel_edge)
