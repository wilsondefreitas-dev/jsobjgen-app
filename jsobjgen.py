class JsObjGen: 
    
    def __init__(self, file_name, js_obj) -> None:
        
        self.__js_obj = js_obj
        self.__file_name = file_name

    def saveJsFile(self):

        new_file = open('{}.js'.format(self.file_name), 'w', encoding='UTF-8')
        new_file.write('var {}'.format(self.file_name)) 
        new_file.write('= {\n')
        
        for data in self.js_obj:
            new_file.write( self.__format_attr_value(data) )
        
        new_file.write('}')
        new_file.close()

        return new_file
    
    def __format_attr_value(self, data):

        def check_obj_init() -> str: 
            return data.object_init 

        def check_obj_end() -> str: 
            return data.object_end 
        
        if data.type == 'boolean' or data.type == 'boolean_and_chooser':
            return '    {0}:{1},\n'.format( data.name, data.value )
        if data.type == 'string' or data.type == 'select' or data.type == 'colorpicker' or data.type == 'string_and_file_chooser':
            return '    {2}{0}:"{1}"{3},\n'.format( data.name, data.value, check_obj_init(), check_obj_end())
        if data.type == 'array':
            new_str = ''

            for subvalue in data.subvalue:
                print(subvalue.name, ':', subvalue.value)
                new_str += ( '    {}'.format( self.__format_attr_value(subvalue) ) ) 

            return '    {0}:[\n{2}    ],\n'.format( data.name, '{', new_str, '}' )
        else: 
            return ''

    @property
    def js_obj(self): return self.__js_obj

    @property
    def file_name(self): return self.__file_name