import pyttsx3
import PyPDF2
speaker = pyttsx3.init()
book = open('story.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
for page_num in range(8, pages):
    page = pdfReader.getPage(page_num)
    text = page.extractText()
    speaker.say(text)
speaker.runAndWait()