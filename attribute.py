class Attr:

    def __init__(self, label, name, type, value, options = [], subvalue = [], tip='') -> None:

        self.__label = label
        self.__name = name
        self.__type = type
        self.__value = value
        self.__options = options
        self.__subvalue = subvalue
        self.__tip = tip

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
        