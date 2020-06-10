import PyPDF2
def makeHead(PDFNAME):
    # Open a resume already containing the header in it
    resumeFile = PyPDF2.PdfFileReader(open(PDFNAME, 'rb'))
    Writer = PyPDF2.PdfFileWriter()
    # Select the page of resume file (1st page) that contains the header
    resume = resumeFile.getPage(0)
    # Crop the header and add it to the writer
    resume.cropBox.lowerLeft = (0, 660)
    resume.mediaBox.lowerLeft = (0, 0)
    resume.bleedBox.lowerLeft = (0, 0)
    resume.trimBox.lowerLeft = (0, 0)
    Writer.addPage(resume)
    # Now some Manual work
    
    headFile = open('hello.pdf', 'wb')
    Writer.write(headFile)
    headFile.close()

    # Reopen 
    helloFile = PyPDF2.PdfFileReader(open('try.pdf', 'rb'))
    pg1 = helloFile.getPage(0)
    x = PyPDF2.PdfFileReader(open('test.pdf', 'rb'))
    pg1.mergePage(x.getPage(0))
    # pg1.addTransformation(ctm=(1, 0, 0, 1, 0, 660))
    NewWriter = PyPDF2.PdfFileWriter()
    NewWriter.addPage(pg1)
    NewWriter.addPage(x.getPage(1))
    headFile = open('hello2.pdf', 'wb')
    NewWriter.write(headFile) 
makeHead()
