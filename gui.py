import PySimpleGUI as sg
from jsobjgen import *
from attribute import *
from shutil import *


class Gui:

    def __init__(self) -> None:

        self.__configInputElements = []
        self.__js_obj = None
        self.__main_layout = None

    def generate(self, js_obj, jsobj_gen) -> None:

        self.__configInputElements = []
        self.__js_obj = js_obj

        sg.theme('LightBrown1')

        self.generateInputLayout(self.__js_obj)

        def tab2_layout(): return [[sg.T('This is inside tab 2')]] 
        def tab3_layout(): return [[sg.T('This is inside tab 3')]]  

        self.__main_layout = [ 
                   [ sg.TabGroup( [ [ 
                       sg.Tab('Config.JS', self.__configInputElements), 
                       sg.Tab('Structure.js', tab2_layout()), 
                       sg.Tab('Glossary.js', tab3_layout()) ] ], ) 
                    ],    
                   [sg.Button('Salvar')]
                 ]    

        window = sg.Window('JSOBJ-GEN 4 Akira').Layout([[sg.Column(self.__main_layout, size=(450, 543), scrollable=True, vertical_scroll_only=True)]])

        while True:     

            event, values = window.read()
    
            # pega dados dos input
            for data in self.__js_obj:

                try:
                    if len(data.subvalue) == 0:

                        data.value =  str(values['{}'.format(data.id)]).lower() if (data.type == 'boolean' or data.type ==  'boolean_and_chooser' ) else values['{}'.format(data.id)]

                    else:

                        for subattr in data.subvalue:

                            for _value in values:

                                if type(_value) == str:
                                    
                                    if str(subattr.id) in _value and '_button' not in _value:

                                        if subattr.name == 'file':
                                            subattr.value = values[_value].split('/')[len(values[_value].split('/'))-1]
                                        else:
                                            subattr.value = values[_value]
                                        
                            
                except: pass
            
            if event in (sg.WIN_CLOSED, 'Cancel'):
                break

            elif event == 'add_button':

                new_list = []

                for index in range(len(data.add_model)):

                    new_list.insert(len(data.subvalue)-1, 
                        Attr( 
                            data.add_model[index]['label'], 
                            data.add_model[index]['name'], 
                            data.add_model[index]['type'], 
                            data.add_model[index]['value'], 
                            tip=data.add_model[index]['tip'], 
                            object_init=data.add_model[index]['object_init'], 
                            object_end=data.add_model[index]['object_end'] 
                        ) 
                    )
                
                data.subvalue.append( new_list )

                window.hide()
                self.generate( self.__js_obj, jsobj_gen )

            elif event == 'Salvar':

                for _value in values:

                    if type(_value) == str:

                        if '_inputfile' in _value and values[_value] != '':

                            if 'logo' in _value:

                                copyfile(values[_value], './img/logo.png')

                            else:

                                if len(values[_value].split('/')) > 1:
                                
                                    copyfile(values[_value], './files/{}'.format(values[_value].split('/')[len(values[_value].split('/'))-1]))
                print(values)

                # jsobj_gen.saveJsFile()

            elif event == 'Excluir':
                print('excluindo o bang!')
                print(self.__configInputElements)

            else:
                try:
                    window.Element('{}'.format(event+'_button')).Update( disabled=( values['{}'.format(event)] == False ) )
                except: pass

        window.close()

    def generateInputLayout(self, js_obj, subvalue=[]) -> list:

        obj_to_read = []
        sub_append = []

        if (len(subvalue) > 0): 
            obj_to_read = subvalue
        else: 
            obj_to_read = js_obj

        for data in obj_to_read:

            if type(data) == list:

                new_list = []
                
                for value in data:
                    print(value)

                    new_list.append( self.get_elements_group(value, js_obj) )

                sub_append.append( sg.Frame('', new_list, font='Any 12', title_color='blue') )

            else:

                elements_group = self.get_elements_group(data, js_obj)
                self.__configInputElements.append( elements_group )
        
        
        if  obj_to_read == subvalue and len(subvalue) > 1: 
            self.__configInputElements.append( sub_append )

    def get_elements_group(self, data, js_obj) -> list:

        elements_group = []

        if data.type == 'boolean':

            elements_group = [ 
                    sg.Text(data.label, tooltip=data.tip), 
                    sg.Checkbox('', tooltip=data.tip, key=('{}'.format(data.id)), default=(data.value == 'true') ) 
                    
                ] 

        elif data.type == 'string':

            elements_group = [
                    sg.Text(data.label, tooltip=data.tip), 
                    sg.InputText(size=(15, 15), default_text=data.value, key=('{}'.format(data.id))),
                    sg.Button('X',  button_color='white on red')
                    
                ] 

        elif data.type == 'colorpicker':

            elements_group = [
                    sg.Text(data.label, tooltip=data.tip), 
                    sg.InputText(size=(15, 15), default_text=data.value, tooltip=data.tip, key=('{}'.format(data.id))), 
                    sg.ColorChooserButton('Escolher Cor', target=('{}'.format(data.id))) 
                
                ]
            
        elif data.type == 'boolean_and_chooser':

            elements_group = [ 
                    sg.Text(data.label, tooltip=data.tip), 

                    sg.Checkbox('', enable_events=True, tooltip=data.tip, key=('{}'.format(data.id)), default=(data.value == 'true')), 

                    sg.FileBrowse('Escolher Arquivo', key='{}_button'.format(data.id), target=('{}_inputfile'.format(data.name)), file_types=(("Png Files", "*.png"),("Jpg Files", "*.jpg"),), disabled=data.value == 'false'),

                    sg.InputText(size=(15, 15), tooltip=data.tip,disabled=True, key=('{}_inputfile'.format(data.name)))
                
                ] 

        elif data.type == 'string_and_file_chooser':

            elements_group = [ 
                    sg.Text(data.label, tooltip=data.tip),

                    sg.InputText(data.value, size=(15, 15), tooltip=data.tip, disabled=True, key=('{}_inputfile'.format(data.id))),

                    sg.FileBrowse('Escolher Arquivo', key='{}_button'.format(data.id), target=('{}_inputfile'.format(data.id)), file_types=(("Png Files", "*.png"),("Jpg Files", "*.jpg"),), disabled=data.value == 'false') 
                
                ] 

        elif data.type == 'select':

            elements_group = [
                    sg.Text(data.label, tooltip=data.tip), 
                    sg.Combo(data.options, default_value=data.value, size=(10, 10), readonly=True, tooltip=data.tip, key=('{}'.format(data.id)))
                ] 

        elif data.type == 'array':

            self.__configInputElements.append( [ sg.Text(data.label + ' ' + ('-'*70), tooltip=data.tip) ] )
            self.generateInputLayout(js_obj, subvalue=data.subvalue) 

        elif data.type == 'add_button':

            # elements_group = [ sg.Button(data.label, tooltip=data.tip, key=('{}'.format(data.type))) ]
            self.__configInputElements.append( [ sg.Button(data.label, tooltip=data.tip, key=('{}'.format(data.type))) ] )

        return elements_group