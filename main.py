from collections import deque

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class QueueCanvas(BoxLayout):
    customers = 0
    customersName = deque([])

    def label_update(self):
        self.ids['Customer'].text = str(self.customers) + ' står i køen'

    def customer_register(self):
        self.customersName.append(self.ids['name_register'].text)
        self.ids['name_register'].text = ' '

class QueueApp(App):
    def build(self):
        return QueueCanvas()


if __name__ == '__main__':
    QueueApp().run()
