# 🕵️‍♀️ Image Steganography using OpenCV and Streamlit

Steganography is the **art of concealing the existence of communication** by hiding information inside other non-secret media.
This project demonstrates **Image Steganography** using the **Least Significant Bit (LSB)** method with a simple **Streamlit GUI** that allows users to **encode (hide)** and **decode (extract)** text messages within image files.

---

## 🎯 Project Overview

A simple GUI-based steganography tool that allows users to:

* Hide text data inside images using the **LSB method**.
* Extract hidden messages from stego images.
* Visualize both cover and stego images.
* Download the encoded image directly through the web interface.

---

## 🧱 Types of Steganography

1. **Image Steganography** — Hiding data inside images (used in this project).
2. **Audio Steganography** — Hiding data within audio signals.
3. **Video Steganography** — Embedding data inside video frames.

---

## 🌟 Features

* 🔐 **Encode (Hide)** secret text messages inside images (PNG, JPG, BMP).
* 🔓 **Decode (Extract)** hidden messages from stego images.
* 🧠 Automatically checks the image’s capacity before encoding.
* 💬 Displays image capacity and message size in bits.
* 📥 Download stego images directly after encoding.
* ⚡ Clean, interactive **Streamlit** interface — no command-line input needed.

---

## 🧰 Technologies Used

* **Python 3.x**
* **OpenCV (cv2)**
* **NumPy**
* **Pillow (PIL)**
* **Streamlit**

---

## ⚙️ Requirements

Install the following dependencies before running the project:

```bash
pip install streamlit opencv-python pillow numpy
```

Or using the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>
```

### 2️⃣ Run the Streamlit App

```bash
streamlit run app.py
```

Then open the link shown in the terminal (usually `http://localhost:8501`) in your browser.

---

## 🔍 What Is Steganography

Steganography hides secret data inside ordinary media (like images, audio, or video) to prevent detection.
In this project, we use **Image Steganography**, specifically the **Least Significant Bit (LSB) method**, to embed data into image pixels with no visible change.

---

## 🧩 Least Significant Bit (LSB) Technique

Each pixel in an image contains **Red, Green, and Blue (RGB)** components, each represented by **8 bits** (0–255).
The **LSB** technique replaces the last bit of each color channel with a bit from the secret message.

* If the secret bit is `1` → pixel value becomes **odd**.
* If the secret bit is `0` → pixel value becomes **even**.

This modification is subtle and **imperceptible** to the human eye.

> 💡 The fewer bits changed, the harder it is to detect any alteration.

---

## ⚙️ How It Works

### 🔐 **Encoding Process**

1. The secret text message is converted into **binary** (using ASCII values).
2. Each bit of the binary message is embedded into the **LSBs** of image pixels.
3. A **delimiter** (`1111111111111110`) marks the end of the message.
4. The modified image is saved as the **stego image**.

### 🔓 **Decoding Process**

1. Read the **LSBs** from each image pixel sequentially.
2. Stop reading when the **delimiter** is encountered.
3. Convert the extracted binary sequence back into readable text.

---

## 🖼️ Understanding a Digital Image

A **digital image** is a 2D matrix of **pixels**, each containing RGB color intensity values between 0–255.

| Channel | Bit Range | Description              |
| ------- | --------- | ------------------------ |
| Red     | 0–255     | Intensity of red color   |
| Green   | 0–255     | Intensity of green color |
| Blue    | 0–255     | Intensity of blue color  |

Each pixel = 3 color values × 8 bits = **24 bits total per pixel**.
Changing the **least significant bit** (rightmost bit) alters the color by less than 1% — ideal for hidden data embedding.

---

## 🧠 Example

Suppose a pixel has:

```
R = 11001010
G = 01101100
B = 11110010
```

To hide a message bit `1`, the LSBs are modified:

```
R = 11001011
G = 01101101
B = 11110011
```

The visual difference is negligible, but the data is successfully embedded.

---

## 🖼️ Hiding an Image Inside Another

This same LSB concept can hide **an image within another image**:
Each pixel of the secret image replaces the LSBs of the cover image’s pixels.

* More LSBs used = More data hidden.
* But higher distortion risk — so balance capacity and image quality.

---

## 🧪 Example Workflow

1. Upload a **cover image**.
2. Enter your **secret message**.
3. Click “🔐 Encode Message”.
4. Download the **stego image**.
5. Switch to “🔓 Decode Message” mode and upload the stego image to view the hidden text.

---
