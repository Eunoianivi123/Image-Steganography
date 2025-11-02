import streamlit as st
import numpy as np
import cv2
from PIL import Image
from io import BytesIO
from imgStegno import (
    text_to_bin,
    available_capacity,
    encode_bits_into_image,
    END_DELIMITER,
    decode_bits_from_image,
    bin_to_text,
    is_printable_text,
)


st.set_page_config(page_title="Steganography App", layout="centered")
st.title("🕵️‍♀️ Image Steganography using OpenCV")

mode = st.radio("Choose an action:", ["Encode (Hide Message)", "Decode (Extract Message)"])

if mode == "Encode (Hide Message)":
    uploaded_file = st.file_uploader("Upload Cover Image", type=["png", "jpg", "jpeg", "bmp"])
    if uploaded_file is not None:
        image = np.array(Image.open(uploaded_file))
        st.image(image, caption="Cover Image", use_column_width=True)

        message = st.text_area("Enter the secret message:")
        if message:
            binary_message = text_to_bin(message) + END_DELIMITER
            bits_needed = len(binary_message)
            cap = available_capacity(image)

            st.write(f"🧠 Image Capacity: {cap} bits")
            st.write(f"💬 Message Size: {bits_needed} bits")

            if bits_needed > cap:
                st.error("Message too long to fit in this image!")
            else:
                if st.button("🔐 Encode Message"):
                    stego_image = encode_bits_into_image(image, binary_message)

                    # Convert back to downloadable image
                    output_image = Image.fromarray(stego_image)
                    buf = BytesIO()
                    output_image.save(buf, format="PNG")
                    byte_im = buf.getvalue()

                    st.success("✅ Message successfully hidden in image!")
                    st.download_button(
                        label="📥 Download Stego Image",
                        data=byte_im,
                        file_name="stego_image.png",
                        mime="image/png"
                    )

elif mode == "Decode (Extract Message)":
    uploaded_stego = st.file_uploader("Upload Stego Image", type=["png", "jpg", "jpeg", "bmp"])
    if uploaded_stego is not None:
        image = np.array(Image.open(uploaded_stego))
        st.image(image, caption="Stego Image", use_column_width=True)

        if st.button("🔓 Decode Message"):
            bits = decode_bits_from_image(image)
            # decode_bits_from_image now returns None when no delimiter is found
            if not bits:
                st.error("No meaningful message encoded.")
            else:
                message_bits = bits[:bits.index(END_DELIMITER)]
                message = bin_to_text(message_bits)
                # validate the decoded message is mostly printable text
                if not is_printable_text(message):
                    st.error("No meaningful message encoded.")
                else:
                    st.success("✅ Hidden Message Found:")
                    st.text_area("Hidden Message", message, height=150)