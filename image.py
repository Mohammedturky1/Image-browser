#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:





# In[33]:



import glob
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog, messagebox

class Image_Viewer:
    def __init__(self, root):
        self.window = root
        self.window.geometry("960x600")
        self.window.title('Image Viewer')
        self.window.configure(bg='gray20')
        self.window.resizable(width = False, height = False)

  
        self.img = img
        self.Image_Path = image_path
        
        self.Image_List = list()
        self.cur_index = 0

        self.width = 740
        self.height = 480

        self.menubar = Menu(self.window)
        edit = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='Open', menu=edit)
        edit.add_command(label='Open Image',command=self.Open_Image)
        edit.add_command(label='Open Images',command=self.Open_Images)
        edit.add_command(label='Open Folder',command=self.Open_Folder)



        exit = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='Exit', menu=exit)
        exit.add_command(label='Exit', command=self.Exit)

        self.window.config(menu=self.menubar)

        prev_btn = Button(self.window, text="Prev",         font=("Helvetica", 15, 'bold'), command=self.Prev_Image)
        prev_btn.place(x=15,y=270)

        next_btn = Button(self.window, text="Next",         font=("Helvetica", 15, 'bold'), command=self.Next_Image)
        next_btn.place(x=865,y=270)

        self.frame_1 = Frame(self.window,         bg='gray20',width=self.width,height=self.height)
        self.frame_1.pack()
        self.frame_1.place(anchor='center', relx=0.5, rely=0.5)

    def Clear_Screen(self):
        for widget in self.frame_1.winfo_children():
            widget.destroy()

    def Exit(self):
        self.window.destroy()

    def Open_Image(self):
        self.Clear_Screen()
        self.Image_List.clear()
        self.cur_index = 0

        self.Image_Path =         filedialog.askopenfilename(initialdir = "/",         title = "Select an Image",         filetypes = (("Image files", "*.jpg *.jpeg *.png"),))
        if len(self.Image_Path) != 0:
            self.Image_List.append(self.Image_Path)
            self.Show_Image(0)

    def Open_Images(self):
        self.Clear_Screen()
        self.Image_List.clear()
        self.cur_index = 0

        self.Image_Path =         filedialog.askopenfilenames(initialdir = "/",         title = "Select Images",         filetypes = (("Image files", "*.jpg *.jpeg *.png"),))
        if len(self.Image_Path) != 0:
            for path in self.Image_Path:
                self.Image_List.append(path)
            self.Show_Image(0)

    def Open_Folder(self):
        self.Clear_Screen()
        self.Image_List.clear()
        self.cur_index = 0

        self.directory = filedialog.askdirectory()
        if self.directory != '':
            for filename in glob.iglob(self.directory + '**/*.jpg', recursive=True):
                self.Image_List.append(filename)

            self.Show_Image(0)

    def Show_Image(self, index):
        image = Image.open(self.Image_List[index])
        resized_image = image.resize((self.width, self.height))
        self.img = ImageTk.PhotoImage(resized_image)
        label = Label(self.frame_1, image=self.img)
        label.pack()

    def Prev_Image(self):
        if self.cur_index > 0 and self.cur_index < len(self.Image_List):
            self.cur_index -= 1
            self.Clear_Screen()
            self.Show_Image(self.cur_index)
        else:
            self.cur_index = len(self.Image_List) - 1
            self.Clear_Screen()
            self.Show_Image(self.cur_index)
    def Next_Image(self):
        if self.cur_index < len(self.Image_List) - 1:
            self.cur_index += 1
            self.Clear_Screen()
            self.Show_Image(self.cur_index)
        else:
            self.cur_index = 0
            self.Clear_Screen()
            self.Show_Image(self.cur_index)

if __name__ == "__main__":
    root = Tk()
    img = None
    image_path = None
    obj = Image_Viewer(root)
    root.mainloop()


# In[ ]:





# In[ ]:




