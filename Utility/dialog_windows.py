import os

from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.dropdown import DropDown
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivy.uix.button import Button
from kivymd.uix.menu import MDDropdownMenu


class DialogContent(BoxLayout):
    pass


class InputDialogContent(DialogContent):
    pass


class DeleteDialogContent(DialogContent):
    pass


class UploadDialogContent(DialogContent):
    pass


class SaveDialogContent(DialogContent):
    pass


class DialogWindow(MDDialog):
    def __init__(self, **kwargs):
        super().__init__(
            title=kwargs["title"],
            type="custom",
            content_cls=kwargs["content_cls"],
            buttons=[
                MDFlatButton(
                    text="OK",
                    theme_text_color="Custom",
                    on_release=self.close
                ),
            ],
        )
        self.mode = kwargs["mode"]
        self.controller = kwargs["controller"]
        self.model = kwargs["model"]

    def close(self, obj):
        self.dismiss()


class InputWindow(DialogWindow):
    def __init__(self, **kwargs):
        super().__init__(
            title="New animal: ",
            content_cls=InputDialogContent(),
            mode="input",
            controller=kwargs["controller"],
            model=kwargs["model"]
        )
        '''drop_down = DropDown()
        btn = Button(text="Plankton", size_hint_y=None, height=20)
        btn.bind(on_release=lambda btn: drop_down.select(btn.text))
        btn1 = Button(text="Dolphin", size_hint_y=None, height=20)
        btn1.bind(on_release=lambda btn1: drop_down.select(btn1.text))
        btn2 = Button(text="Shark", size_hint_y=None, height=20)
        btn2.bind(on_release=lambda btn2: drop_down.select(btn2.text))
        btn3 = Button(text="Killerwhale", size_hint_y=None, height=20)
        btn3.bind(on_release=lambda btn3: drop_down.select(btn3.text))


        drop_down.add_widget(btn)
        drop_down.add_widget(btn1)
        drop_down.add_widget(btn2)
        drop_down.add_widget(btn3)

        main_but = Button(text="Choose animal", size_hint=(.3, .3))
        main_but.pos_hint = ()
        main_but.bind(on_release=drop_down.open)
        drop_down.bind(on_select=lambda instance, x: setattr(self.content_cls.ids['type'], 'text', x))
        self.add_widget(main_but)'''

    def close(self, obj):
        self.dismiss()
        self.controller.close_dialog(
            [
                self.content_cls.ids.type.text,
                self.content_cls.ids.input_row_index.text,
                self.content_cls.ids.input_column_index.text
            ]
        )


class DeleteWindow(DialogWindow):
    def __init__(self, **kwargs):
        super().__init__(
            title="Delete animal: ",
            content_cls=DeleteDialogContent(),
            mode="delete",
            controller=kwargs["controller"],
            model=kwargs["model"]
        )

    def close(self, obj):
        self.dismiss()
        self.controller.close_dialog(
            [
                self.content_cls.ids.delete_animal_x.text,
                self.content_cls.ids.delete_animal_y.text
            ]
        )


class SaveWindow(DialogWindow):
    def __init__(self, **kwargs):
        super().__init__(
            title="Saving: ",
            content_cls=SaveDialogContent(),
            mode="save",
            controller=kwargs["controller"],
            model=kwargs["model"]
        )

    def close(self, obj):
        self.dismiss()
        self.controller.close_dialog(self.content_cls.ids.save_path.text)


class UploadWindow(DialogWindow):
    def __init__(self, **kwargs):
        super().__init__(
            title="Upload: ",
            content_cls=UploadDialogContent(),
            mode="upload",
            controller=kwargs["controller"],
            model=kwargs["model"]
        )

    def close(self, obj):
        self.dismiss()
        self.controller.close_dialog(self.content_cls.ids.upload_path.text)


Builder.load_file(os.path.join(os.path.dirname(__file__), "dialog_windows.kv"))
