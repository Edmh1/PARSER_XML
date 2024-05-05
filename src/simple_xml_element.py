from .xml_element import *

# Clase concreta para elementos XML con contenido simple
class SimpleXmlElement(XmlElement):

    # Polimorfismo: tipo(overriding)
    def get_details(self):
        attributes = self.get_attributes()
        items = ""                                        
        for key, value in attributes.items():              
            items += f"{key.capitalize()} = {value}, "       
        return items                     