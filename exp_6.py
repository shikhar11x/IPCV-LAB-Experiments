# Experiment 6: Periodic noise reduction using inverse filtering and Wiener filtering.

from scipy.signal import wiener
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('input_image.jpg', 0)

if img is None:
    print("Error: 'input_image.jpg' not found.")
    exit()

# Convert to float for safe arithmetic
img_float = img.astype(np.float64)

# Add periodic (sinusoidal) noise
noise = 20 * np.sin(np.linspace(0, 50, img.shape[1]))
noise = np.tile(noise, (img.shape[0], 1))          # ✅ full image pe noise lagao
noisy = np.clip(img_float + noise, 0, 255)

# Wiener filter
wiener_img = wiener(noisy, mysize=5)               # ✅ float input → float output

# ✅ Normalize to uint8 for display
wiener_img = np.clip(wiener_img, 0, 255).astype(np.uint8)
noisy_disp = noisy.astype(np.uint8)

# Display all three
plt.figure(figsize=(12, 4))
plt.subplot(1, 3, 1)
plt.imshow(img, cmap='gray')
plt.title('Original')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(noisy_disp, cmap='gray')
plt.title('Periodic Noisy Image')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(wiener_img, cmap='gray')
plt.title('Wiener Filtered Image')
plt.axis('off')

plt.tight_layout()
plt.savefig('Output-Images/output-exp-6.png', dpi=150)
plt.show()