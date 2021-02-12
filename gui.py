from tkinter import *

class Gui:

    def __init__(self) -> None:

        self.__root = Tk()
        self.__configure()

        pass

    def __configure(self) -> None:

        self.__root.resizable(False, False)
        self.__root.geometry('538x700')
        self.__root.title('jsObj-Gen for Akira')

        top_frame = Frame(self.__root, bg="blue", width=540, height=80)

        button1 = Button(top_frame, text = "Config.js", height=3, width=37)
        button2 = Button(top_frame, text = "Structure.js", height=3, width=37)

        button1.grid(row=0,column=0)
        button2.grid(row=0,column=1)

        top_frame.pack()

        input_main_frame = Frame(self.__root, bg="blue", width=540, height=600)
        input_main_frame.pack()

        input_frame = Frame(input_main_frame, width=540, height=50)
        input_frame.pack()

        label = Label(input_frame, text = "Modo Navegação:", height=2, width=20)
        entry = Entry(input_frame, width=37)

        label.grid(column=0)
        entry.grid(column=1)

        label = Label(input_frame, text = "Modo Navegação:", height=2, width=20)
        entry = Entry(input_frame, width=37)

        label.grid(column=0)
        entry.grid(column=1)
        label = Label(input_frame, text = "Modo Navegação:", height=2, width=20)
        entry = Entry(input_frame, width=37)

        label.grid(column=0)
        entry.grid(column=1)

        label = Label(input_frame, text = "Modo Navegação:", height=2, width=20)
        entry = Entry(input_frame, width=37)

        label.grid(column=0)
        entry.grid(column=1)
        label = Label(input_frame, text = "Modo Navegação:", height=2, width=20)
        entry = Entry(input_frame, width=37)

        label.grid(column=0)
        entry.grid(column=1)

        label = Label(input_frame, text = "Modo Navegação:", height=2, width=20)
        entry = Entry(input_frame, width=37)

        label.grid(column=0)
        entry.grid(column=1)
        label = Label(input_frame, text = "Modo Navegação:", height=2, width=20)
        entry = Entry(input_frame, width=37)

        label.grid(column=0)
        entry.grid(column=1)

        label = Label(input_frame, text = "Modo Navegação:", height=2, width=20)
        entry = Entry(input_frame, width=37)

        label.grid(column=0)
        entry.grid(column=1)
        label = Label(input_frame, text = "Modo Navegação:", height=2, width=20)
        entry = Entry(input_frame, width=37)

        label.grid(column=0)
        entry.grid(column=1)

        label = Label(input_frame, text = "Modo Navegação:", height=2, width=20)
        entry = Entry(input_frame, width=37)

        label.grid(column=0)
        entry.grid(column=1)
        label = Label(input_frame, text = "Modo Navegação:", height=2, width=20)
        entry = Entry(input_frame, width=37)

        label.grid(column=0)
        entry.grid(column=1)

        label = Label(input_frame, text = "Modo Navegação:", height=2, width=20)
        entry = Entry(input_frame, width=37)

        label.grid(column=0)
        entry.grid(column=1)
        label = Label(input_frame, text = "Modo Navegação:", height=2, width=20)
        entry = Entry(input_frame, width=37)

        label.grid(column=0)
        entry.grid(column=1)

        label = Label(input_frame, text = "Modo Navegação:", height=2, width=20)
        entry = Entry(input_frame, width=37)

        label.grid(column=0)
        entry.grid(column=1)
        label = Label(input_frame, text = "Modo Navegação:", height=2, width=20)
        entry = Entry(input_frame, width=37)

        label.grid(column=0)
        entry.grid(column=1)

        label = Label(input_frame, text = "Modo Navegação:", height=2, width=20)
        entry = Entry(input_frame, width=37)

        label.grid(column=0)
        entry.grid(column=1)

        label = Label(input_frame, text = "Modo Navegação:", height=2, width=20)
        entry = Entry(input_frame, width=37)

        label.grid(column=0)
        entry.grid(column=1)

        label = Label(input_frame, text = "Modo Navegação:", height=2, width=20)
        entry = Entry(input_frame, width=37)

        label.grid(column=0)
        entry.grid(column=1)
        label = Label(input_frame, text = "Modo Navegação:", height=2, width=20)
        entry = Entry(input_frame, width=37)

        label.grid(column=0)
        entry.grid(column=1)

        label = Label(input_frame, text = "Modo Navegação:", height=2, width=20)
        entry = Entry(input_frame, width=37)

        label.grid(column=0)
        entry.grid(column=1)
        label = Label(input_frame, text = "Modo Navegação:", height=2, width=20)
        entry = Entry(input_frame, width=37)

        label.grid(column=0)
        entry.grid(column=1)

        label = Label(input_frame, text = "Modo Navegação:", height=2, width=20)
        entry = Entry(input_frame, width=37)

        label.grid(column=0)
        entry.grid(column=1)
        label = Label(input_frame, text = "Modo Navegação:", height=2, width=20)
        entry = Entry(input_frame, width=37)

        label.grid(column=0)
        entry.grid(column=1)

        label = Label(input_frame, text = "Modo Navegação:", height=2, width=20)
        entry = Entry(input_frame, width=37)

        label.grid(column=0)
        entry.grid(column=1)

        # leftframe = Frame(main_frame)
        # leftframe.pack(side=LEFT)
        
        # rightframe = Frame(main_frame)
        # rightframe.pack(side=RIGHT)

        # label = Label(leftframe, text = "Hello world")
        # label.pack()

        # label = Label(rightframe, text = "Hello world")
        # label.pack()



    def show(self) -> None:

        self.__root.mainloop()

    

            
# from tkinter import *

# from tkinter import *  
  
# top = Tk()  
  
# top.geometry("400x250")  
  
# name = Label(top, text = "Name").place(x = 30,y = 50)  
  
# email = Label(top, text = "Email").place(x = 30, y = 90)  
  
# password = Label(top, text = "Password").place(x = 30, y = 130)  
  
# sbmitbtn = Button(top, text = "Submit",activebackground = "pink", activeforeground = "blue").place(x = 30, y = 170)  
  
# e1 = Entry(top).place(x = 80, y = 50)  
  
  
# e2 = Entry(top).place(x = 80, y = 90)  
  
  
# e3 = Entry(top).place(x = 95, y = 130)  
  
# top.mainloop()  