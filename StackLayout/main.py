from kivy.app import App
from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button


class StackLayoutExample(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        size = '120dp'
        # self.orientation = "lr-bt"
        # self.padding = '60dp', '60dp'
        # self.spacing = '60dp', '60dp'
        for i in range(100):
            b = Button(text=str(i+1),size_hint=(None,None),size=(size,size))
            self.add_widget(b)

class MyApp(App):
    def build(self):
        self.title = "StackLayout"
        
        
    
    
MyApp().run()