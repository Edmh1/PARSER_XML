from .xml_element import *
from .simple_xml_element import *

# Clase concreta para elementos XML con contenido complejo
class ComplexXmlElement(XmlElement):

    #(TAREA: IMPLEMENTAR METODO DE LA CLASE CONCRETA)
    def get_details(self):
        attributes = self.get_attributes()                      #Obtenemos el diccionario con los atributos
        items = ""
        details = ""

        if attributes:                                          #Si la vairbale 'atributos' tiene elementos se cumple el if
            for key, value in attributes.items():               #Obtenemos las llaves del diccionario
                items += f"{key.capitalize()} = {value} "                                                   
        
        if items == "":
            details = f"\n"
        else:                                                   #Inicializa la variable 'details' con los detalles de los atributos 
            details = f"{items}\n"
                                  
        for child in self.element:                              #Al ser un elemento complejo iteramos en cada uno de sus hijos
            if len(child) > 0:                                  #Si la longitud del hijo es mayor a 0 es un elemento complejo
                child_element = ComplexXmlElement(child)
            else:
                child_element = SimpleXmlElement(child)         #Si la longitud es 0 el hijo es un elemento simple
            details += f"\t{child_element.get_details()}\n"       #Añadimos los detalles del hijo al string del elemento complejo mayor
        return details
