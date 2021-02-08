from jsobjgen import JsObjGen
# import tkinter as tk # Python 3.x Version

# root = tk.Tk()

# label = tk.Label(root, text="Hello World!") # Create a text label
# label.pack(padx=200, pady=200) # Pack it into the window

# root.mainloop()

print('start!')


try:
    new_file = open('config.js', 'r')
    print(new_file.read())
except:
    new_ref = JsObjGen( 'config', ( 
        { 'attr':'validationMode', 'type':'boolean', 'value':'true' },
        { 'attr':'primaryColor', 'type':'string', 'value':'#3862A6' },
        { 'attr':'language', 'type':'select', 'value':'PT', 'options':['PT', 'ES', 'IN'] },
        { 'attr':'extraButtons', 'type':'array', 'value':'', 'subvalue':[
            { 'attr':'label', 'type':'string', 'value':'Teste Download' },
            { 'attr':'type', 'type':'select', 'value':'download', 'options':['download', 'open'] },
            { 'attr':'file', 'type':'string', 'value':'glossary.html' }
        ]}
    ))

    new_ref.saveJsFile()