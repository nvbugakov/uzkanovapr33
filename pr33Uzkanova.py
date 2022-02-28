from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.codeinput import CodeInput
from pygments.lexers import HtmlLexer
from kivy.uix.scatter import Scatter

from kivy.uix.floatlayout import FloatLayout

class myApp(App):
    def build(self):
        fl=FloatLayout(size=(200, 200))
        fl.add_widget(Button(
            text="Экономика",
            font_size=20,
            on_press=self.btn_press,
            background_color=[0,3,1,1],
            background_normal='',
            size_hint=(.5, .25),
            pos=(10, 20)))
        fl.add_widget(Button(
            text="Янажата",
            font_size=20,
            on_press=self.btn_press1,
            background_color=[1,3,0,1],
            background_normal='',
            size_hint=(.5, .25),
            pos=(100, 50)))
        return fl
    def btn_press(self, instance,value):        
        instance.text='Экономика'
    
       
    def btn_press1(self, instance):
        instance.text='Янажата'

if __name__=="__main__":
    myApp().run()
