from tkinter import Tk, filedialog, Label, Entry, Button # For GUI
from PIL import ImageTk, Image

import numpy as np # For Image manipulation
import array
import secrets

import os.path
from os import path # Check if file actually exists

def scramImg(): # Main function to scramble image
    passes = int(passEntry.get() or 0) # In case some nonsense value is entered
    maxVari = int(diffEntry.get() or 0)
    result = np.asarray(origImg) # Converts the image to an array of RGB values
    
    if passes > 0 and maxVari > 0:
        for i in range(passes): # Main scramble function; note could differ for varying file format, should be made generic and tested
            dummy = np.random.randint(-1 * maxVari, high=maxVari, size=result.shape) # This returns an array of noise of the same shape as the given image
            result = np.add(result, dummy.astype("uint8")) # The noise is superimposed onto the image
            
    newImg = Image.fromarray(result)
    scramTkImg = ImageTk.PhotoImage(newImg) # Convert RGB array to image
    scramLabel.configure(image=scramTkImg)
    scramLabel.image = scramTkImg
    return 
    
root = Tk() # Setting up window
root.withdraw()
file_path = filedialog.askopenfilename() # Asks where file is at; would enforce images only later, could have separate logic for text
if not path.isfile(file_path):
    exit
root.deiconify()

root.title('Basic Image Viewer') # Title, Icon
root.iconbitmap('wave.ico')

origImg = Image.open(file_path) # Original image; could try salting later
result = np.asarray(origImg)

Label(root, text="Original Image").grid(row=0, column=0) # Displaying original image
origTkImg = ImageTk.PhotoImage(origImg)
origLabel = Label(image=origTkImg)
origLabel.grid(row=1, column=0, rowspan=6)

Label(root, text="# of Passes").grid(row=1, column=1) # Displaying buttons with entry fields
passEntry = Entry(root)
passEntry.grid(row=2, column=1)
Label(root, text="Max RGB diff").grid(row=3, column=1)
diffEntry = Entry(root)
diffEntry.grid(row=4, column=1)

button_scramble = Button(root, text="Scramble", command=lambda: scramImg()) # Linking scramble button with scramble function
button_exit = Button(root, text="Exit", command=root.quit)
button_scramble.grid(row=5, column=1)
button_exit.grid(row=6, column=1)

Label(root, text="Scrambled Image").grid(row=0, column=2)
scramTkImg = ImageTk.PhotoImage(origImg) # The first scrambled image is always the initial image unscrambled for display purposes; possible change in the future?
scramLabel = Label(image=scramTkImg)
scramLabel.grid(row=1, column=2, rowspan=6)

root.mainloop()