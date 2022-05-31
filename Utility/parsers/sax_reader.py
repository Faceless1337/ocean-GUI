import xml.sax as sax


class XmlReader(sax.ContentHandler):
    def __init__(self) -> None:
        super().__init__()
        self.age = None
        self.male = None
        self.hp = None
        self.y = None
        self.x = None
        self.type = None
        self.current = None
        self.table_data = []
        self.animal_data = []
        self.parser = sax.make_parser()

    def startElement(self, name, attrs):
        """
        Rewritten function from inherited class which use as start parser element
        :param name: current element name
        :param attrs: attributes (don't used)
        :return: None
        """
        self.current = name
        if name == "animal":
            pass

    def characters(self, content) -> None:
        """
        Also rewritten function that perform getting data characters
        :param content: character
        :return: None
        """
        if self.current == "type":
            self.type = content
        elif self.current == "x":
            self.x = content
        elif self.current == "y":
            self.y = content
        elif self.current == "hp":
            self.hp = content
        elif self.current == "male":
            self.male = content
        elif self.current == "age":
            self.age = content

    def endElement(self, name) -> None:
        """
        Rewritten function from inherited class which use as end parser element
        :param name:
        :return: None
        """
        if self.current == "type":
            self.animal_data.append(self.type)
        elif self.current == "x":
            self.animal_data.append(self.x)
        elif self.current == "y":
            self.animal_data.append(self.y)
        elif self.current == "hp":
            self.animal_data.append(self.hp)
        elif self.current == "male":
            self.animal_data.append(self.male)
        elif self.current == "age":
            self.animal_data.append(self.age)
        if len(self.animal_data) == 6:
            self.table_data.append(tuple(self.animal_data))
            self.animal_data = []

        self.current = ""
