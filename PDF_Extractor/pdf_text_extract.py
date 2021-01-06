import PyPDF2 as p2

PDFfile = open("unlock_52920-02-40030-01-1AB-2.pdf", 'rb')
pdfread = p2.PdfFileReader(PDFfile)

x = pdfread.getPage(0)
page_content = x.extractText()
print(page_content)