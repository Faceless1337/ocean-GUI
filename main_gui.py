# main file for GUI version

from kivymd.app import MDApp
from Model.screen import ScreenModel
from Controller.screen import ScreenController
from View.myscreen import ScreenView
from kivy.core.window import Window
from kivymd.uix.button import MDRectangleFlatButton


n = 11


class Pass_MVC(MDApp):
    def __init__(self):
        super().__init__()
        oceanTable = []
        #print(len(oceanTable))
        self.model = ScreenModel()
        self.controller = ScreenController(self.model)
        self.view = ScreenView(model=self.model, controller=self.controller)

    def build(self):
        Window.size = (1920, 1080)
        self.title = "Ocean"
        return self.view.build()


