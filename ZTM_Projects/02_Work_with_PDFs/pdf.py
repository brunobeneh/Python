import PyPDF2

# PyPDF2 only can read on binary mode, so we need to put the 'rb'.
# 'r' it's for read and 'rb' it's for read binary
# on this example, we can creat a new pdf and rotate it.

with open('dummy.pdf', 'rb') as file:
    reader = PyPDF2.PdfFileReader(file)
    page = reader.getPage(0)
    page.rotateCounterClockwise(90)
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)
    with open('tilt.pdf', 'wb') as new_file:
        writer.write(new_file)