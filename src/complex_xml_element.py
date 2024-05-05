from .xml_element import *
from .simple_xml_element import *

# Clase concreta para elementos XML con contenido complejo
class ComplexXmlElement(XmlElement):

    # Polimorfismo: tipo(overriding, overloading)
    def get_details(self, tab):
        attributes = self.get_attributes()
        items = ""
        for key, value in attributes.items():               
            items += f"{key.capitalize()} = {value},"                                                  

        for child in self.get_element():
            if len(child) > 0:
                child_element = ComplexXmlElement(child)
                items += f"\n{'\t' * tab}{child_element.get_details(tab + 1)}"  
            else:
                child_element = SimpleXmlElement(child)
                items += f"\n{'\t' * tab}{child_element.get_details()}"
        return items

