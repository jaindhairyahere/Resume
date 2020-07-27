import PyPDF2
import sys, os, subprocess, time
HEADER_PDF = str(sys.argv[1])
TEMPLATE_PDF = str(sys.argv[2])
PAGES = sys.argv[3]
TARGET_FILE = 'compiledResumes/{}'.format(HEADER_PDF)
def makeHead(PDFNAME):
    # Open a resume already containing the header in it
    resumeFile = PyPDF2.PdfFileReader(open(PDFNAME, 'rb'))
    Writer = PyPDF2.PdfFileWriter()
    # Select the page of resume file (1st page) that contains the header
    resume = resumeFile.getPage(0)
    # Crop the header and add it to the writer
    resume.cropBox.lowerLeft = (0, 690)
    resume.cropBox.upperRight = ()
    resume.mediaBox.lowerLeft = (0, 0)
    resume.bleedBox.lowerLeft = (0, 0)
    resume.trimBox.lowerLeft = (0, 0)
    Writer.addPage(resume)
    # Now some Manual work
    headFile = open('header{}.pdf'.format(PAGES), 'wb')
    Writer.addJS("this.print({bUI:true,bSilent:false,bShrinkToFit:true});")
    Writer.write(headFile)
    headFile.close()
    opener ="print" if sys.platform == "darwin" else "xdg-open"
    subprocess.call([opener, 'header{}.pdf'.format(PAGES)])
    

def editTemplate(TEMPLATE):
    # Reopen 
    templateFile = PyPDF2.PdfFileReader(open(TEMPLATE, 'rb'))
    pg1 = templateFile.getPage(0)
    header_files = PyPDF2.PdfFileReader(open('header{}.pdf'.format(PAGES), 'rb'))
    pg1.mergePage(header_files.getPage(0))

    NewWriter = PyPDF2.PdfFileWriter()
    NewWriter.addPage(pg1)
    # NewWriter.addPage(header_files.getPage(0))
    headFile = open(TARGET_FILE, 'wb')
    NewWriter.write(headFile) 
    headFile.close()
    opener ="open" if sys.platform == "darwin" else "xdg-open"
    subprocess.call([opener, TARGET_FILE.format(PAGES)])
# makeHead(HEADER_PDF)
editTemplate(TEMPLATE_PDF)
