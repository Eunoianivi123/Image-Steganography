import numpy as np

def text_to_bin(message: str) -> str:
    return ''.join(format(ord(ch),'08b') for ch in message)

END_DELIMITER = '1111111111111110'

def available_capacity(image: np.ndarray) -> int:
    h,w,channels = image.shape
    return h * w * channels

def encode_bits_into_image(image : np.ndarray, bits : str) -> np.ndarray:
    stego = image.copy()

    if stego.shape[2] == 4:
        stego = stego[:, :, :3]

    h, w, channels = stego.shape
    flat_pixels = stego.reshape(-1,channels)

    bit_idx = 0
    total_bits = len(bits)

    for pix_idx in range(flat_pixels.shape[0]):
        for channel in range(channels):
            if bit_idx < total_bits:
                # Clear the least significant bit (LSB) by ANDing with 254 (11111110)
                # and then set the LSB with the new bit.
                flat_pixels[pix_idx, channel] = (flat_pixels[pix_idx, channel] & 254) | int(bits[bit_idx])
                bit_idx += 1
            else:
                break
        if bit_idx >= total_bits:
            break
    stego = flat_pixels.reshape((h, w, channels))
    return stego

def bin_to_text(binary_data: str) -> str:
    chars = []
    for i in range(0, len(binary_data), 8):
        byte = binary_data[i:i+8]
        if len(byte) < 8:
            continue
        chars.append(chr(int(byte, 2)))
    return ''.join(chars)

def decode_bits_from_image(image: np.ndarray) -> str:

    if image.shape[2] == 4:
        image = image[:, :, :3]

    h, w, channels = image.shape
    flat_pixels = image.reshape(-1, channels)
    bits = ''

    for pix in flat_pixels:
        for channel in range(channels):
            bits += str(pix[channel] & 1)
            if bits.endswith(END_DELIMITER):
               return bits
    return ''
