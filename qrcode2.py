import qrcode
import os

#input_URL = "https://www.google.com/"
input_URL = input("Enter your text: ")

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=15,
    border=4,
)

qr.add_data(input_URL)
qr.make(fit=True)

# Create dirctory 
if not os.path.isdir("qr_images"):
    os.mkdir("qr_images")

img = qr.make_image(fill_color="black", back_color="white")
img.save("qr_images/url_qrcode1.png")

print(qr.data_list)