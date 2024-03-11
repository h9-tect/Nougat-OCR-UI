import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import subprocess

class FancyNougatPDFConverter:
    def __init__(self, master):
        self.master = master
        self.configure_gui()
        self.create_widgets()

    def configure_gui(self):
        self.master.title("Fancy Nougat PDF Converter")
        self.master.geometry("600x200")  # Set a suitable window size
        self.master.resizable(False, False)  # Disable window resizing

        # Set a theme
        self.style = ttk.Style()
        if "clam" in self.style.theme_names():
            self.style.theme_use("clam")  # Use a theme that is commonly available

        # Custom styles
        self.style.configure("TFrame", background="#252526")
        self.style.configure("TLabel", background="#252526", foreground="#D7D7D7", font=('Helvetica', 10))
        self.style.configure("TEntry", fieldbackground="#3C3C3C", foreground="#D7D7D7", font=('Helvetica', 10))
        self.style.configure("TButton", background="#007ACC", foreground="#D7D7D7", font=('Helvetica', 10), borderwidth=1)
        self.style.map("TButton", background=[("active", "#005C99")], foreground=[("active", "#FFFFFF")])
        self.style.configure("TCheckbutton", background="#252526", foreground="#D7D7D7", font=('Helvetica', 10))

    def create_widgets(self):
        frame = ttk.Frame(self.master, style="TFrame")
        frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)

        # PDF file selection
        ttk.Label(frame, text="PDF File:", style="TLabel").grid(row=0, column=0, sticky=tk.W, pady=(0, 10))
        self.pdf_entry = ttk.Entry(frame, width=50, font=('Helvetica', 10))
        self.pdf_entry.grid(row=0, column=1, sticky=tk.EW, pady=(0, 10), padx=(0, 10))
        ttk.Button(frame, text="Select PDF", command=self.browse_pdf).grid(row=0, column=2, pady=(0, 10))

        # Output folder selection
        ttk.Label(frame, text="Output Folder:", style="TLabel").grid(row=1, column=0, sticky=tk.W, pady=(0, 10))
        self.output_entry = ttk.Entry(frame, width=50, font=('Helvetica', 10))
        self.output_entry.grid(row=1, column=1, sticky=tk.EW, pady=(0, 10), padx=(0, 10))
        ttk.Button(frame, text="Choose Folder", command=self.browse_output_folder).grid(row=1, column=2, pady=(0, 10))

        # Options
        self.recompute_var = tk.BooleanVar()
        self.markdown_var = tk.BooleanVar()
        ttk.Checkbutton(frame, text="Recompute", variable=self.recompute_var, style="TCheckbutton").grid(row=2, column=0, sticky=tk.W, pady=(0, 10))
        ttk.Checkbutton(frame, text="Markdown Compatibility", variable=self.markdown_var, style="TCheckbutton").grid(row=2, column=1, sticky=tk.W, pady=(0, 10))

        # Convert button
        ttk.Button(frame, text="Convert Now", command=self.run_nougat).grid(row=3, column=0, columnspan=3, pady=(20, 0))

        # Adjust column configuration for stretching
        frame.columnconfigure(1, weight=1)

    def browse_pdf(self):
        file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        if file_path:
            self.pdf_entry.delete(0, tk.END)
            self.pdf_entry.insert(0, file_path)

    def browse_output_folder(self):
        folder_path = filedialog.askdirectory()
        if folder_path:
            self.output_entry.delete(0, tk.END)
            self.output_entry.insert(0, folder_path)

    def run_nougat(self):
        pdf_path = self.pdf_entry.get().strip()
        output_dir = self.output_entry.get().strip()
        # Here you should implement the logic to call your conversion function or script
        messagebox.showinfo("Info", "This is where the PDF conversion process would take place.")

if __name__ == "__main__":
    root = tk.Tk()
    app = FancyNougatPDFConverter(root)
    root.mainloop()
