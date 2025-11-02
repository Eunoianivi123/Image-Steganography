Image Steganography using OpenCV and Streamlit
Steganography is the art of hiding the fact that communication is taking place, by hiding information in other information. For hiding secret information in images, there exists a large variety of steganography techniques some are more complex than others and all of them have respective strong and weak points. Different applications may require absolute invisibility of the secret information, while others require a large secret message to be hidden.
TYPES OF STEGANOGRAPHY

STEGANOGRAPHY IN IMAGE
STEGANOGRAPHY IN AUDIO
STEGANOGRAPHY IN VIDEO

A Simple GUI Based Steganography (LSB-Method) Tool For Hide-Unhide (Encode-Decode) Text From Image File. 

Features

🔐 Encode (Hide) secret text messages inside images (PNG, JPG, BMP).

🔓 Decode (Extract) hidden messages from stego images.

🧠 Automatically checks the image’s capacity before encoding.

💬 Displays image capacity and message size in bits.

📥 Option to download the stego image after encoding.

⚡ User-friendly Streamlit interface — no complex commands needed.

Technologies Used

Python 3.x

OpenCV (cv2)

NumPy

Pillow (PIL)

Streamlit

Requirements

opencv-python-headless

numpy

streamlit

Pillow

🚀 Getting Started
1️⃣ Clone the Repository
git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>

2️⃣ Install Dependencies

Make sure you have Python installed (3.8+ recommended). Then install required libraries:

pip install -r requirements.txt

If you don’t have a requirements.txt, you can manually install them:

pip install streamlit opencv-python pillow numpy

▶️ Run the Application

Use the following command to start the Streamlit web app:

streamlit run app.py

Then open the link shown in your terminal (usually http://localhost:8501) in your browser.

Documentation

🔍 What Is Steganography

Steganography is the technique of hiding secret data within an ordinary, non-secret file or message to avoid detection.
In this project, we mainly focus on Image Steganography — concealing information inside digital images in such a way that there’s no visible change to the human eye.

The most common and simple technique for image steganography is the Least Significant Bit (LSB) embedding algorithm.

🧩 Least Significant Bit (LSB) Technique

Every color pixel in an image consists of three components — Red, Green, and Blue (RGB) — each represented by 8 bits (values ranging from 0–255).
The LSB method hides information by altering the least significant bit of each RGB component.

If a bit of the secret message is 1, the pixel value is made odd.

If it’s 0, the pixel value is made even.

This change is visually imperceptible, as modifying the least significant bit only changes the color intensity slightly (e.g., 255 → 254).

💡 Even though each pixel can store up to 3 bits of secret data (one per color channel), it’s good practice to store smaller messages in larger images to maintain stealth.

⚙️ How It Works
🔐 Encoding Process

The secret message is first converted into binary using ASCII representation.

The binary bits are embedded into the LSBs of image pixels sequentially.

Once all bits are hidden, a delimiter (1111111111111110) is appended to mark the message end.

The resulting image, called the Stego Image, looks visually identical to the original.

🔓 Decoding Process

The program reads the LSBs of the image pixels.

It reconstructs the hidden binary sequence until it encounters the delimiter.

The binary sequence is then converted back into readable text.

🖼️ Understanding a Digital Image

A digital image is a two-dimensional array (matrix) of pixels.
Each pixel represents a color based on its RGB values.

Channel	Bit Range	Description
Red	0–255	Intensity of red color
Green	0–255	Intensity of green color
Blue	0–255	Intensity of blue color

Each channel is represented using 8 bits, forming 24 bits per pixel (8 * 3 = 24).
In binary, the leftmost bit is the most significant bit (MSB) and the rightmost bit is the least significant bit (LSB).

Changing the LSB alters the color by less than 1% — hence, perfect for steganography.

🧠 Example

Let’s say a pixel has RGB values:

R = 11001010
G = 01101100
B = 11110010

To hide the message bit 1, we modify the LSB of each channel:

R = 11001011  (LSB changed to 1)
G = 01101101  (LSB changed to 1)
B = 11110011  (LSB changed to 1)

The overall pixel color changes only slightly — visually undetectable to the human eye.

🖼️ Hiding an Image Inside Another

The same concept can be extended to hide an entire image within another image:

Each bit of the secret image replaces the least significant bit of the cover image.

The process ensures that the larger image (cover) visually remains the same.

The more bits you use (e.g., using 2 or 3 LSBs), the more data can be hidden — but the higher the visual distortion.
