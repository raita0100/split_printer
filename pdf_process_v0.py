from PyPDF2 import PdfFileWriter, PdfFileReader
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-f", "--file", required=True, help="Path to the input file")
ap.add_argument("-m", "--method", required=True, type=int,help="Oparation to perform 1.odd_even_split 2.reverse")
args = vars(ap.parse_args())

file_name=  args["file"]
total_pages = 0

def separate_odd_even_pages():

    print("[INFO] Loading file {}".format(file_name))
    input_pdf = PdfFileReader(open(file_name, "rb"))

    output_even = PdfFileWriter()
    output_odd = PdfFileWriter()
    print("[INFO] Converting ....")

    total_pages = input_pdf.numPages
    print(f'\nTotal Pages : {total_pages}')

    for i in range(input_pdf.numPages):

        if i%2 == 0:
            output_odd.addPage(input_pdf.getPage(i))
        else:
            output_even.addPage(input_pdf.getPage(i))

    if total_pages%2 == 1:
        _, _, w, h = input_pdf.getPage(0)['/MediaBox']
        output_even.addBlankPage(w, h)

    with open("odd_pages.pdf","wb") as odd_file_writer:
        output_odd.write(odd_file_writer)

    odd_file_writer.close()

    with open("even_pages.pdf", "wb") as even_file_writer:
        output_even.write(even_file_writer)
    even_file_writer.close()

    print("[INFO] Convertion end and files saved")

def reverse_pages():

    print("[INFO] Loading file {}".format(file_name))
    input_pdf = PdfFileReader(open(file_name,"rb"))

    reversed_writer = PdfFileWriter()

    number_pages = input_pdf.numPages

    print("[INFO] Converting ....")
    for i in range(0, number_pages):

        reversed_writer.addPage(input_pdf.getPage(number_pages-1-i))

    with open("reversed.pdf", "wb") as write_file:
        reversed_writer.write(write_file)

    write_file.close()
    print("[INFO] Convertion end and files saved")

if args["method"] == 1:
    separate_odd_even_pages()
    
elif args["method"] == 2:
    reverse_pages()
