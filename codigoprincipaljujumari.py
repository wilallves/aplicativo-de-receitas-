
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout

Window.size = 360, 640

# Julia e Mariana
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
        self.login_button = Button(text=" Cadastre-se", background_color=get_color_from_hex('#1eb88f'))
        self.login_button.bind(on_press=self.cadastrar)
        self.add_widget(self.cadastrar_button)
        self.add_widget(self.login_button)
        
    def entrar(self, *args):
        self.parent.parent.current = 'Login'
    
    def cadastrar(self, *args):
        self.parent.parent.current = 'Cadastro'

# Julia e Mariana
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

# Mari e Julia
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

# Victor Makson
class TelaPratos(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.clearcolor = get_color_from_hex("#ff831")
        self.cols = 2
        self.size_hint = (1, 1)
        self.entradas()
        self.veganos()
        self.sobremesas()
        self.aperitivos()

    def entradas(self):
        imagem_entradas = Image(source=r'C:\Users\aluno.sesipaulista\Desktop\aplicativo-de-receitas-\imagens e icones\1.jpeg', size_hint=(1, None), height='200dp')
        botão_entradas = Button(text='entrada', size_hint=(0.5, None), halign="center", valign="center", height='30dp', background_color=('#9E0A0A'), color=(1, 1, 1, 1), pos_hint={'x': 0.25, 'top': 1})
        botão_entradas.bind(on_press=self.va_para_entradas)
        entradas = GridLayout(cols=1, size_hint_y=None, height='230dp')
        entradas.add_widget(imagem_entradas)
        entradas.add_widget(botão_entradas)
        self.add_widget(entradas)
        
    def va_para_entradas(self, instance):
        self.parent.parent.current = 'Entradas'

    def veganos(self):
        imagem_veganos = Image(source=r'C:\Users\aluno.sesipaulista\Desktop\aplicativo-de-receitas-\imagens e icones\2.jpeg', size_hint=(1, None), height='200dp')
        botão_veganos = Button(text='veganos', size_hint=(0.5, None), height='30dp', background_color=('#9E0A0A'), color=(1, 1, 1, 1), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        botão_veganos.bind(on_press=self.on_button_press)
        veganos = GridLayout(cols=1, size_hint_y=None, height='230dp')
        veganos.add_widget(imagem_veganos)
        veganos.add_widget(botão_veganos)
        self.add_widget(veganos)
        
    def sobremesas(self):
        imagem_sobremesas = Image(source=r'C:\Users\aluno.sesipaulista\Desktop\aplicativo-de-receitas-\imagens e icones\3.jpeg', size_hint=(1, None), height='200dp')
        botão_sobremesas= Button(text='sobremesas', size_hint=(0.5, None), height='30dp', background_color=('#9E0A0A'), pos_hint={'x': 0.25, 'center_y': 0.5})
        botão_sobremesas.bind(on_press=self.on_button_press)
        sobremesas = GridLayout(cols=1, size_hint_y=None, height='230dp')
        sobremesas.add_widget(imagem_sobremesas)
        sobremesas.add_widget(botão_sobremesas)
        self.add_widget(sobremesas)
        
    def aperitivos(self):
        imagem_aperitivos = Image(source=r'C:\Users\aluno.sesipaulista\Desktop\aplicativo-de-receitas-\imagens e icones\4.jpeg', size_hint=(1, None), height='200dp')
        botão_aperitivos = Button(text='aperitivos', size_hint=(0.5, None), height='30dp', background_color=('#9E0A0A'), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        botão_aperitivos.bind(on_press=self.on_button_press)
        aperitivos = GridLayout(cols=1, size_hint_y=None, height='230dp')
        aperitivos.add_widget(imagem_aperitivos)
        aperitivos.add_widget(botão_aperitivos)
        self.add_widget(aperitivos)

    def on_button_press(self, instance):
        self.parent.parent.current = 'Entradas'

# Tela de Entradas
class TelaEntradas(BoxLayout):  # Cambié el diseño para que se adapte mejor
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.clearcolor = (0.9, 0.5, 0, 0)
        self.orientation = 'vertical'
        self.padding = 10

        label_titulo = Label(
            text="Entradas", 
            size_hint=(1, 0.1),
            color=[1, 1, 1, 1],
            font_size=45
        )
        self.add_widget(label_titulo)

        foto_lasanha = Image(
            source='C:/Users/aluno.sesipaulista/Downloads/08_LASANHA_FINAL-1-min.webp',
            size_hint=(1, 0.4)
        )
        self.add_widget(foto_lasanha)

        botao_lasanha = Button(
            text='Confira já', 
            background_color=get_color_from_hex('#5e2129'),
            size_hint=(1, 0.1)
        )
        self.add_widget(botao_lasanha)

        foto_strogonoff = Image(
            source='C:/Users/aluno.sesipaulista/Downloads/download (2).jpg',
            size_hint=(1, 0.4)
        )
        self.add_widget(foto_strogonoff)

        botao_strogonoff = Button(
            text='Confira já',
            background_color=get_color_from_hex('#5e2129'), 
            size_hint=(1, 0.1)
        )
        self.add_widget(botao_strogonoff)

        foto_cuscuz = Image(
            source='C:/Users/aluno.sesipaulista/Downloads/images (3).jpg',
            size_hint=(1, 0.4)
        )
        self.add_widget(foto_cuscuz)

        botao_cuscuz = Button(
            text='Confira já',
            background_color=get_color_from_hex('#5e2129'), 
            size_hint=(1, 0.1)
        )
        self.add_widget(botao_cuscuz)

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
         screen_entradas = Screen(name='Entradas')
         
         screen_login.add_widget(tela_login)
         screen_cadastro.add_widget(tela_cadastro)
         screen_home.add_widget(tela_home)
         screen_pratos.add_widget(tela_pratos)
         screen_entradas.add_widget(TelaEntradas())  # Crear una instancia directamente aquí
         
         sm.add_widget(screen_home)
         sm.add_widget(screen_login)
         sm.add_widget(screen_cadastro)
         sm.add_widget(screen_pratos)
         sm.add_widget(screen_entradas)

         return sm

if __name__ == '__main__':
     MyApp().run()
