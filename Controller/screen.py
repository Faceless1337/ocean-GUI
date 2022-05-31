from kivymd.uix.snackbar import Snackbar
from Model.oceanController import FileReader
from Model.screen import ScreenModel


class ScreenController:
    _observers = []

    def __init__(self, model: ScreenModel):
        self.model = model
        self.model.oceanStorage.ocean = FileReader.loadFromFile("default.xml")
        self.model.updateOcean()
        self._observers = []
        self._dialog = None

    def add_animal(self, data):
        self.model.add_new_animal(data=data)

    def dialog(self, mode, dialog):
        self.open_dialog(mode, dialog)

    def next_step(self):
        self.model.next_step()

    def delete_animal(self, data):
        delete = self.model.delete_animal(int(data[0]), int(data[1]))
        if delete:
            Snackbar(text=f"Animal was deleted!").open()

    def upload_from_file(self, file_name):
        self.model.read_from_file(file_name)

    def save_in_file(self, file_name):
        self.model.write_to_file(file_name)

    def open_dialog(self, dialog, mode):
        self._dialog = dialog

    def close_dialog(self, dialog_data: list = []):
        data = dialog_data
        self.model.notify_observers(data)
        self._dialog = None
