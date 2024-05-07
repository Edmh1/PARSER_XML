# Parser_XML

## What is a parser?

In computer technology, a parser is a program that's usually part of a compiler. It receives input in the form of sequential source program instructions, interactive online commands, markup tags or some other defined interface.

Parsers break the input they get into parts such as the nouns (objects), verbs (methods), and their attributes or options. These are then managed by other programming, such as other components in a compiler. A parser may also check to ensure that all the necessary input has been provided.


## About this project

The purpose of this parser is to show in a more readable way the content and structure of an .xml document or xml schema, as well as the specified objectives for the accomplishment of the proposed activity.

For the development of this, we used **python** and the library _xml.etree.ElementTree_, making use of functions like _.parse()_  or _.getRoot()_, in order to obtein the document structure and to be able to access the different elements of the document. 

It is important to know the structure of an xml schema document, so we will show you below how it is structured

- **XML schema definition**

  An infrastructure document that defines the rules and constraints for XML data documents, which are instances of the XSD.

  An XSD contains a set of components, such as declarations and type definitions that specify the structure and semantics of elements and attributes. These components provide documentation about the data and can be used to assess the validity of correctly formatted XML instances.

- **XSD element**

  Declares a named structure that can have instance data in XML documents. The structure of an XSD element can be _simple_ or _complex_. Elements can be declared globally or locally.

  Global elements appear at the top level of a document's schema, which means that the parent must be the schema. They must be unique within the entire schema and can be reused (referenced) in other elements, types or groups. Local elements are found within other elements or complex types.

- **XSD atributte**

  Models data values in an XML schema. It assigns a name to an attribute and associates it with a simple type. XSD attributes can be declared globally or locally.

  Global attributes are top-level components that are contained in an XML schema. They must be unique within the containing schema and can be reused (referenced) in other elements, types or groups. Local attributes are defined within elements or types. They are in the scope of their parent's definitions and cannot be reused in other elements or types.

- **XSD simple type**

  A top-level schema component that defines reusable data types for attributes and simple, text-only elements. It constrains the value of an attribute or element in an XML instance.

  Each simple type is a constraint on another simple type, which is known as its base type, which may be a built-in type or a user-defined type. Therefore, all simple types are direct or indirect derivations of built-in data types.

- **XSD complex type**

  A top-level schema component that defines reusable data types for complex elements. XSD complex types have child elements and attributes and specify constraints on the content of the elements.

  Complex types can be derived from other types by constraint or extension.



## Members

- Castro Sebastián
- Escobar Andrés
- Manotas Eddie
- Navarro Vladimir

