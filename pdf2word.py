from pdf2docx import Converter
pdf_file = 'pdf1.pdf'
docx_file = 'pdf1.docx'
cv = Converter(pdf_file)
cv.convert(docx_file)
cv.close()
