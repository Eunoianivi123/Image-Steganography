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


def _inject_styles():
    css = """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Roboto:wght@300;400;700&display=swap');
    html, body, [class*="css"] {
        background: linear-gradient(180deg, #05170d 0%, #0b2816 35%, #36261b 100%);
        color: #282E2AFF;
        font-family: 'Roboto', sans-serif;
    }
    .stApp > header {visibility: hidden;} /* hide default header */
    .app-title {
        font-family: 'Orbitron', sans-serif;
        color: #bfffcf;
        font-size: 34px;
        margin-bottom: 6px;
        text-shadow: 0 0 18px rgba(0,255,128,0.08);
    }
    .block {
        background: rgba(12,18,12,0.56);
        border: 1px solid rgba(255,255,255,0.04);
        border-left: 6px solid #0f9d58;
        padding: 18px;
        border-radius: 10px;
        box-shadow: 0 10px 40px rgba(0,0,0,0.6);
    }
    .stButton>button, .stDownloadButton>button {
        background: linear-gradient(90deg,#0f9d58,#0b6623) !important;
        color: #e9ffef !important;
        border: none !important;
        box-shadow: 0 6px 14px rgba(0,0,0,0.5) !important;
        border-radius: 8px !important;
        padding: 8px 14px !important;
    }
    .stTextArea>div>div>textarea { background: rgba(0,0,0,0.35) !important; color: #e6f5ea !important; }
    .stFileUploader { background: rgba(255,255,255,0.02); border-radius:8px; }
    .footer { color: #9edfb1; font-size:12px; margin-top:12px; opacity:0.9 }
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)


st.set_page_config(page_title="Steganography App", layout="centered")
_inject_styles()
st.markdown('<div class="app-title">🕵️‍♀️ Image Steganography — Cyber LSB</div>', unsafe_allow_html=True)
st.markdown('<div class="block">', unsafe_allow_html=True)

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
    # close block div and add footer
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('<div class="footer">Styled with deep green accents • Wood tones • Cyber font</div>', unsafe_allow_html=True)