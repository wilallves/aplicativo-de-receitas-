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


class Home(BoxLayout):
    def __init__(self, **kwargs):
        super(Home, self).__init__(**kwargs)
        # Defina a cor de fundo desejada
        Window.clearcolor = get_color_from_hex("#ff8e31")
        self.orientation = "vertical"
        self.padding = [100, 100]
        self.spacing = 10

        # Adicione a imagem (certifique-se de que o arquivo esteja no mesmo diretório)
        self.add_widget(Image(source='IMG_9831-removebg-preview.png', size=(200, 200)))
        self.add_widget(Label(text="ChefeVirtual", font_size=50, font_name='Impact', color=get_color_from_hex('#d5fff4')))
        self.add_widget(Label(text="Seja Bem-Vinda", font_size=20, font_name='Arial', color=get_color_from_hex('#d5fff4')))

        # Botões
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


class TelaLogin(BoxLayout):
    def __init__(self, **kwargs):
        super(TelaLogin, self).__init__(**kwargs)
        self.orientation = "vertical"
        self.padding = [100, 100]
        self.spacing = 10
        Window.clearcolor = get_color_from_hex("#ff8e31")

        # Imagem (certifique-se de que o arquivo esteja no mesmo diretório)
        self.add_widget(Label(text="ChefeVirtual", font_size=50, font_name='Impact', color=get_color_from_hex('#d5fff4')))
        self.add_widget(Label(text="Faça seu Login", font_size=20, font_name='Arial', color=get_color_from_hex('#d5fff4')))

        # Campos de entrada
        self.add_widget(Label(text="Nome de usuário:", font_name='Arial', color=get_color_from_hex('#5e2129'), font_size=20))
        self.username_input = TextInput(hint_text="Nome de usuário ...")
        self.add_widget(self.username_input)

        self.add_widget(Label(text="Senha:", font_name='Arial', color=get_color_from_hex('#5e2129'), font_size=20))
        self.senha_input = TextInput(hint_text="Digite sua senha ...", password=True)
        self.add_widget(self.senha_input)

        # Botão de Entrar
        self.cadastrar_button = Button(text="Entrar", background_color=get_color_from_hex('#5e2129'))
        self.cadastrar_button.bind(on_press=self.tela_pratos)
        self.add_widget(self.cadastrar_button)

    def tela_pratos(self, *args):
        self.parent.parent.current = 'Pratos'

class TelaCadastro(BoxLayout):
    def __init__(self, **kwargs):
        super(TelaCadastro, self).__init__(**kwargs)
        # Remova a linha abaixo se quiser manter o fundo branco
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
class TelaPratos(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.clearcolor = get_color_from_hex("#ff8e31")
        self.cols = 2
        self.size_hint = (1, 1)
        self.title_label = Label(text="Menu", halign="right", valign="top", size_hint=(0.5, 0.5), height="40dp", color='#722f37', font_size="25sp", pos_hint={20, 20})
        self.add_widget(self.title_label)
        


        # Adicione as imagens e botões
        self.image_layout = GridLayout(cols=2)
        self.add_widget(self.image_layout)
        self.add_pratos_de_entrada_image_and_button()
        self.add_veganos_image_and_button()
        self.add_sobremesa_image_and_button()
        self.add_aperitivo_image_and_button()

        self.button = Button(text=" adicionar uma receita", size_hint=(0, 0.1), background_color=('#9E0A0A'), color=(1, 1, 1, 1), pos_hint={'x': 0.25, 'y': 1})
        self.button.bind(on_release=self.on_button_release)
        self.add_widget(self.button)
        
    def add_pratos_de_entrada_image_and_button(self):
        self.image1 = Image(source=r'C:\Users\aluno.sesipaulista\Desktop\aplicativo-de-receitas-\imagens e icones\1.jpeg', size_hint=(1, None), height='200dp')
        self.button1 = Button(text='entrada', size_hint=(0.5, None), halign="center", valign="center", height='30dp', background_color=('#9E0A0A'), color=(1, 1, 1, 1), pos_hint={'x': 0.25, 'top': 1})
        self.button1.bind(on_release=self.on_button_release)
        self.layout1 = BoxLayout(orientation='vertical')
        self.layout1.add_widget(self.image1)
        self.layout1.add_widget(self.button1)
        self.add_widget(self.layout1)
        self.layout1.pos_hint = {'top': 1}

    def add_veganos_image_and_button(self):
        self.image2 = Image(source=r'C:\Users\aluno.sesipaulista\Desktop\aplicativo-de-receitas-\imagens e icones\2.jpeg', size_hint=(1, None), height='200dp')
        self.button2 = Button(text='veganos', size_hint=(0.5, None), height='30dp', background_color=('#9E0A0A'), color=(1, 1, 1, 1), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        self.layout2 = BoxLayout(orientation='vertical')
        self.button2.bind(on_release=self.on_button_release)
        self.layout2.add_widget(self.image2)
        self.layout2.add_widget(self.button2)
        self.add_widget(self.layout2)
        
    def add_sobremesa_image_and_button(self):
        self.image3 = Image(source=r'C:\Users\aluno.sesipaulista\Desktop\aplicativo-de-receitas-\imagens e icones\3.jpeg', size_hint=(1, None), height='200dp')
        self.button3= Button(text='sobremesas', size_hint=(0.5, None), height='30dp', background_color=('#9E0A0A'), pos_hint={'x': 0.25, 'self_y': 0.5})
        self.layout3 = BoxLayout(orientation='vertical')
        self.button3.bind(on_release=self.on_button_release)
        self.layout3.add_widget(self.image3)
        self.layout3.add_widget(self.button3)
        self.add_widget(self.layout3)

        
    def add_aperitivo_image_and_button(self):
        self.image4 = Image(source=r'C:\Users\aluno.sesipaulista\Desktop\aplicativo-de-receitas-\imagens e icones\4.jpeg', size_hint=(1, None), height='200dp')
        self.button4 = Button(text='aperitivos', size_hint=(0.5, None), height='30dp', background_color=('#9E0A0A'), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        self.button4.bind(on_release=self.on_button_release)
        self.layout4 = BoxLayout(orientation='vertical')
        self.layout4.add_widget(self.image4)
        self.layout4.add_widget(self.button4)
        self.add_widget(self.layout4)


    def on_button_release(self, instance):
        print('Botão liberado')


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
