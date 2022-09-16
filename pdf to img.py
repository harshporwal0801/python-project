from pdf2jpg import pdf2jpg
inputpath = r"C:\Users\harsh\Desktop\pdf-test.pdf"
outputpath = r"C:\Users\harsh\Desktop\qrcode"
# To convert single page
result = pdf2jpg.convert_pdf2jpg(inputpath, outputpath, pages="1")
print(result)
