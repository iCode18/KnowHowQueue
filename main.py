from collections import deque

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

customerList = deque([])


class QueueCanvas(BoxLayout):
    customers = 0

    def label_update(self):
        self.ids['Customer'].text = str(len(customerList)) + ' står i køen'

    def customer_register(self):
        customerList.append(self.ids['name_register'].text);
        self.ids['name_register'].text = 'Registrer ditt navn i køen'

    def text_input_update(self):
        if self.ids['name_register'].text == 'Registrer ditt navn i køen':
            self.ids['name_register'].text = ' '


class QueueApp(App):
    def build(self):
        return QueueCanvas()


if __name__ == '__main__':
    QueueApp().run()
