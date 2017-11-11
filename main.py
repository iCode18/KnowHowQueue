from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class QueueCanvas(BoxLayout):
    pass


class QueueApp(App):
    def build(self):
        return QueueCanvas()


if __name__ == '__main__':
    QueueApp().run()
