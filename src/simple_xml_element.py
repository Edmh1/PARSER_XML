from .xml_element import *

# Clase concreta para elementos XML con contenido simple
class SimpleXmlElement(XmlElement):

    #(TAREA: IMPLEMENTAR METODO DE LA CLASE CONCRETA)
    def get_details(self):
        details = self.get_attributes()
        items = ""                                      #Inicializamos una variable que guarde los items  
        for key, value in details.items():              #Iteramos por cada una de las llaves que tenga el diccionario
            items += f"{key.capitalize()} = {value} "   #Agregamos la llave y el valor a la variable items
        return items                     