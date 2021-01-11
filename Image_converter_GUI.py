import tkinter as tk
from tkinter import filedialog
from PIL import Image

root = tk.Tk()
canvass = tk.Canvas(root, width = 300, height = 300, bg = 'azure3', relief='raised')
canvass.pack()

label1 = tk.Label(root, text='Image Converter', bg='azure3')
label1.config(font=('helvetica', 20))
canvass.create_window(150, 60, window=label1)

def getPNG():
    global img
    import_file_path = filedialog.askopenfilename()
    img = Image.open(import_file_path)

browse_png = tk.Button(text='Select PNG file', command = getPNG, bg = 'blue', fg='white', font=('helvetica', 12, 'bold'))
canvass.create_window(150, 130, window=browse_png)

def convert():
    global img
    export_file_path = filedialog.asksaveasfilename(defaultextension = '.jpg')
    img.save(export_file_path)

saveasButton = tk.Button(text='Convert PNG to JPG', command=convert, bg='blue', fg='white', font=('helvetica', 12, 'bold'))
canvass.create_window(150, 180, window=saveasButton)
root.mainloop()