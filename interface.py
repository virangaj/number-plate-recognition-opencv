from cProfile import label
from fileinput import filename
import tkinter as tk
from tkinter import *

from tkinter import Canvas, filedialog, Text
import os
from PIL import Image, ImageTk


from main import main
from getVehicleDetails import *

root = tk.Tk()

# open image


def open_image_eng():
    filename = filedialog.askopenfilename(
        initialdir='F:\3rd Yr\CS 314 - Image Processing Practical\Project\Project\Samples', title='Select File', filetype=(("jpeg files", "*.jpg"), ("png files", "*.png"), ("all files", "*.*")))
    text = main(filename)

    display_original(filename)
    display_output()
    print(text)
    display_details_eng(text)


def open_image_army():
    filename = filedialog.askopenfilename(
        initialdir='F:\3rd Yr\CS 314 - Image Processing Practical\Project\Project\Samples', title='Select File', filetype=(("jpeg files", "*.jpg"), ("png files", "*.png"), ("all files", "*.*")))
    text = main(filename)

    display_original(filename)
    display_output()
    print(text)
    display_details_army(text)


def open_image_by_number():
    filename = filedialog.askopenfilename(
        initialdir='F:\3rd Yr\CS 314 - Image Processing Practical\Project\Project\Samples', title='Select File', filetype=(("jpeg files", "*.jpg"), ("png files", "*.png"), ("all files", "*.*")))
    text = main(filename)

    display_original(filename)
    display_output()
    print(text)
    display_details_by_number(text)


def display_details_army(text):
    print('Number Plate :', text)
    owner = ''
    if not text:
        print('Number plate cannot detected')
    else:
        owner = vehicle_related(text)

    numberplate_text = Label(
        root, text='Number plate : {}'.format(text), fg='red', font=("Helvetica", 14))
    numberplate_text.pack()

    province_text = Label(
        root, text='Vehicle Related To : {}'.format(owner), fg='red', font=("Helvetica", 14))
    province_text.pack()


def display_details_eng(text):
    print('Number Plate :', text)

    province = ''
    type = ''
    category = ''

    if not text:
        print('Number plate cannot detected')
    else:
        splited_text = text.split()
        print(splited_text)

        # return province
        if splited_text[0].isalpha():
            province = get_province(splited_text[0])
            print(
                'Vehicle Registered in : {} - {} '.format(splited_text[0], province))
            type = get_vehicle_type(splited_text[1])
            if splited_text[0].isalpha():
                print(
                    'Vehicle class is : {} - {} '.format(splited_text[1], type))
        else:
            category = categorized_by_number(text)

        # return vehicle type

    numberplate_text = Label(
        root, text='Number plate : {}'.format(text), fg='blue', font=("Helvetica", 14))
    numberplate_text.pack()

    vehicle_category = Label(
        root, text='Category by Number: {}'.format(category), fg='blue', font=("Helvetica", 14))
    vehicle_category.pack()

    province_text = Label(
        root, text='Province : {}'.format(province), fg='blue', font=("Helvetica", 14))
    province_text.pack()

    vehicle_type = Label(
        root, text='Vehicle class : {}'.format(type), fg='blue', font=("Helvetica", 14))
    vehicle_type.pack()


def display_original(filename):
    # print(filename.split('/')[-1])
    img = Image.open(filename)
    img.thumbnail((350, 350))
    img = ImageTk.PhotoImage(img)
    original_img.configure(image=img)
    original_img.image = img


def display_output():
    # img = Image.open(filename)
    # img.thumbnail((350, 350))
    img = ImageTk.PhotoImage(Image.open(
        "F://3rd Yr//CS 314 - Image Processing Practical//Project//Project//NumberPlateDetection//crop.jpg"))
    output_img.configure(image=img)
    output_img.image = img


# header text
province_text = Label(
    root, text='Number Plate Reader', fg='#263D42', font=("Helvetica", 18))
province_text.pack()


# create canvas
canvas = tk.Canvas(root, height=600, width=500, bg='#263D42')
canvas.pack()

# create middle frame
frame = tk.Frame(root, bg='white')
frame.place(relwidth=0.8, relheight=0.6, relx=0.1, rely=0.1)

# disply first image

original_img = Label(frame)
original_img.pack()

# disply output image
output_img = Label(frame)
output_img.pack()

# buttons
open_file_en = tk.Button(root, text='Open Image with English Letters', padx=10,
                         pady=5, fg='white', bg='#263D42', command=open_image_eng)


open_file_si = tk.Button(root, text='Open Image with Sinhala Letters', padx=10,
                         pady=5, fg='white', bg='#263D42', command=open_image_army)


exit_window = tk.Button(root, text='Exit', padx=10,
                        pady=5, fg='white', bg='#263D42', command=lambda: exit())

open_file_en.pack()
open_file_si.pack()

exit_window.pack()


root.title("Number Plate Reader")
root.mainloop()
