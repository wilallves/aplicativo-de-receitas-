from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class MinhaApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', spacing=10, padding=[20, 10], size_hint=(None, None), size=(100, 50))
        # Tamanho do BoxLayout definido como (200, 100)
        
        botao1 = Button(text='Login', size_hint=(None, None), size=(100, 50))
        # Tamanho do botão definido como (100, 50)
        
        botao2 = Button(text='Cadastro', size_hint=(None, None), size=(100, 50))
        # Tamanho do botão definido como (100, 50)
        
        layout.add_widget(botao1)
        layout.add_widget(botao2)
        
        return layout

if __name__ == '__main__':
    MinhaApp().run()
