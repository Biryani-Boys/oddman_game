from random import randint
from tkinter import *

from PIL import ImageTk, Image

from selector import selector_session


class App(Tk):

    def __init__(self):
        super().__init__()

        self.correct = None
        self.options = {'A': None, 'B': None, 'C': None, 'D': None}
        self.canvas = Canvas(self, width=1000, height=500, bg='beige')
        self.canvas.pack()
        self.canvas.bind('<1>', self.make_circle)

        self.w = 190
        self.h = 150

        l = Label(self.canvas, text="WHICH IS THE ODD MAN ?")
        l.config(font=("Courier", 16))
        l.place(x=100, y=100)

        self.canvas.create_rectangle(100, 170, 100 + self.w, 170 + self.h, outline='red')
        self.canvas.create_rectangle(300, 170, 300 + self.w, 170 + self.h, outline='red')
        self.canvas.create_rectangle(500, 170, 500 + self.w, 170 + self.h, outline='red')
        self.canvas.create_rectangle(700, 170, 700 + self.w, 170 + self.h, outline='red')

        self.inputtxt = Text(self.canvas, height=1,
                             width=3, font=("Courier", 16),
                             bg="white")
        self.inputtxt.place(x=475, y=350)
        self.Output = Text(self.canvas, height=2,
                           width=10,
                           bg="light cyan")
        self.Output.place(x=111, y=416)

        self.Display = Button(self.canvas, height=2,
                              width=20,
                              text="Check",
                              command=lambda: self.Take_input())
        self.Display.place(x=111, y=415 - 50)

        self.Pass_Button = Button(self.canvas, height=2, width=20, text="PASS", command=self.display_images)
        self.Pass_Button.place(x=780, y=50)

    def Take_input(self):
        INPUT = self.inputtxt.get("1.0", "end-1c")
        print(INPUT)
        if (INPUT == self.correct):
            self.Output.delete("1.0", "end")
            self.Output.insert(END, "Correct")

            # Restart the stuff
            self.display_images()

        else:
            self.Output.delete("1.0", "end")
            self.Output.insert(END, "Wrong")

    def display_images(self):
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

    def make_circle(self, event):
        x, y = event.x, event.y
        print(x, y)


if __name__ == '__main__':
    Game = App()
    Game.display_images()
    Game.mainloop()
