from PIL import Image
import tkinter as tk
from tkinter import filedialog
import copy
import os

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilenames()
basedirectory = os.path.dirname(file_path[0])
image_list = []

for file in file_path:
    # Validates only png, jpegs, and HEIC (APPLE)
    if file.endswith('.png') or file.endswith('.jpeg') or file.endswith('.HEIC'):
        image = Image.open(file)
        image_convert = image.convert('RGB')
        image_list.append(image_convert)


filename = input('Enter name of pdf: ')

image_list_shortened = copy.copy(image_list)
image_list_shortened.pop(0)
image_list[0].save(f'{basedirectory}/{filename}.pdf', save_all=True, append_images=image_list_shortened)
print('Done! Files Converted')





