# from jsobjgen import JsObjGen
# from jsobjmodel import JsObjModel

# jsobj_model = JsObjModel()

# def init():

#     try:
#         jsobj_model.update( 'config', open('config.js', 'r').read().split('\n') )
#         new_file = JsObjGen( 'config', jsobj_model.config )
#     except:
#         new_file = JsObjGen( 'config', jsobj_model.config )

# if __name__ == '__main__':
#     init()
    



import tkinter as tk # Python 3.x Version

root = tk.Tk()

frame_a = tk.Frame()

label = tk.Label(master=frame_a, text="Name")

entry = tk.Entry(master=frame_a)

button = tk.Button(master=frame_a, text="Salvar")

label.pack()
entry.pack()
button.pack()
frame_a.pack()

root.mainloop()