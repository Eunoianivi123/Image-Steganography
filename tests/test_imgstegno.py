import unittest
import numpy as np

from imgStegno import (
    text_to_bin,
    END_DELIMITER,
    available_capacity,
    encode_bits_into_image,
    decode_bits_from_image,
    bin_to_text,
    is_printable_text,
)


class TestImageStegno(unittest.TestCase):

    def test_encode_decode_roundtrip(self):
        # small RGB image 10x10
        h, w = 10, 10
        image = np.zeros((h, w, 3), dtype=np.uint8)

        message = "Hello, world!"
        binary_message = text_to_bin(message) + END_DELIMITER

        cap = available_capacity(image)
        self.assertGreaterEqual(cap, len(binary_message))

        stego = encode_bits_into_image(image.copy(), binary_message)

        bits = decode_bits_from_image(stego)
        self.assertIsNotNone(bits, "Decoded bits should not be None for a stego image")
        self.assertIn(END_DELIMITER, bits)

        message_bits = bits[: bits.index(END_DELIMITER)]
        decoded = bin_to_text(message_bits)
        self.assertEqual(decoded, message)
        self.assertTrue(is_printable_text(decoded))

    def test_decode_on_clean_image_returns_none(self):
        # Create a clean image (all zeros) which shouldn't contain the END_DELIMITER
        h, w = 8, 8
        image = np.zeros((h, w, 3), dtype=np.uint8)

        bits = decode_bits_from_image(image)
        self.assertIsNone(bits, "Decoding a clean image should return None (no delimiter)")


if __name__ == "__main__":
    unittest.main()
