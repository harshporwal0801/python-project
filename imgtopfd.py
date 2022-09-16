import os
from PIL import Image

# Create dirctory 
if not os.path.isdir("pdf_images"):
    os.mkdir("pdf_images")

img = Image.open(r'C:\Users\harsh\Desktop\hp.png')
pdf_file = img.convert('RGB')
pdf_file.save(r'pdf_images/hp.pdf')

print("Image to pdf converted successfully")

