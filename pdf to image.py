# import module
import os
from pdf2image import convert_from_path

# Create dirctory 
if not os.path.isdir("img_pfd"):
    os.mkdir("img_pdf")

file = convert_from_path('pdf-test.pdf')

for i in range(len(file)):

 file[i].save('page'+ str(i) +'.jpg', 'JPEG')