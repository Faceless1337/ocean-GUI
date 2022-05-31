from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.snackbar import Snackbar

from Model.oceanController import OceanController
from Model.oceanController import FileReader
from Model.animals import FantomAnimal
from Model.animals import Plankton
from Model.animals import Killerwhale
from Model.animals import Shark
from Model.animals import Dolphin
from Model.living import AnimalsType
from Model.living import Animals
import random

n = 11
setattr(Animals, 'n', 11)


class OceanStorage:
    def __init__(self, ocean):
        self.ocean = ocean


class ScreenModel:
    _not_filtered = []

    def __init__(self):
        self.dialog = None
        self.oceanStorage = OceanStorage(None)
        self.oceanController = OceanController(n)
        self._observers = []
        oceanTable = []
        for row_index in range(1, n - 1):
            line = []
            for column_index in range(1, n - 1):
                line.append(MDRectangleFlatButton(
                    text="\n",
                    pos_hint={'center_x': .125 + .09 * column_index, 'center_y': .9 - .07 * row_index},
                    size_hint=(0.025, 0.025),
                    font_size=20,
                    md_bg_color=(0, 1, 1, 0)
                ))
            oceanTable.append(line)
        self.oceanTable = oceanTable

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self, data):
        for x in self._observers:
            x.model_is_changed(data)

    def read_from_file(self, file_name: str) -> None:
        ocean_ = FileReader.loadFromFile(file_name=file_name)
        print(ocean_)
        self.oceanStorage.ocean = ocean_ if ocean_ is not None else self.oceanStorage.ocean
        self.updateOcean()

    @staticmethod
    def create_empty_file(path):
        try:
            with open(path, 'w'):
                pass
            return True
        except Exception as e:
            return False

    def write_to_file(self, path: str):
        path = "XML/" + path
        FileReader.saveToFile(self.oceanStorage.ocean, path)
        Snackbar(text="Ocean was saved").open()

    def add_new_animal(self, data):
        animal_type, x, y = data
        if animal_type not in ["Plankton", "Dolphin", "Shark", "Killerwhale"]:
            Snackbar(text="Invalid animal type").open()
            return
        x = int(x)
        y = int(y)
        if (x < 1 or x > n - 2) or (y < 1 or y > n - 2):
            Snackbar(text="Invalid row or column number").open()
            return
        if animal_type == "Plankton":
            self.oceanStorage.ocean[x][y] = Plankton(x, y, 2, 0)
        elif animal_type == "Shark":
            self.oceanStorage.ocean[x][y] = Shark(x, y, 5, random.choice([True, False]), 0)
        elif animal_type == "Dolphin":
            self.oceanStorage.ocean[x][y] = Dolphin(x, y, 4, random.choice([True, False]), 0)
        elif animal_type == "Killerwhale":
            self.oceanStorage.ocean[x][y] = Killerwhale(x, y, 6, random.choice([True, False]), 0)
        self.updateOcean()

    def updateOcean(self):
        for raw_index in range(1, n - 1):
            for column_index in range(1, n - 1):
                if self.oceanStorage.ocean[raw_index][column_index].getType() == AnimalsType.EMPTY:
                    text = "E"
                if self.oceanStorage.ocean[raw_index][column_index].getType() == AnimalsType.PLANKTON:
                    text = "P"
                if self.oceanStorage.ocean[raw_index][column_index].getType() == AnimalsType.SHARK:
                    text = "S"
                if self.oceanStorage.ocean[raw_index][column_index].getType() == AnimalsType.KILLERWHALE:
                    text = "K"
                if self.oceanStorage.ocean[raw_index][column_index].getType() == AnimalsType.DOLPHIN:
                    text = "D"
                self.oceanTable[raw_index - 1][column_index - 1].text = text

    def delete_animal(self, x, y):
        if (x < 1 or x > n - 2) or (y < 1 or y > n - 2):
            Snackbar(text="Invalid row or column number").open()
            return
        self.oceanStorage.ocean[x][y] = FantomAnimal(x, y)
        self.updateOcean()
        return True

    def next_step(self):
        self.oceanController.update(self.oceanStorage.ocean)
        self.updateOcean()
