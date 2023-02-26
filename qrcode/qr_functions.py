
import cv2
from PIL import Image
import zbarlight


def identify_qr_codes(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Print the shape and data type of the grayscale image
    # print("Shape:", gray.size)
    # print("Data type:", gray.dtype)
    if len(gray.shape) != 2:
        print("Error: grayscale image has invalid shape:", gray.shape)
        return

    new_image =pil_img = Image.fromarray(gray)
    # Decode any QR codes in the frame
    qr_codes = zbarlight.scan_codes(['qrcode'], new_image)

    # If any QR codes were found, print them out
    if qr_codes is not None:
        return True
    return False
