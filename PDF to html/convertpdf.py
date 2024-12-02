# importing required modules
import PyPDF2
# creating a pdf file object
pdfFileObj = open('100_Ways_to_Motivate_Others.pdf', 'rb')
# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
# printing number of pages in pdf file
print(pdfReader.numPages)
# creating a page object
pageObj = pdfReader.getPage(10)
# extracting text from page
print(pageObj.extractText())
# closing the pdf file object
pdfFileObj.close()
