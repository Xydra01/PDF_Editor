import tkinter as tk
import sys
from tkinter import filedialog
from pypdf import PdfWriter


def select_files():
   
    # Create a hidden root window so the main Tkinter window doesn't appear
    root = tk.Tk()
    root.withdraw() 

    # Open the file dialog and allow multiple file selection
    file_paths = filedialog.askopenfilenames(
        title="Select Multiple Files",
        initialdir="/", # Default starting directory (Changable)
        filetypes=(("All files", "."), ("PDF Files", ".pdf"))
    )

    # Destroy the hidden root window after selection
    root.destroy()

    return file_paths

def convert():
    # TODO: Add functionality to convert non-pdf files into pdfs
    _
        

def split():
    # TODO: Add fucntionality to split a single pdf file into multiple pdf files
    _

def edit():
    # TODO: Add functionality to allow for the editing of text or other characteristics of PDF files.
    _

def merge():
    files_to_merge = select_files()

    merged_pdf = PdfWriter()

    for f in files_to_merge:
        if ".pdf" not in f:
            print('Invalid file type')
            menu()
        else:
            merged_pdf.append(f)
    
    merged_pdf.write("merged_pdf.pdf")


def menu():
    
    print("""
    PDF Editor v1.0
    
    Type your selection from the following menu options (Not case sensitive):
          
    > convert (Not Implemented)
    > split (Not Implemented)
    > edit (Not Implemented)
    > merge
    > exit
    
    """)

    response = input()
    

    if response == 'convert':
        print('Not currently implemented')
        

    elif response == 'split':
        print('Not currently implemented')
        

    elif response == 'edit':
        print('Not currently implemented')
        

    elif response == 'merge':
        merge()

    elif response == 'exit':
        sys.exit()

    else:
        print('Invalid response.')
    
    menu()

menu()

