class JsObjGen: 
    
    def __init__(self, file_name, js_obj) -> None:
        
        self.__js_obj = js_obj
        self.__file_name = file_name

    @property
    def js_obj(self): return self.__js_obj

    @property
    def file_name(self): return self.__file_name

    def saveJsFile(self):

        new_file = open('{}.js'.format(self.file_name), 'w', encoding='UTF-8')
        new_file.write('var {}'.format(self.file_name)) 
        new_file.write('= {\n')
        
        for data in self.js_obj:
            new_file.write( self.__format_attr_value(data) )
        
        new_file.write('}')
        new_file.close()
    
    def __format_attr_value(self, data):
        
        if data['type'] == 'boolean':
            return '    {0}:{1},\n'.format( data['attr'], data['value'] )
        if data["type"] == 'string' or data["type"] == 'select' :
            return '    {0}:"{1}",\n'.format( data['attr'], data['value'] )
        if data['type'] == 'array':
            new_str = ''

            for subvalue in data['subvalue']:
                new_str += ( '    {}'.format( self.__format_attr_value(subvalue) ) ) 

            return '    {0}:[{1}\n{2}    {3}],\n'.format( data['attr'], '{', new_str, '}' )
        else: 
            return 'ola'

