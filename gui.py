import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GButton_737=tk.Button(root)
        GButton_737["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times',size=10)
        GButton_737["font"] = ft
        GButton_737["fg"] = "#000000"
        GButton_737["justify"] = "center"
        GButton_737["text"] = "Button"
        GButton_737.place(x=40,y=30,width=70,height=25)
        GButton_737["command"] = self.GButton_737_command

        GRadio_231=tk.Radiobutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GRadio_231["font"] = ft
        GRadio_231["fg"] = "#333333"
        GRadio_231["justify"] = "center"
        GRadio_231["text"] = "RadioButton"
        GRadio_231.place(x=30,y=90,width=85,height=25)
        GRadio_231["command"] = self.GRadio_231_command

        GRadio_943=tk.Radiobutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GRadio_943["font"] = ft
        GRadio_943["fg"] = "#333333"
        GRadio_943["justify"] = "center"
        GRadio_943["text"] = "RadioButton"
        GRadio_943.place(x=30,y=130,width=85,height=25)
        GRadio_943["command"] = self.GRadio_943_command

    def GButton_737_command(self):
        print("command")


    def GRadio_231_command(self):
        print("command")


    def GRadio_943_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
