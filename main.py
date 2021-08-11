from random import randint
from tkinter import *
from PIL import ImageTk, Image
from selector import selector_session
from tkinter import messagebox



class App(Tk):

    def __init__(self):
        super().__init__()

        self.correct = None
        self.options = {'A': None, 'B': None, 'C': None, 'D': None}
        self.canvas = Canvas(self, width=1000, height=500, bg='#92A8D1')
        self.canvas.pack()

        self.w = 190
        self.h = 150
        self.score = 0

        l = Label(self.canvas, text="WHICH IS THE ODD MAN ?", bg="#92A8D1")
        l.config(font=("Courier", 16))
        l.place(x=100, y=100)

        A = Label(self.canvas, text="A", bg="#92A8D1")
        A.config(font=("Courier", 16))
        A.place(x=183, y=332)

        B = Label(self.canvas, text="B", bg="#92A8D1")
        B.config(font=("Courier", 16))
        B.place(x=392, y=333)

        C = Label(self.canvas, text="C", bg="#92A8D1")
        C.config(font=("Courier", 16))
        C.place(x=589, y=332)

        D = Label(self.canvas, text="D", bg="#92A8D1")
        D.config(font=("Courier", 16))
        D.place(x=794, y=336)

        self.scorebutton = Label(self.canvas, text=f"score:{self.score}", bg="#92A8D1")
        self.scorebutton.config(font=("Courier", 16))
        self.scorebutton.place(x=651, y=419)

        self.canvas.create_rectangle(100, 170, 100 + self.w, 170 + self.h, outline='#FF6F61')
        self.canvas.create_rectangle(300, 170, 300 + self.w, 170 + self.h, outline='#FF6F61')
        self.canvas.create_rectangle(500, 170, 500 + self.w, 170 + self.h, outline='#FF6F61')
        self.canvas.create_rectangle(700, 170, 700 + self.w, 170 + self.h, outline='#FF6F61')

        self.inputtxt = Text(self.canvas, height=1,
                             width=3, font=("Courier", 16),
                             bg="white")
        self.inputtxt.place(x=475, y=350)
        self.Output = Label(self.canvas, text="   ")
        self.Output.config(font=("Courier", 16))

        self.Output.place(x=111, y=416)

        self.Display = Button(self.canvas, height=2,
                              width=20,
                              text="Check",
                              command=lambda: self.Take_input(), bg="#66ff33")
        self.Display.place(x=111, y=415 - 50)

        self.Pass_Button = Button(self.canvas, height=2, width=20, text="PASS", bg="#66ff33",
                                  command=self.passer)
        self.Pass_Button.place(x=713, y=90)

    def Take_input(self):
        INPUT = self.inputtxt.get("1.0", "end-1c")
        print(INPUT)
        if (INPUT == self.correct):
            self.Output.destroy()
            self.Output = Label(self.canvas, text="Correct")
            self.Output.config(font=("Courier", 16))
            self.Output.place(x=111, y=416)

            # Restart the stuff
            self.changescore()

            self.display_images()




        else:
            self.Output.destroy()
            self.Output = Label(self.canvas, text="Wrong")
            self.Output.config(font=("Courier", 16))
            self.Output.place(x=111, y=416)

    def changescore(self):
        self.score = self.score + 1

        self.scorebutton.destroy()
        self.scorebutton = Label(self.canvas, text=f"score:{self.score}")
        self.scorebutton.config(font=("Courier", 16))
        self.scorebutton.place(x=651, y=419)

    def display_images(self):
        try:
            images_to_load = list(selector_session())

            correct_option = images_to_load[3]

            # Distributing the images into A,B,C,D randomly and also getting the correct option marked.
            for x, y in zip((3, 2, 1, 0), ("D", "C", "B", "A")):
                chosen = images_to_load.pop(randint(0, x))
                if chosen == correct_option:
                    self.correct = y
                self.options[y] = chosen

            # Correct answer
            # print(self.correct)

            # Loading the image and putting in rectangle.

            self.imgA = Image.open(self.options['A'])  # Rendering the image
            self.imgA = self.imgA.resize((self.w - 1, self.h - 1),
                                         Image.ANTIALIAS)  # To fit the image in the box , we need to resize it , the modlue has inbuilt functions to do that.
            self.imageA = ImageTk.PhotoImage(self.imgA)  # Loading a image object that can be used on canvas
            A = self.canvas.create_image(101, 171, anchor=NW, image=self.imageA)

            self.imgB = Image.open(self.options['B'])  # Rendering the image
            self.imgB = self.imgB.resize((self.w - 1, self.h - 1),
                                         Image.ANTIALIAS)  # To fit the image in the box , we need to resize it , the modlue has inbuilt functions to do that.
            self.imageB = ImageTk.PhotoImage(self.imgB)  # Loading a image object that can be used on canvas
            B = self.canvas.create_image(301, 171, anchor=NW, image=self.imageB)

            self.imgC = Image.open(self.options['C'])  # Rendering the image
            self.imgC = self.imgC.resize((self.w - 1, self.h - 1),
                                         Image.ANTIALIAS)  # To fit the image in the box , we need to resize it , the modlue has inbuilt functions to do that.
            self.imageC = ImageTk.PhotoImage(self.imgC)  # Loading a image object that can be used on canvas
            C = self.canvas.create_image(501, 171, anchor=NW, image=self.imageC)

            self.imgD = Image.open(self.options['D'])  # Rendering the image
            self.imgD = self.imgD.resize((self.w - 1, self.h - 1),
                                         Image.ANTIALIAS)  # To fit the image in the box , we need to resize it , the modlue has inbuilt functions to do that.
            self.imageD = ImageTk.PhotoImage(self.imgD)  # Loading a image object that can be used on canvas
            D = self.canvas.create_image(701, 171, anchor=NW, image=self.imageD)
        except:
            self.display_images()

    def passer(self):
        messagebox.showinfo(title='Pass',message=f'Correct Option was : {self.correct}')
        self.display_images()

if __name__ == '__main__':
    Game = App()
    Game.display_images()
    Game.mainloop()

