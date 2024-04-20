import PyPDF2
import tkinter as tk
from tkinter import filedialog, messagebox

def center_window(root, width, height):
    # Get the screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Calculate the x and y coordinates for the window to be centered
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)

    # Set the window geometry to center it on the screen
    root.geometry(f"{width}x{height}+{x}+{y}")

class PDFMergerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF Merger Tool")
        self.root.geometry("400x250")
        self.root.resizable(False, False)  # Make window non-resizable
        self.pdf_files = []

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.root, text="Select PDF Files to Merge", font=("Arial", 14), fg="white", bg="black")
        self.label.pack(pady=10)

        self.add_files_button = tk.Button(self.root, text="Add PDF Files", command=self.select_pdf_files, bg="gray", fg="white")
        self.add_files_button.pack(pady=5)

        self.description_label = tk.Label(self.root, text="Selected PDF Files:", font=("Arial", 10, "bold"), fg="white", bg="black")
        self.description_label.pack(pady=5)

        self.selected_files_label = tk.Listbox(self.root, font=("Arial", 10), fg="white", bg="black", bd=0, selectmode=tk.MULTIPLE, height=4)
        self.selected_files_label.pack(pady=5, padx=10, fill=tk.BOTH, expand=True)

        self.output_filename_label = tk.Label(self.root, text="Output Filename (without extension):", font=("Arial", 10), fg="white", bg="black")
        self.output_filename_label.pack(pady=5)

        self.output_filename_entry = tk.Entry(self.root, width=30)
        self.output_filename_entry.pack()

        self.merge_button = tk.Button(self.root, text="Merge PDFs", command=self.merge_pdf_files, bg="gray", fg="white")
        self.merge_button.pack(pady=5)

        self.watermark_label = tk.Label(self.root, text="https://github.com/anonfaded/pdf-merger", font=("Arial", 12, "bold"), fg="green", bg="black")
        self.watermark_label.pack(pady=5)

    def select_pdf_files(self):
        selected_files = filedialog.askopenfilenames(title="Select PDF Files", filetypes=[("PDF files", "*.pdf")])
        if selected_files:
            self.pdf_files.extend(selected_files)
            self.update_selected_files_label()

    def update_selected_files_label(self):
        self.selected_files_label.delete(0, tk.END)  # Clear existing entries
        for file_path in self.pdf_files:
            self.selected_files_label.insert(tk.END, file_path)

    def merge_pdf_files(self):
        output_filename = self.output_filename_entry.get().strip()
        if not output_filename:
            messagebox.showerror("Error", "Please enter a valid output filename.")
            return

        if not self.pdf_files:
            messagebox.showerror("Error", "No PDF files selected.")
            return

        if len(self.pdf_files) < 2:
            messagebox.showerror("Error", "Please select at least two PDF files.")
            return

        if not output_filename.endswith(".pdf"):
            output_filename += ".pdf"

        merger = PyPDF2.PdfMerger()
        for filename in self.pdf_files:
            with open(filename, 'rb') as pdf_file:
                pdf_reader = PyPDF2.PdfReader(pdf_file)
                merger.append(pdf_reader)

        try:
            with open(output_filename, 'wb') as merged_file:
                merger.write(merged_file)
            messagebox.showinfo("Success", f"PDF files merged successfully! Merged PDF saved as '{output_filename}'.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

def main():
    root = tk.Tk()
    root.config(bg="black")
    app = PDFMergerApp(root)
    center_window(root, 400, 350)  # Specify the width and height of the window
    root.mainloop()

if __name__ == "__main__":
    main()
