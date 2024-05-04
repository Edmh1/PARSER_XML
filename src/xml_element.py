from abc import ABC, abstractmethod

# Clase abstracta para los elementos xml
class XmlElement(ABC):
    def __init__(self, element):
        self.element = element

    def get_name(self):
        return self.element.tag

    def get_attributes(self):
        return self.element.attrib

    # Polimorfismo: tipo(overriding)
    @abstractmethod
    def get_details(self):
        raise NotImplementedError("Debes implementar este metodo en las clases hijas")