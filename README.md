## OCR Text Detection using OpenCV and EasyOCR

This Python script demonstrates Optical Character Recognition (OCR) using OpenCV and EasyOCR libraries to extract and visualize text from an image.

### Dependencies
- **OpenCV:** Widely used for computer image processing.
- **EasyOCR:** Library for recognizing and extracting text from images.
- **Matplotlib:** Used for plotting and displaying images.
- **NumPy:** Commonly used for numerical operations.

### Usage
1. Import the necessary libraries: OpenCV, EasyOCR, Matplotlib, and NumPy.
2. Read an image using OpenCV's imread function.
3. Set the language for OCR (English in this case) using EasyOCR.
4. Extract text from the image and visualize it with confidence score filtering.
5. Display the original and processed images using Matplotlib.

### Code Execution
```python
# **Clone the Repository:**
   ```bash
   git clone 'https://github.com/Yrk-Yashraj/Image-Text-Detection.git'
# Ensure you have the required libraries installed (cv2, easyocr, matplotlib, numpy).
# Adjust the image path accordingly.

# Example:
image_path = "your_image.jpg"
img = cv2.imread(image_path)
# ...
# Execute the script to perform OCR text detection.

