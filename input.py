from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from sys import exit as e
from PIL import ImageTk, Image


class App(Tk):

    def __init__(self):
        super().__init__()
        self.canvas = Canvas(self, width=1000, height=500, bg='beige')
        self.canvas.pack()
        self.canvas.bind('<1>', self.make_circle)

        self.select_button = Button(self.canvas, text="Select", font=('calibri', 10), bd=3, width=8, bg='white',
                                    command=self.open, relief=RIDGE)
        self.select_button.place(x=0, y=460)

        self.canvas.create_rectangle(100, 170, 100 + 190, 170 + 150, outline='red')  # Make rectcangle for showing image

        label = Label(self.canvas, text="Add File")
        label.config(font=("Courier", 16))
        label.place(x=100, y=100)

        label2 = Label(self.canvas, text="Enter Tags")
        label2.config(font=("Courier", 16))
        label2.place(x=100, y=350)

        self.inputtags = Text(self.canvas, height=1,
                              width=50, font=("Courier", 16),
                              bg="white")
        self.inputtags.place(x=105, y=400)

        self.finish_button = Button(self.canvas, height=2,
                                    width=20,
                                    text="Finish",
                                    command=self.finish)
        self.finish_button.place(x=310, y=100)

    def open(self):
        self.file_chosen = askopenfilename(initialdir="/Desktop", title="Select file", filetypes=(
            ('JPG', '*.jpg'), ('PNG', '*.png'), ('JPEG', '*jpeg')), defaultextension=".jpg")

        try:

            w = 189  # width of picture
            h = 149  # height of picture

            img = Image.open(self.file_chosen)  # Rendering the image
            self.img = img.resize((w, h),
                                  Image.ANTIALIAS)  # To fit the image in the box , we need to resize it , the modlue has inbuilt functions to do that.

            self.image = ImageTk.PhotoImage(self.img)  # Loading a image object that can be used on canvas
            self.canvas.create_image(101, 171, anchor=NW, image=self.image)

        except:
            messagebox.showinfo('Error')
            return ()

    def make_circle(self, event):

        x, y = event.x, event.y
        print(x, y)

    def finish(self):
        with open("count.txt", 'r') as count:
            self.fileid = int(count.read()) + 1
        with open("count.txt", 'w') as count:
            count.write(str(self.fileid))

        filename = f"Images/{self.fileid}.jpeg"  # The name of the new file

        self.img.save(f"{filename}")  # saving the image file into the folder of the App

        # File saving with the tags
        with open("files.txt", 'a') as file:
            file.write(f"{filename},{self.inputtags.get('1.0', 'end-1c')},\n")  # writing the data into the app

        e()


if __name__ == '__main__':
    App().mainloop()
