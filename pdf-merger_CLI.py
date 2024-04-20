import PyPDF2
import tkinter as tk
from tkinter import filedialog
from colorama import init, Fore
import os

# Initialize colorama
init(autoreset=True)

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def select_pdf_files():
    clear_terminal()
    print(Fore.YELLOW + "PDF Merger Tool -  " + Fore.GREEN + "https://github.com/anonfaded/pdf-merger")
    pdf_files = []
    while True:
        filename = filedialog.askopenfilename(title="Select PDF file")
        if not filename:  # User cancelled selection
            break
        pdf_files.append(filename)
        choice = input("Do you want to add more PDF files? (y/n): ")
        if choice.lower() != 'y':
            break
    return pdf_files

def merge_pdf_files(pdf_files, output_filename):
    merger = PyPDF2.PdfMerger()
    for filename in pdf_files:
        with open(filename, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            merger.append(pdf_reader)
    with open(output_filename, 'wb') as merged_file:
        merger.write(merged_file)
    print(Fore.GREEN + f"PDF files merged successfully! Merged PDF saved as '{output_filename}'.")

def main():
    while True:
        try:
            pdf_files = select_pdf_files()
            if not pdf_files:
                print(Fore.RED + "No PDF files selected. Exiting.")
                break
            clear_terminal()
            output_filename = input("Enter the filename for the merged PDF (without extension): ").strip()
            if not output_filename:
                output_filename = "merged.pdf"  # Default filename
            if not output_filename.endswith(".pdf"):
                output_filename += ".pdf"  # Add the .pdf extension if not present
            merge_pdf_files(pdf_files, output_filename)
            break
        except Exception as e:
            print(Fore.RED + f"An error occurred: {e}")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main()
