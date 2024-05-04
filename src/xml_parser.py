import xml.etree.ElementTree as ET
from .simple_xml_element import *
from .complex_xml_element import *

# Clase de lector de XML
class XmlParser:
    def __init__(self, file_path):
        self.tree = ET.parse(file_path)
        self.root = self.tree.getroot()

    def get_schema_details(self):
        details = "\nDetalles del XML:\n\n"
        for element in self.root:
            if len(element) > 0:
                xml_element = ComplexXmlElement(element)
            else:
                xml_element = SimpleXmlElement(element)
            details += f"  {xml_element.get_details()}\n"
        return details
