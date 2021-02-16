class Attr:

    def __init__(self, label, name, type, value, options = [], subvalue = [], tip='', add_model=[], object_init=False, object_end=False) -> None:

        self.__label = label
        self.__name = name
        self.__type = type
        self.__value = value
        self.__options = options
        self.__subvalue = subvalue
        self.__tip = tip
        self.__add_model = add_model
        self.__object_init = object_init
        self.__object_end = object_end

        print(self.__label)
        print(self.__add_model)

    @property
    def label(self) -> str:
        return self.__label
    
    @property
    def name(self) -> str:
        return self.__name

    @property
    def type(self) -> str:
        return self.__type

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value) -> None:
        self.__value = value

    @property
    def options(self) -> str:
        return self.__options

    @property
    def subvalue(self) -> str:
        return self.__subvalue

    @property
    def tip(self) -> str:
        return self.__tip

    @property
    def add_model(self) -> list:
        return self.__add_model

    @property
    def object_init(self) -> list:
        return self.__object_init

    @property
    def object_end(self) -> list:
        return self.__object_end

        