import tkinter as tk
from tkinter import filedialog, messagebox
from pdf2docx import Converter
import os

pdf_path = ""

def select_pdf():
    global pdf_path
    pdf_path = filedialog.askopenfilename(
        title="Выберите PDF файл",
        filetypes=[("PDF-файлы", "*.pdf")]
    )
    if pdf_path:
        label_path.config(text=pdf_path)

def convert_pdf():
    if not pdf_path:
        messagebox.showwarning("Ошибка", "Сначала выберите PDF файл")
        return

    docx_path = os.path.splitext(pdf_path)[0] + ".docx"

    try:
        cv = Converter(pdf_path)
        cv.convert(docx_path)
        cv.close()
        messagebox.showinfo("Готово", f"Файл сохранён:\n{docx_path}")
    except Exception as e:
        messagebox.showerror("Ошибка", str(e))

root = tk.Tk()
root.title("Конвертер PDF → DOCX")
root.geometry("400x250")

btn_select = tk.Button(root, text="Выбрать PDF", command=select_pdf)
btn_select.pack(pady=10)

label_path = tk.Label(root, text="Файл не выбран", wraplength=350)
label_path.pack(pady=10)

btn_convert = tk.Button(root, text="Конвертировать", command=convert_pdf)
btn_convert.pack(pady=20)

root.mainloop()
