class RiempiDict:
    def __init__(self) -> None:
        self.__dict__ = dict()

    def create_key(self,key):
        self.__dict__[key] = []
    def add_element(self,key,element):
        self.__dict__[key].append(element)
    
    def print_dict(self):
        print(self.__dict__)

    def remove_key(self,key):
        del self.__dict__[key]

    def remove_element(self,key,element):
        self.__dict__[key].remove(element)

mydict = RiempiDict()

mydict.create_key("animali")
mydict.add_element("animali","gatto")
mydict.add_element("animali","gallina")
mydict.add_element("animali","cane")

mydict.create_key("nomi")
mydict.add_element("nomi","laura")
mydict.add_element("nomi","anna")
mydict.add_element("nomi","gianna")

mydict.print_dict()

del_key = input("scrivi la chiave da eliminare ")
key_del_element = input("scrivi la chiave dell'elemento da eliminare ")
name_del_element = input("scrivi il nome dell'elemento da eliminare ")


mydict.remove_key(del_key)
mydict.remove_element(key_del_element,name_del_element)
mydict.print_dict()















