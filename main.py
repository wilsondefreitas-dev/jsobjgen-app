from jsobjgen import *
from jsobjmodel import *
from gui import *

jsobj_model = JsObjModel()
GUI = Gui()

def init():

    try:
        jsobj_model.update( 'config', open('config.js', 'r').read().split('\n') )
        jsobj_gen = JsObjGen( 'config', jsobj_model.config )
    except:
        jsobj_gen = JsObjGen( 'config', jsobj_model.config )

    GUI.generate( jsobj_model.config, jsobj_gen )

if __name__ == '__main__':
    init()

