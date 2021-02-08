from attribute import Attr

class JsObjModel:

    def __init__(self) -> None:
        
        self.config = [  

            Attr('Modo de Validação', 'validationMode','boolean', 'true'),
            Attr('Cor Primária', 'primaryColor','string', '#3862A6'),
            Attr('Idioma', 'language','select', 'PT', ['PT', 'ES', 'IN']),
            Attr('Botões Extras', 'extraButtons','array', '', [], [

                Attr('Label', 'label','string', 'Baixar PDF'),
                Attr('Tipo', 'type','select', 'download', ['download', 'open']),
                Attr('Arquivo', 'file','string', 'glossary.html'),

            ])
        
        ]

    def update(self, file_name, file_content) -> None:

        for data in file_content:

            data = data.strip().replace(',', '').split(':')

            for attr in self.config:

                if attr.name == data[0]:

                    if len(attr.subvalue) == 0:

                        attr.value = data[1].replace('"', '')

                    else:

                        for subattr in attr.subvalue:

                            for data in file_content:

                                data = data.strip().replace(',', '').split(':')

                                if data[0] == subattr.name:

                                    subattr.value = data[1].replace('"', '')


                    break 

    