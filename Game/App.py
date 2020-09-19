from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import StringProperty


class Window(FloatLayout):
    button_text = StringProperty('Start')  # Text for the start/stop simulation button

    def __init__(self, **kwargs):
        super(Window, self).__init__(**kwargs)


class LifeApp(App):
    def build(self):
        return Window()


if __name__ == '__main__':
    LifeApp().run()
