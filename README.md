# 🎨 Color Detection Project

## 📝 Overview

This repository contains a Python script for detecting and identifying colors in an image using OpenCV and pandas. The script allows users to click on an image to detect the color at that point and find the closest matching color name from a predefined dataset.

---

## ✨ Features

- 🖱️ Detects RGB values of a clicked point in an image.  
- 🔍 Matches the detected color to the closest known color name using a CSV dataset.  
- 🖼️ Displays the color name and RGB values on the image with a colored rectangle.

---

## 🛠️ Requirements

- 🐍 Python 3.x  
- 📸 OpenCV (`cv2`)  
- 📊 pandas  

Install the required packages using pip:

```bash
pip install opencv-python pandas
```

---

## 📂 Files

- `color_detection.py`: The main Python script for color detection.  
- `colors.csv`: A dataset containing color names, hex codes, and RGB values for matching.

---

## 🚀 Usage

1. 📥 Place your image file as `image.png` in the same directory as the script.  
2. 📋 Ensure `colors.csv` is in the same directory.  
3. ▶️ Run the script:

```bash
python color_detection.py
```

4. 🖱️ Double-click on the displayed image to select a point.  
   The script will show the closest color name and RGB values.

---

## 🔧 How It Works

- The script loads an image and a CSV file with color data.
- A mouse callback function captures the RGB values of the clicked point.
- The closest color name is determined by calculating the distance in RGB space.
- The result is displayed on the image with a colored rectangle and text.

---

## 📸 Screenshots

Below is an example of the color detection output.  


![image](https://github.com/user-attachments/assets/80a0a407-85da-450e-9767-cb24722e67a4)

---

## 📊 Dataset

The `colors.csv` file contains a comprehensive list of colors with their names, hex codes, and RGB values, sourced from various standards and palettes.

---

## 🤝 Contributing

Feel free to fork this repository, make improvements, and submit pull requests.  
Issues and suggestions are welcome! 🌟

---

## 📜 License

This project is licensed under the MIT License.  

