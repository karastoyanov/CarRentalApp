import sys
from tkinter import *
import tkinter as tk
from PIL import Image
from . import show_customers





class App:
    root = tk.Tk()
    root.title("Car Rental App")
    root.geometry("700x900")
    icon = tk.PhotoImage(file = r"images/car-rental.png")
    root.wm_iconphoto(False, icon)
    
    def showCustomers():
        pass
    
    
    # List all customers
    customersListImage = PhotoImage(file = r"images/client.png")
    customersListButton = Button(root, image = customersListImage, command = exec(open('show_customers.py').read()))
    customersListLabel = Label(image = customersListImage)
    customersListButton.pack(pady = 20)
    customersListButton.place(x = 50, y = 100)
    
        


mainloop()