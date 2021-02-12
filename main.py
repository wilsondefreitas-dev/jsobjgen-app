from jsobjgen import *
from jsobjmodel import *
from gui import *

jsobj_model = JsObjModel()
GUI = Gui()

def init():

    try:
        jsobj_model.update( 'config', open('config.js', 'r').read().split('\n') )
        new_file = JsObjGen( 'config', jsobj_model.config )
    except:
        new_file = JsObjGen( 'config', jsobj_model.config )

    GUI.show()

if __name__ == '__main__':
    init()

