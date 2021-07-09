from PySimpleGUI.PySimpleGUI import Print
from attribute import Attr

class JsObjModel:

    def __init__(self) -> None:
        
        self.config = [  

            # E S T I L O

            Attr('Topo', 'showTop','boolean', 'true', tip='Ativar topo do player.'),

            Attr('Logo no Topo', 'logoOn','boolean_and_chooser', 'true', tip='Ativar o logo no topo do player. Inserir logo na pasta "_content/images". IMPORTANTE: salvar logo com altura máxima de 32 px.'),

            Attr('Cor Primária', 'primaryColor','colorpicker', '#3862A6', tip='Definir cor primária do player em hexadecimal ou rgb. Indicado usar uma cor escura.'),

            Attr('Cor Secundária', 'secondaryColor','colorpicker', '#559A73', tip='Definir cor secundária do player em hexadecimal ou rgb. Indicado usar uma cor clara.'),

            # f u n c i o n a l i d a d e s

            Attr('Modo de Validação', 'validationMode','boolean', 'true', tip='Libera a navegação do treinamento, permitindo que o usuário consiga avançar, voltar e navegar a vontade pelo menu. Indicado para validação.'),

            Attr('Legenda', 'subtitleOn','boolean', 'true', tip='Ativar legenda no treinamento. Também ativa o botão de ligar e desligar legenda no menu principal do player.'),

            Attr('Som', 'soundOn','boolean', 'true', tip='Ativar efeitos sonoros e trilhas no treinamento. Também ativa o botão de ligar e desligar sons no menu principal do player.'),

            Attr('Paginação', 'pageNumberOnTop','boolean', 'true', 'Mostrar páginação do treinamento no topo.'),

            Attr('Progresso', 'progressCourse','boolean', 'false', tip='Mostrar progresso do usuário no treinamento em porcentagem no topo.'),

            Attr('Pontuação', 'gameMode','boolean', 'false', tip='Ativar display com pontuação no topo do player. Indicado para games.'),
            
            Attr('Idioma', 'language','select', 'PT', options=['PT', 'ES', 'IN'], tip='Selecionar idioma do Akira.'),

            Attr('API OnePage', 'onePage','boolean', 'false', tip='Integrar com OnePage'),

            Attr('Libras', 'libraOn','boolean', 'false', tip='Ativar os vídeos de apoio que são executados em conjunto com a legenda. Indicado para libras.'),

            Attr('Glossário', 'glossaryOn','boolean', 'false', tip='Ativar glossário.'),

            Attr('Material Complementar', 'extraButtons','array', '', tip='Inserir botões extras no menu e navegação.', subvalue=[

                Attr('Adicionar Novo', None,'add_button', None, tip='Inserir mais um botão.')

            ], add_model=[
                    
                    # Attr('-----> Label', 'label','string', 'Baixar PDF', tip='Definir nome do botão extra.', object_init='{\n'),
                    { 'label': 'Nome do Botão', 'name':'label','type':'string', 'value':'Baixar Material', 'tip':'Definir nome do botão extra', 'object_init': '{', 'object_end': '' },
                    { 'label': '→ Arquivo', 'name':'file','type':'string_and_file_chooser', 'value':'', 'tip':'Definir nome do arquivo da ação escolhida', 'object_init': '', 'object_end': '}' }
                    # Attr('-----> Arquivo', 'file','string_and_file_chooser', 'glossary.html', tip='Definir nome do arquivo da ação escolhida.', object_end='\n}')

            ])
        
        ]

    def update(self, file_name, file_content) -> None:

        startArray = False

        #loop no arquivo
        for data in file_content:

            data = data.strip().replace(',', '').split(':')

            #loop no modelo
            for attr in self.config:

                if attr.name == data[0]:

                    if len(attr.subvalue) == 0:

                        attr.value = data[1].replace('"', '')

                    else:

                        subvalue_index = 0

                        for data2 in file_content:
                            

                            if '[' in data2[len(data2)-1]: startArray = True
                            elif ']' in data2[len(data2)-2:len(data2)]: startArray = False
                            elif '],' in data2[len(data2)-2:len(data2)]: startArray = False

                            data2 = data2.strip().replace(',', '').split(':')

                            if startArray:

                                for index in range(len(attr.add_model)):

                                    if attr.add_model[index]['name'] == data2[0].replace('{', ''):

                                        attr.subvalue.insert(
                                            subvalue_index, 
                                            Attr(attr.add_model[index]['label'], 
                                                 attr.add_model[index]['name'], 
                                                 attr.add_model[index]['type'],  
                                                 data2[1].replace('"', '').replace('}', ''), 
                                                 attr.add_model[index]['tip'], 
                                                 object_init=attr.add_model[index]['object_init'], 
                                                 object_end=attr.add_model[index]['object_end'] ))

                                        subvalue_index += 1
                                    
