from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.uix.image import Image ,AsyncImage
from functools import partial
from kivy.uix.modalview import ModalView
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window

Window.size = 360,640

#Julia e Mariana
class Home(BoxLayout):
    def __init__(self, **kwargs):
        super(Home, self).__init__(**kwargs)
        
        Window.clearcolor = get_color_from_hex("#ff8e31")
        self.orientation = "vertical"
        self.padding = [100, 100]
        self.spacing = 10

        
        self.add_widget(Image(source='IMG_9831-removebg-preview.png', size_hint=(None,None),size=(250,250)))
        self.add_widget(Label(text="ChefeVirtual", font_size=50, font_name='Impact', color=get_color_from_hex('#d5fff4')))
        self.add_widget(Label(text="Seja Bem-Vinda", font_size=20, font_name='Arial', color=get_color_from_hex('#d5fff4')))

        
        self.cadastrar_button = Button(text="Entrar", background_color=get_color_from_hex('#1eb88f'))
        self.cadastrar_button.bind(on_press=self.entrar)
        self.login_button = Button(text="Não possui uma conta? Cadastre-se", background_color=get_color_from_hex('#1eb88f'))
        self.login_button.bind(on_press=self.cadastrar)
        self.add_widget(self.cadastrar_button)
        self.add_widget(self.login_button)
        
    def entrar(self, *args):
        self.parent.parent.current = 'Login'
    
    def cadastrar(self, *args):
        self.parent.parent.current = 'Cadastro'

#Julia e Mariana
class TelaLogin(BoxLayout):
    def __init__(self, **kwargs):
        super(TelaLogin, self).__init__(**kwargs)
        self.orientation = "vertical"
        self.padding = [100, 100]
        self.spacing = 10
        Window.clearcolor = get_color_from_hex("#ff8e31")

       
        self.add_widget(Label(text="ChefeVirtual", font_size=50, font_name='Impact', color=get_color_from_hex('#d5fff4')))
        self.add_widget(Label(text="Faça seu Login", font_size=20, font_name='Arial', color=get_color_from_hex('#d5fff4')))

        
        self.add_widget(Label(text="Nome de usuário:", font_name='Arial', color=get_color_from_hex('#5e2129'), font_size=20))
        self.username_input = TextInput(hint_text="Nome de usuário ...")
        self.add_widget(self.username_input)

        self.add_widget(Label(text="Senha:", font_name='Arial', color=get_color_from_hex('#5e2129'), font_size=20))
        self.senha_input = TextInput(hint_text="Digite sua senha ...", password=True)
        self.add_widget(self.senha_input)

       
        self.cadastrar_button = Button(text="Entrar", background_color=get_color_from_hex('#5e2129'))
        self.cadastrar_button.bind(on_press=self.tela_pratos)
        self.add_widget(self.cadastrar_button)

    def tela_pratos(self, *args):
        self.parent.parent.current = 'Pratos'
#Mari e Julia
class TelaCadastro(BoxLayout):
    def __init__(self, **kwargs):
        super(TelaCadastro, self).__init__(**kwargs)
  
        Window.clearcolor = (1, 1, 1, 1)
        self.orientation = 'vertical'
        self.padding = [120, 120]
        self.spacing = 10

        self.add_widget(Label(text='Tela Cadastro', font_size=40, font_name='Georgia', color=get_color_from_hex('#e6e5ee')))

        self.username_input = TextInput(hint_text="Nome de usuário ...")
        self.email_input = TextInput(hint_text="Digite seu email ...")
        self.celular_input = TextInput(hint_text="Digite o número do seu celular ...")
        self.senha_input = TextInput(hint_text="Digite sua senha ...", password=True)

        self.add_widget(Label(text="Nome de usuário:", font_name='Arial', color=get_color_from_hex('#e6e5ee'), font_size=20))
        self.add_widget(self.username_input)
        self.add_widget(Label(text="Email:", font_name='Arial', color=get_color_from_hex('#e6e5ee'), font_size=20))
        self.add_widget(self.email_input)
        self.add_widget(Label(text="Celular:", font_name='Arial', color=get_color_from_hex('#e6e5ee'), font_size=20))
        self.add_widget(self.celular_input)
        self.add_widget(Label(text="Senha:", font_name='Arial', color=get_color_from_hex('#e6e5ee'), font_size=20))
        self.add_widget(self.senha_input)

        self.button_cadastrar = Button(text='Cadastrar', background_color=(0, 0, 1))
        self.button_cadastrar.bind(on_press=self.tela_pratos)
        self.add_widget(self.button_cadastrar)

    def tela_pratos(self, *args):
        self.parent.parent.current = 'Pratos'

from kivy.uix.gridlayout import GridLayout

#Victor Makson
class TelaPratos(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.clearcolor = get_color_from_hex("#ff8e31")
        self.cols = 2

        
        entrada_layout = GridLayout(cols=1, size_hint_y=None, height='230dp')
        self.image1 = Image(source='1.jpeg', size_hint_y=None, height='200dp')
        self.button1 = Button(text='entrada', size_hint_y=None, height='30dp', background_color=(0.619, 0.039, 0.039, 1))
        self.button1.bind(on_release=self.on_button_release)
        entrada_layout.add_widget(self.image1)
        entrada_layout.add_widget(self.button1)

        
        veganos_layout = GridLayout(cols=1, size_hint_y=None, height='230dp')
        self.image2 = Image(source='2.jpeg', size_hint_y=None, height='200dp')
        self.button2 = Button(text='veganos', size_hint_y=None, height='30dp', background_color=(0.619, 0.039, 0.039, 1))
        self.button2.bind(on_release=self.on_button_release)
        veganos_layout.add_widget(self.image2)
        veganos_layout.add_widget(self.button2)

        
        self.add_widget(entrada_layout)
        self.add_widget(veganos_layout)

        
        sobremesas_layout = GridLayout(cols=1, size_hint_y=None, height='230dp')
        self.image3 = Image(source='3.jpeg', size_hint_y=None, height='200dp')
        self.button3 = Button(text='sobremesas', size_hint_y=None, height='30dp', background_color=(0.619, 0.039, 0.039, 1))
        self.button3.bind(on_release=self.on_button_release)
        sobremesas_layout.add_widget(self.image3)
        sobremesas_layout.add_widget(self.button3)
        self.add_widget(sobremesas_layout)

        
        aperitivos_layout = GridLayout(cols=1, size_hint_y=None, height='230dp')
        self.image4 = Image(source='4.jpeg', size_hint_y=None, height='200dp')
        self.button4 = Button(text='aperitivos', size_hint_y=None, height='30dp', background_color=(0.619, 0.039, 0.039, 1))
        self.button4.bind(on_release=self.on_button_release)
        aperitivos_layout.add_widget(self.image4)
        aperitivos_layout.add_widget(self.button4)
        self.add_widget(aperitivos_layout)

    def on_button_release(self, instance):
        print("Button released")




class MyApp(App):
    def build(self):
         sm = ScreenManager()
         tela_login = TelaLogin()
         tela_cadastro = TelaCadastro()
         tela_home = Home()
         tela_pratos = TelaPratos()

         screen_login = Screen(name='Login')
         screen_cadastro = Screen(name='Cadastro')
         screen_home = Screen(name='Home')
         screen_pratos = Screen(name='Pratos')

         screen_login.add_widget(tela_login)
         screen_cadastro.add_widget(tela_cadastro)
         screen_home.add_widget(tela_home)
         screen_pratos.add_widget(tela_pratos)

         sm.add_widget(screen_home)
         sm.add_widget(screen_login)
         sm.add_widget(screen_cadastro)
         sm.add_widget(screen_pratos)
         

         return sm

if __name__ == '__main__':
     MyApp().run()
   
