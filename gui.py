import PySimpleGUI as sg
from jsobjgen import *

class Gui:

    def __init__(self) -> None:

        self.__configInputElements = []
        self.__js_obj = None
        self.__main_layout = None

        pass

    def generate(self, js_obj, jsobj_gen) -> None:

        self.__configInputElements =[]
        self.__js_obj = js_obj

        sg.theme('LightBrown1')

        self.generateInputLayout(js_obj)

        def tab2_layout(): return [[sg.T('This is inside tab 2')]] 
        def tab3_layout(): return [[sg.T('This is inside tab 3')]]  

        self.__main_layout = [ 
                   [ sg.TabGroup( [ [ sg.Tab('Config.JS', self.__configInputElements), sg.Tab('Structure.js', tab2_layout()), sg.Tab('Glossary.js', tab3_layout()) ] ], ) ],    
                   [sg.Button('Salvar')]
                 ]    

        window = sg.Window('JSOBJ-GEN 4 Akira').Layout([[sg.Column(self.__main_layout, size=(450, 543), scrollable=True, vertical_scroll_only=True)]])

        while True:     
            event, values = window.read()

            # pega dados dos input
            for data in js_obj:
                try:
                    if len(data.subvalue) == 0:
                        data.value =  str(values['_{}_'.format(data.name)]).lower() if (data.type == 'boolean') else values['_{}_'.format(data.name)]
                    else:
                        for subattr in data.subvalue:

                            subattr.value = values['_{}_'.format(subattr.name)]
                            
                except: pass

            if event == '_add_button_':

                for value in data.add_model:
                    data.subvalue.insert(0, value)

                window.hide()
                self.generate( js_obj, jsobj_gen )

            if event == 'Salvar':
                jsobj_gen.saveJsFile()

            if event in (sg.WIN_CLOSED, 'Cancel'):
                break

        window.close()

    def generateInputLayout(self, js_obj, subvalue=[]) -> list:

        obj_to_read = []

        if (len(subvalue) > 0): obj_to_read = subvalue
        else: obj_to_read = js_obj

        for data in obj_to_read:

            if data.type == 'boolean':

                self.__configInputElements.append( [ sg.Text(data.label, tooltip=data.tip), sg.Checkbox('Ativar', tooltip=data.tip, key=('_{}_'.format(data.name)), default=(data.value == 'true') ) ] )

            elif data.type == 'string':

                self.__configInputElements.append( [sg.Text(data.label, tooltip=data.tip), sg.InputText(size=(15, 15), default_text=data.value, key=('_{}_'.format(data.name)))] )

            elif data.type == 'colorpicker':

                self.__configInputElements.append( [sg.Text(data.label, tooltip=data.tip), sg.InputText(size=(15, 15), default_text=data.value, tooltip=data.tip, key=('_{}_'.format(data.name))), sg.ColorChooserButton('Escolher Cor') ] )
                
            elif data.type == 'boolean_and_chooser':

                self.__configInputElements.append( [ sg.Text(data.label, tooltip=data.tip), sg.Checkbox('Ativar', tooltip=data.tip, key=('_{}_'.format(data.name))), sg.FileBrowse('Escolher Logo') ] )

            elif data.type == 'string_and_file_chooser':

                self.__configInputElements.append( [ sg.Text(data.label, tooltip=data.tip), sg.Checkbox('Ativar', tooltip=data.tip, key=('_{}_'.format(data.name))), sg.FileBrowse('Escolher Arquivo') ] )

            elif data.type == 'select':

                self.__configInputElements.append( [sg.Text(data.label, tooltip=data.tip), sg.Combo(data.options, default_value=data.value, size=(10, 10), readonly=True, tooltip=data.tip, key=('_{}_'.format(data.name)))] )

            elif data.type == 'array':

                self.__configInputElements.append([sg.Text(data.label + ' ' + ('-'*80), tooltip=data.tip)])
                self.generateInputLayout(js_obj, subvalue=data.subvalue) 

            elif data.type == 'add_button':

                self.__configInputElements.append([sg.Button(data.label, tooltip=data.tip, key=('_{}_'.format(data.type)))])