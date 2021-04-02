import requests
from PyPDF2 import PdfFileReader
import io
url = 'https://books-library.online/files/books-library.online-12230111Ib9C3.pdf'

r = requests.get(url)
f = io.BytesIO(r.content)
reader = PdfFileReader(f)
if reader.isEncrypted:
  reader.decrypt("")
contents = reader.getPage(0).extractText()
print(contents)