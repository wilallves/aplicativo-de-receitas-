from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

    botao1 = Button(text='Login', size_hint=(None, None), size=(100, 50))
    # Tamanho do botão definido como (100, 50)
    
    botao2 = Button(text='Cadastro', size_hint=(None, None), size=(100, 50))
    # Tamanho do botão definido como (100, 50)
    
    layout.add_widget(botao1)
    layout.add_widget(botao2)
    
    return layout

    self.add_widget(Label(text='Cidade'))
    self.cidade = TextInput(multiline=False)
    self.add_widget(self.cidade)

    self.add_widget(Label(text='Data de Nascimento'))
    self.data_nascimento = TextInput(multiline=False)
    self.add_widget(self.data_nascimento)

    self.add_widget(Label(text='Telefone'))
    self.telefone = TextInput(multiline=False)
    self.add_widget(self.telefone)

    self.add_widget(Label(text='User Name'))
    self.username = TextInput(multiline=False)
    self.add_widget(self.username)

    self.add_widget(Label(text='Password'))
    self.password = TextInput(password=True, multiline=False)
    self.add_widget(self.password)

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class LoginScreen(GridLayout):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text='User Name'))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)
        self.add_widget(Label(text='Password'))
        self.password = TextInput(password=True, multiline=False)
        self.add_widget(self.password)


class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', spacing=10, padding=[20, 10], size_hint=(None, None), size=(100, 50))
        botao1 = Button(text='Login', size_hint=(None, None), size=(100, 50))
        botao2 = Button(text='Cadastro', size_hint=(None, None), size=(100, 50))
        layout.add_widget(botao1)
        layout.add_widget(botao2)
        return LoginScreen()


if __name__ == '__main__':
    MyApp().run()

    