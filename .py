import subprocess
import sys

subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "qrcode[pil]"])

import pyotp
import qrcode
import os
from qrcode.constants import ERROR_CORRECT_L

t = pyotp.TOTP("MilanoSuperSecretKey")


auth_str = t.provisioning_uri(name="AustineMilano", issuer_name="Elote App")

qr = qrcode.QRCode(
    version=1,
    error_correction=ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(auth_str)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("totp_qr.png")
print("QR code saved as totp_qr.png")

os.startfile("totp_qr.png")
