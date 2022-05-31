from parsers.dom_writer import XmlWriter

start_data = [
    ("Plankton", 1,  1,  2, "none", 0), ("Plankton", 1,  10,  2, "none", 0), ("Plankton", 2,  2,  2, "none", 0), ("Plankton", 2,  10,  2, "none", 0), ("Plankton", 3,  7,  2,"none",  0), ("Plankton", 5,  8,  2, "none", 0), ("Plankton", 6,  3,  2, "none", 0), ("Plankton", 6,  6,  2,  "none", 0), ("Plankton", 6,  9,  2, "none", 0), ("Plankton", 7,  2,  2, "none", 0), ("Plankton", 7,  5,  2, "none", 0), ("Plankton", 7,  7,  2, "none", 0), ("Plankton", 8,  3,  2, "none", 0), ("Plankton", 8,  10,  2, "none", 0), ("Plankton", 9,  5,  2, "none", 0), ("Plankton", 10,  3,  2, "none", 0), ("Plankton", 10,  5,  2, "none", 0), ("Plankton", 10,  7,  2, "none", 0), ("Plankton", 10,  8,  2, "none", 0), ("Plankton", 10,  9,  2, "none", 0), ("Plankton", 10,  10,  2, "none", 0), ("Shark", 4,  7,  5,  True,  0), ("Shark", 5,  4,  5,  True,  0), ("Shark", 6,  2,  5,  True,  0), ("Shark", 6,  5,  5,  True,  0), ("Shark", 8,  4,  5,  True,  0), ("Shark", 9,  7,  5,  True,  0),  ("FantomAnimal", 0,  0, "none", "none", "none"), ("FantomAnimal", 0,  1, "none", "none", "none"), ("FantomAnimal", 0,  2, "none", "none", "none"), ("FantomAnimal", 0,  3, "none", "none", "none"), ("FantomAnimal", 0,  4, "none", "none", "none"), ("FantomAnimal", 0,  5, "none", "none", "none"), ("FantomAnimal", 0,  6, "none", "none", "none"), ("FantomAnimal", 0,  7, "none", "none", "none"), ("FantomAnimal", 0,  8, "none", "none", "none"), ("FantomAnimal", 0,  9, "none", "none", "none"), ("FantomAnimal", 0,  10, "none", "none", "none"), ("FantomAnimal", 1,  0, "none", "none", "none"), ("FantomAnimal", 1,  2, "none", "none", "none"), ("FantomAnimal", 1,  3, "none", "none", "none"), ("FantomAnimal", 1,  4, "none", "none", "none"), ("FantomAnimal", 1,  5, "none", "none", "none"), ("FantomAnimal", 1,  6, "none", "none", "none"), ("FantomAnimal", 1,  8, "none", "none", "none"), ("FantomAnimal", 1,  9, "none", "none", "none"), ("FantomAnimal", 2, 0, "none", "none", "none"), ("FantomAnimal", 2,  1, "none", "none", "none"), ("FantomAnimal", 2,  3, "none", "none", "none"), ("FantomAnimal", 2,  5, "none", "none", "none"), ("FantomAnimal", 2,  6, "none", "none", "none"), ("FantomAnimal", 2,  7, "none", "none", "none"), ("FantomAnimal", 2,  8, "none", "none", "none"), ("FantomAnimal", 2,  9, "none", "none", "none"), ("FantomAnimal", 3,  0, "none", "none", "none"), ("FantomAnimal", 3,  1, "none", "none", "none"), ("FantomAnimal", 3,  2, "none", "none", "none"), ("FantomAnimal", 3,  3, "none", "none", "none"), ("FantomAnimal", 3,  5, "none", "none", "none"), ("FantomAnimal", 3,  6, "none", "none", "none"), ("FantomAnimal", 3,  8, "none", "none", "none"), ("FantomAnimal", 3,  9, "none", "none", "none"), ("FantomAnimal", 3,  10, "none", "none", "none"), ("FantomAnimal", 4,  0, "none", "none", "none"), ("FantomAnimal", 4,  1, "none", "none", "none"), ("FantomAnimal", 4,  2, "none", "none", "none"), ("FantomAnimal", 4,  6, "none", "none", "none"), ("FantomAnimal", 4,  8, "none", "none", "none"), ("FantomAnimal", 4,  9, "none", "none", "none"), ("FantomAnimal", 4,  10, "none", "none", "none"), ("FantomAnimal", 5,  0, "none", "none", "none"), ("FantomAnimal", 5,  5, "none", "none", "none"), ("FantomAnimal", 5,  9, "none", "none", "none"), ("FantomAnimal", 5,  10, "none", "none", "none"), ("FantomAnimal", 6,  0, "none", "none", "none"), ("FantomAnimal", 6,  1, "none", "none", "none"), ("FantomAnimal", 6,  4, "none", "none", "none"), ("FantomAnimal", 6,  7, "none", "none", "none"), ("FantomAnimal", 6,  8, "none", "none", "none"), ("FantomAnimal", 6,  10, "none", "none", "none"), ("FantomAnimal", 7,  0, "none", "none", "none"), ("FantomAnimal", 7,  1, "none", "none", "none"), ("FantomAnimal", 7,  3, "none", "none", "none"), ("FantomAnimal", 7,  4, "none", "none", "none"), ("FantomAnimal", 7,  8, "none", "none", "none"), ("FantomAnimal", 7,  10, "none", "none", "none"), ("FantomAnimal", 8,  0, "none", "none", "none"), ("FantomAnimal", 8,  2, "none", "none", "none"), ("FantomAnimal", 8,  5, "none", "none", "none"), ("FantomAnimal", 8,  7, "none", "none", "none"), ("FantomAnimal", 8,  8, "none", "none", "none"), ("FantomAnimal", 8,  9, "none", "none", "none"), ("FantomAnimal", 9,  0, "none", "none", "none"), ("FantomAnimal", 9,  2, "none", "none", "none"), ("FantomAnimal", 9,  3, "none", "none", "none"), ("FantomAnimal", 9,  4, "none", "none", "none"), ("FantomAnimal", 9,  8, "none", "none", "none"), ("FantomAnimal", 9,  9, "none", "none", "none"), ("FantomAnimal", 9,  10, "none", "none", "none"), ("FantomAnimal", 10,  0, "none", "none", "none"), ("FantomAnimal", 10,  1, "none", "none", "none"), ("FantomAnimal", 10,  2, "none", "none", "none"), ("FantomAnimal", 10,  4, "none", "none", "none"), ("FantomAnimal", 10,  6, "none", "none", "none"), ("Killerwhale", 3,  4,  6,  True,  0), ("Killerwhale", 4,  3,  6,  True,  0), ("Killerwhale", 4,  5,  6,  True,  0), ("Killerwhale", 5,  1,  6,  True,  0), ("Killerwhale", 7,  6,  6,  True,  0), ("Killerwhale", 9,  1,  6,  True,  0), ("Dolphin", 1,  7,  4,  True,  0), ("Dolphin", 2,  4,  4,  True,  0), ("Dolphin", 4,  4,  4,  True,  0), ("Dolphin", 5,  2,  4,  True,  0), ("Dolphin", 5,  3,  4,  True,  0), ("Dolphin", 5,  6,  4,  True,  0), ("Dolphin", 5,  7,  4,  True,  0), ("Dolphin", 7,  9,  4,  True,  0), ("Dolphin", 8,  1,  4,  True,  0), ("Dolphin", 8,  6,  4,  True,  0), ("Dolphin", 9,  6,  4,  True,  0)
]


class XMLGenerator:
    def __init__(self):
        pass

    @staticmethod
    def generate_xml_files() -> None:
        """
        Create XML file with start data
        :return: None
        """
        path = f"../XML/default.xml"
        data_dict = {}
        with open(path, 'w') as file:
            dom_writer = XmlWriter(path)
            id = 0
            for element in start_data:
                for element in start_data:
                   # print(element)
                    type, x, y, hp, male, age = element
                    data_dict["type"] = type
                    data_dict["x"] = str(x)
                    data_dict["y"] = str(y)
                    data_dict["hp"] = str(hp)
                    data_dict["male"] = str(male)
                    data_dict["age"] = str(age)
                    dom_writer.create_animals(data_dict)
        # creating xml file using dom parser
        dom_writer.create_xml_file()


def main():
    XMLGenerator.generate_xml_files()


if __name__ == "__main__":
    main()
