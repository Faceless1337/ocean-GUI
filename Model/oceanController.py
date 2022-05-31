import random
from Model.animals import FantomAnimal
from Model.animals import Plankton
from Model.animals import Killerwhale
from Model.animals import Shark
from Model.animals import Dolphin
from Model.living import Animals
from Model.living import AnimalsType
from Utility.parsers.dom_writer import XmlWriter
from Utility.parsers.sax_reader import XmlReader
import numpy as np
import pandas as pd




class OceanController:
    def __init__(self, size: int):
        self.n: int = size

    @staticmethod
    def getEmptyPosition(ocean, n):
        x = random.randrange(1, n)
        y = random.randrange(1, n)
        while ocean[x][y].getType() != AnimalsType.EMPTY:
            x = random.randrange(1, n)
            y = random.randrange(1, n)
        return [x, y]

    def init(self, ocean: [[]], planktonNumber: int, dolphinNumber: int, sharkNumber: int,
             killerwhaleNumber: int) -> None:
        for i in range(0, self.n):
            for j in range(0, self.n):
                ocean[i][j] = FantomAnimal(i, j)

        for i in range(0, planktonNumber + 1):
            x = self.getEmptyPosition(ocean, self.n)[0]
            y = self.getEmptyPosition(ocean, self.n)[1]
            ocean[x][y] = Plankton(x, y, 2, 0)
        for i in range(0, dolphinNumber + 1):
            x = self.getEmptyPosition(ocean, self.n)[0]
            y = self.getEmptyPosition(ocean, self.n)[1]
            ocean[x][y] = Dolphin(x, y, 4, random.choice([True, False]), 0)
        for i in range(0, sharkNumber + 1):
            x = self.getEmptyPosition(ocean, self.n)[0]
            y = self.getEmptyPosition(ocean, self.n)[1]
            ocean[x][y] = Shark(x, y, 5, random.choice([True, False]), 0)
        for i in range(0, killerwhaleNumber + 1):
            x = self.getEmptyPosition(ocean, self.n)[0]
            y = self.getEmptyPosition(ocean, self.n)[1]
            ocean[x][y] = Killerwhale(x, y, 6, random.choice([True, False]), 0)

    def update(self, paramOcean: [[]]) -> None:
        for i in range(1, self.n - 1):
            for j in range(1, self.n - 1):
                deltaCells = paramOcean[i][j].next(paramOcean)
                if deltaCells:
                    for h in deltaCells:
                        paramOcean[h.getX()][h.getY()] = h

    def deleteOcean(self, paramOcean: []) -> None:
        for i in range(1, self.n - 1):
            for j in range(1, self.n - 1):
                paramOcean[i][j] = None

    def showOcean(self, paramOcean: []) -> None:
        for i in range(1, self.n - 1):
            for j in range(1, self.n - 1):
                if paramOcean[i][j].getType() == AnimalsType.EMPTY:
                    print("E", end=" ")
                if paramOcean[i][j].getType() == AnimalsType.PLANKTON:
                    print("P", end=" ")
                if paramOcean[i][j].getType() == AnimalsType.DOLPHIN:
                    print("D", end=" ")
                if paramOcean[i][j].getType() == AnimalsType.SHARK:
                    print("S", end=" ")
                if paramOcean[i][j].getType() == AnimalsType.KILLERWHALE:
                    print("K", end=" ")
            print()

    def getSizeOfTheOcean(self) -> int:
        return self.n

    def setSizeOfTheOcean(self, size: int) -> None:
        self.n = size

    def addAnimal(self, ocean: [[]]) -> None:
        print("p - plankton")
        print("d - dolphin")
        print("s - shark")
        print("k - killerwhale")
        choice = str(input())
        males = ["male", "female"]
        animals = ["p", "d", "s", "k"]
        while choice not in animals:
            choice = str(input("try more"))

        x = int(input("input x "))
        while x < 1 or x > self.n - 2:
            x = int(input("try more "))
        y = int(input("input y "))
        while y < 1 or y > self.n - 2:
            y = int(input("try more "))

        hp = int(input("input hp "))
        while hp < 1 or hp > 6:
            hp = int(input("try more "))


        if choice == "p":
            age = int(input("input age "))
            while age < 1 or age > 6:
                age = int(input("try more "))
            ocean[x][y] = Plankton(x, y, hp, age)
            return
        else:
            male = str(input("input male "))
            while not male in males:
                male = str(input("try more "))
            if male == "male":
                sex = True
            else:
                sex = False

        age = int(input("input age "))
        while age < 1 or age > 6:
            age = int(input("try more "))

        if choice == "d":
            ocean[x][y] = Dolphin(x, y, hp, sex, age)
            return
        if choice == "s":
            ocean[x][y] = Shark(x, y, hp, sex, age)
            return
        if choice == "k":
            ocean[x][y] = Killerwhale(x, y, hp, sex, age)
            return
        print("invalid letter")

    def killAnimal(self, ocean: []) -> None:
        x = int(input("input x "))
        while x < 1 or x > self.n - 2:
            x = int(input("try more "))
        y = int(input("input y "))
        while y < 1 or y > self.n - 2:
            y = int(input("try more "))
        ocean[x][y] = FantomAnimal(x, y)




class FileReader:
    @classmethod
    def saveToFile(cls, ocean: [[]], path) -> None:
        fout = open('Model/size.txt', 'w')
        fout.write(str(len(ocean)))
        fout.close()
        write = XmlWriter(path)
        data = {}
        for line in ocean:
            for animal in line:
                if animal.getType() == AnimalsType.EMPTY:
                    data["type"] = "FantomAnimal"
                elif animal.getType() == AnimalsType.PLANKTON:
                    data["type"] = "Plankton"
                elif animal.getType() == AnimalsType.SHARK:
                    data["type"] = "Shark"
                elif animal.getType() == AnimalsType.DOLPHIN:
                    data["type"] = "Dolphin"
                elif animal.getType() == AnimalsType.KILLERWHALE:
                    data["type"] = "Killerwhale"
                data["x"] = str(animal.getX())
                data["y"] = str(animal.getY())
                if animal.getType() == AnimalsType.EMPTY:
                    data["hp"] = "none"
                else:
                    data["hp"] = animal.getHp()
                if animal.getType() == AnimalsType.EMPTY or animal.getType() == AnimalsType.PLANKTON:
                    data["male"] = "none"
                else:
                    data["male"] = str(animal.getSex())
                if animal.getType() == AnimalsType.EMPTY:
                    data["age"] = "none"
                else:
                    data["age"] = str(animal.getAge())
                write.create_animals(data)
        write.create_xml_file()

    @classmethod
    def loadFromFile(cls, file_name) -> [[]]:
        fin = open("Model/size.txt", 'r')
        try:
            size: int = int(fin.readline())
            fin.close()
            ocean = np.empty((size, size), dtype="object")
            reader = XmlReader()
            reader.parser.setContentHandler(reader)
            reader.parser.parse(f"XML/{file_name}")
            try:
                print(f"XML/{file_name}")
                reader.parser.parse(f"XML/{file_name}")
            except ValueError:
                print("File not found")
                return None
            data = reader.table_data
            #print(data)
            df = pd.DataFrame(
                data=data,
                columns=[
                    'type', 'x', 'y', 'hp', 'male', 'age'
                ],
            )
            for ind, row in df.iterrows():
                type = row.type
                if type == 'Plankton':
                    ocean[int(row.x)][int(row.y)] = Plankton(int(row.x), int(row.y),
                                                             int(row.hp),
                                                             int(row.age))
                if type == 'FantomAnimal':
                    ocean[int(row.x)][int(row.y)] = FantomAnimal(int(row.x), int(row.y))

                if type == 'Shark':
                    sex = row.male
                    ocean[int(row.x)][int(row.y)] = Shark(int(row.x), int(row.y),
                                                          int(row.hp), sex,
                                                          int(row.age))
                if type == 'Dolphin':
                    sex = row.male
                    ocean[int(row.x)][int(row.y)] = Dolphin(int(row.x), int(row.y),
                                                            int(row.hp), sex,
                                                            int(row.age))
                if type == 'Killerwhale':
                    sex = row.male
                    ocean[int(row.x)][int(row.y)] = Killerwhale(int(row.x), int(row.y),
                                                                int(row.hp), sex,
                                                                int(row.age))
            return ocean

        except ValueError:
            print("Invalid file")
            exit(0)
