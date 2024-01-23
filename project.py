import cv2

# Import the OpenCV library, widely used for computer image processing.

import easyocr

# Import the EasyOCR library; OCR is used for recognizing and extracting text from images.

import matplotlib.pyplot as plt

# Import the Matplotlib library, specifically the pyplot module used for plotting and displaying images.

import numpy as np

# Import the NumPy library, commonly used for numerical operations.

# Read the image from the computer.
image_path = "123.jpg"
# Here, the image is stored in the project folder, but it can be anywhere on the local machine using the correct path.

# Use the cv2 function imread to read the image and store it in the img variable.
img = cv2.imread(image_path)

# Use EasyOCR to set the reading language to English.
reader = easyocr.Reader(["en"], gpu=False)
# Here, GPU is set to false as we don't require GPU acceleration.

# Use the EasyOCR reader function to extract text from img and save it in text_.
text_ = reader.readtext(img)

# Set the limit of the confidence score to display text.
threshold = 0.25
# A confidence score below this limit will not be displayed.

# Core function to process and visualize detected text.
for t_, t in enumerate(text_):
    print(t)

    bbox, text, score = t

    if score > threshold:
        cv2.rectangle(img, bbox[0], bbox[2], (0, 255, 0), 5)
        # Draw a rectangle on the image using OpenCV.

        cv2.putText(img, text, bbox[0], cv2.FONT_HERSHEY_COMPLEX, 0.65, (255, 0, 0), 2)
        # Place text on the image using OpenCV.

# Convert the BGR format of OpenCV to RGB for Matplotlib.
rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Display the original image.
plt.subplot(1, 2, 1)
plt.title("Original Image")
plt.imshow(rgb_img)
plt.axis("off")

# Create a copy of the image for further processing.
processed_img = img.copy()

# Apply a grayscale transformation to the image.
gray_img = cv2.cvtColor(processed_img, cv2.COLOR_BGR2GRAY)

# Display the grayscale image.
plt.subplot(1, 2, 2)
plt.title("Grayscale Image")
plt.imshow(gray_img, cmap="gray")
plt.axis("off")

# Display the processed image.
plt.show()
