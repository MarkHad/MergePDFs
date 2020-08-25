from PyPDF2.merger import PdfFileMerger
import os

pdfs = []
merger = PdfFileMerger()

for file in os.scandir(os.getcwd()):
    if file.path.endswith(".pdf"):      # check if path leads to a pdf
        file_name = file.path.split(os.sep)[-1]

        if 'result_' not in file_name:  # Save all pdfs except 'result_' ones
            pdfs.append(file_name)

print('list of pdfs to merge: ', pdfs)

for pdf in pdfs:
    merger.append(pdf)

for n in range(1, 10):
    output_pdf_name = "result_" + str(n) + ".pdf"       # result_1, result_2 ...
    path_check = "./" + output_pdf_name                 # './result_1.pdf' ...

    if not os.path.exists(path_check):        # Check if pdf exists
        merger.write(output_pdf_name)
        merger.close()
        print("Merged files into ", output_pdf_name)
        break
    else:
        print(output_pdf_name, "already exists")

print("\nDone.")