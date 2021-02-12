from tkinter import *
import PySimpleGUI as sg

class Gui:

    def __init__(self) -> None:

        self.__configInputElements = []

        pass

    def generate(self, js_obj) -> None:

        sg.theme('LightBrown1')

        self.generateInputLayout(js_obj)
        tab2_layout = [[sg.T('This is inside tab 2')]]  

        layout = [ 
                   [ sg.TabGroup( [ [ sg.Tab('Config.JS', self.__configInputElements), sg.Tab('Structure.js', tab2_layout) ] ], ) ],    
                   [sg.Button('Salvar')]
                 ]    

        # Create the Window
        # window = sg.Window('JSOBJ-GEN 4 Akira', layout)
        window = sg.Window('JSOBJ-GEN 4 Akira').Layout([[sg.Column(layout, size=(450, 700), scrollable=True, vertical_scroll_only=True)]])

        # Event Loop to process "events"
        while True:             
            event, values = window.read()
            if event in (sg.WIN_CLOSED, 'Cancel'):
                break

        window.close()


    def generateInputLayout(self, js_obj, subvalue=[]) -> list:

        obj_to_read = []

        if (len(subvalue) > 0): 
            obj_to_read = subvalue
        else: 
            obj_to_read = js_obj

        for data in obj_to_read:

            print(data.label)

            if data.type == 'boolean':

                self.__configInputElements.append( [ sg.Text(data.label, tooltip=data.tip), sg.Checkbox('Ativar', tooltip=data.tip) ] )

            elif data.type == 'string':

                self.__configInputElements.append( [sg.Text(data.label, tooltip=data.tip), sg.InputText(size=(15, 15), default_text=data.value)] )

            elif data.type == 'colorpicker':

                self.__configInputElements.append( [sg.Text(data.label, tooltip=data.tip), sg.InputText(size=(15, 15), default_text=data.value, tooltip=data.tip), sg.ColorChooserButton('Escolher Cor') ] )
                
            elif data.type == 'logochooser':

                self.__configInputElements.append( [ sg.Text(data.label, tooltip=data.tip), sg.Checkbox('Ativar', tooltip=data.tip), sg.FileBrowse('Escolher Logo') ] )

            elif data.type == 'select':

                self.__configInputElements.append( [sg.Text(data.label, tooltip=data.tip), sg.Combo(data.options, default_value=data.value, size=(10, 10), readonly=True, tooltip=data.tip)] )

            elif data.type == 'array':

                self.__configInputElements.append([sg.Text(data.label + ' ' + ('-'*80), tooltip=data.tip)])
                self.generateInputLayout(js_obj, subvalue=data.subvalue) 

            elif data.type == 'add_button':

                self.__configInputElements.append([sg.Button(data.label, tooltip=data.tip)])