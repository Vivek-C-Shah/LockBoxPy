import os
import tkinter as tk
from tkinter import filedialog
import subprocess

def py_to_exe():
    # Select the .py file to convert
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(title="Select .py file to convert", filetypes=[("Python files", "*.py")])
    if not file_path:
        return

    # Convert the .py file to .exe
    subprocess.call(["pyinstaller", file_path, "--onefile"])

    # Show success message
    tk.messagebox.showinfo('Success', 'Conversion successful!')

if __name__ == '__main__':
    root = tk.Tk()
    root.title('Python to EXE Converter')

    # Create the UI elements
    label = tk.Label(root, text='Select the .py file to convert:')
    label.pack()

    # Create a frame to hold the file path input area and browse button
    file_frame = tk.Frame(root)
    file_frame.pack()

    file_path_var = tk.StringVar()
    browse_button = tk.Button(file_frame, text='Browse', command=lambda: file_path_var.set(filedialog.askopenfilename(title="Select .py file to convert", filetypes=[("Python files", "*.py")])))
    browse_button.pack(side=tk.RIGHT)

    convert_button = tk.Button(root, text='Convert to EXE', command=lambda: py_to_exe())
    convert_button.pack()

    root.mainloop()
