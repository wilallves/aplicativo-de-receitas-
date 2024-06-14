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

class TelaCadastro(BoxLayout):
    def __init__(self, **kwargs):
        super(TelaCadastro, self).__init__(**kwargs)
  
        Window.clearcolor = get_color_from_hex("#ff8e31")
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

        self.button_cadastrar = Button(text='Cadastrar', background_color=get_color_from_hex('#5e2129'))
        self.button_cadastrar.bind(on_press=self.tela_pratos)
        self.add_widget(self.button_cadastrar)

    def tela_pratos(self, *args):
        self.parent.parent.current = 'Pratos'

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
        imagem_entradas = Image(source='2.jpeg', size_hint=(1, None), height='200dp')
        botao_entradas = Button(text='entrada', size_hint=(0.5, None), halign="center", valign="center", height='30dp', background_color=('#9E0A0A'), color=(1, 1, 1, 1), pos_hint={'x': 0.25, 'top': 1})
        botao_entradas.bind(on_press=self.va_para_entradas)
        entradas = GridLayout(cols=1, size_hint_y=None, height='230dp')
        entradas.add_widget(imagem_entradas)
        entradas.add_widget(botao_entradas)
        self.add_widget(entradas)
        
    def va_para_entradas(self, instance):
        self.parent.parent.current = 'Entradas'

    def veganos(self):
        imagem_veganos = Image(source='1.jpeg', size_hint=(1, None), height='200dp')
        botao_veganos = Button(text='veganos', size_hint=(0.5, None), height='30dp', background_color=('#9E0A0A'), color=(1, 1, 1, 1), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        botao_veganos.bind(on_press=self.on_veganos_press)
        veganos = GridLayout(cols=1, size_hint_y=None, height='230dp')
        veganos.add_widget(imagem_veganos)
        veganos.add_widget(botao_veganos)
        self.add_widget(veganos)

    def on_veganos_press(self, instance):
        self.parent.parent.current = 'Veganos'

    def sobremesas(self):
        imagem_sobremesas = Image(source='3.jpeg', size_hint=(1, None), height='200dp')
        botao_sobremesas= Button(text='sobremesas', size_hint=(0.5, None), height='30dp', background_color=('#9E0A0A'), pos_hint={'x': 0.25, 'center_y': 0.5})
        botao_sobremesas.bind(on_press=self.on_sobremesas_press)
        sobremesas = GridLayout(cols=1, size_hint_y=None, height='230dp')
        sobremesas.add_widget(imagem_sobremesas)
        sobremesas.add_widget(botao_sobremesas)
        self.add_widget(sobremesas)
        
    def on_sobremesas_press(self, instance):
        self.parent.parent.current = 'Sobremesas'
        
    def aperitivos(self):
        imagem_aperitivos = Image(source='4.jpeg', size_hint=(1, None), height='200dp')
        botao_aperitivos = Button(text='aperitivos', size_hint=(0.5, None), height='30dp', background_color=('#9E0A0A'), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        botao_aperitivos.bind(on_press=self.on_aperitivos_press)
        aperitivos = GridLayout(cols=1, size_hint_y=None, height='230dp')
        aperitivos.add_widget(imagem_aperitivos)
        aperitivos.add_widget(botao_aperitivos)
        self.add_widget(aperitivos)

    def on_aperitivos_press(self, instance):
        self.parent.parent.current = 'Aperitivos'

class TelaEntradas(BoxLayout): 
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.clearcolor = (0.9, 0.5, 0, 0)
        self.orientation = 'vertical'
        self.padding = 10
        self.lasanha()
        self.cuscuz()
        self.strog()
       

    def lasanha(self):
        label_titulo = Label(text="Entradas", size_hint=(1, 0.1),color=[1, 1, 1, 1],font_size=45)
        foto_lasanha = Image(source='lasanha.png',size_hint=(1, 0.4))
        botao_lasanha = Button(text='Confira já', on_press=self.on_lasanha_press,background_color=get_color_from_hex('#5e2129'),size_hint=(1, 0.1))
        lasanha = GridLayout(cols=1, size_hint_y=None, height='230dp')
        lasanha.add_widget(label_titulo)
        lasanha.add_widget(foto_lasanha)
        lasanha.add_widget(botao_lasanha)
        self.add_widget(lasanha)

    def on_lasanha_press(self, instance):
        self.parent.parent.current = 'Lasanha'

    def strog(self):
        foto_strogonoff = Image(source='strogonoff.png.jpg',size_hint=(1, 0.4))
        botao_strogonoff = Button(text='Confira já',background_color=get_color_from_hex('#5e2129'), size_hint=(1, 0.1))
        botao_voltar = Button (text='Voltar', halign='center',color=[1, 1, 1, 1],size_hint_y=None, height=50, size_hint_x=0.9,pos=(300, 50))
        botao_voltar.bind(on_press=self.voltar2)
        strog = GridLayout(cols=1, size_hint_y=None, height='230dp')
        strog.add_widget(foto_strogonoff)
        strog.add_widget(botao_strogonoff)
        strog.add_widget(botao_voltar)
        self.add_widget(strog)

    def on_strog_press(self,instance):
        self.parent.parent.current = "Strog"

    def cuscuz(self):
        foto_cuscuz = Image(source='OIP.jpeg',size_hint=(1, 0.4))
        botao_cuscuz = Button(text='Confira já',background_color=get_color_from_hex('#5e2129'), size_hint=(1, 0.1))
        cuscuz = GridLayout(cols=1, size_hint_y=None, height='175dp')
        cuscuz.add_widget(foto_cuscuz)
        cuscuz.add_widget(botao_cuscuz)
        self.add_widget(cuscuz)

    def voltar2(self, instance):
        self.parent.parent.current= 'Pratos'
     
class TelaLasanha(BoxLayout):
     def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.clearcolor = (0.9, 0.5, 0, 0)
        return self.principal()

     def principal(self):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        ingredients = [
            '1- Massa de lasanha',
            '2- Molho de tomate',
            '3- Carne moída',
            '4- Cebola',
            '5- Alho',
            '6- Queijo mussarela',
            '7- Presunto',
            '8- Queijo parmesão',
            '9- Sal',
            '10- Pimenta',
            '11- Azeite'
        ]

        ingredient_label = Label(text='Ingredientes:\n' + '\n'.join(ingredients), size_hint_y=400, height=300, color=[1,1,1,1])

        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        top_layout = BoxLayout(orientation='horizontal', size_hint_y=100, height=500, size_hint_x=1.5)
        bottom_layout = BoxLayout(orientation='vertical', size_hint_y=None, height=400)


        foto_lasanha = Image(source='lasanha.png', size_hint= (2, 1))
        input_receita = TextInput (hint_text='Adicione um comentário', size_hint_y=50, height=50, size_hint_x=0.9,pos= (200, 50),multiline= True)
        
        botao_modo_preparo = Button (text='Modo de Preparo', halign= 'center',color= [1,1,1,1],size_hint_y=50, height=50, size_hint_x=0.9,pos= (300, 50))
        botao_modo_preparo.bind(on_press=self.modopreparo)
        botao_voltar = Button (text='Voltar', halign='center',color=[1, 1, 1, 1],size_hint_y=None, height=50, size_hint_x=0.9,pos=(300, 50))
        botao_voltar.bind(on_press=self.voltar2)

        bottom_layout.add_widget(ingredient_label)
        bottom_layout.add_widget(input_receita)
        bottom_layout.add_widget(botao_modo_preparo)
        bottom_layout.add_widget(botao_voltar)
        top_layout.add_widget(foto_lasanha)
        top_layout.add_widget(layout)
        main_layout.add_widget(top_layout)
        main_layout.add_widget(bottom_layout)

        self.add_widget(main_layout)

     def modopreparo(self, instance):
        self.clear_widgets()
        self.add_widget(self.Janela_Modo_Preparo())

     def voltar2(self, instance):
        self.parent.parent.current = 'Entradas'

     def Janela_Modo_Preparo(self):
        preparation = (
            "1. Cozinhe a massa conforme as instruções do pacote.\n"
            "2. Refogue a cebola e o alho no azeite.\n"
            "3. Adicione a carne moída e cozinhe até dourar.\n"
            "4. Adicione o molho de tomate e tempere com sal e pimenta.\n"
            "5. Em um refratário, alterne camadas de massa, molho, presunto e mussarela.\n"
            "6. Finalize com queijo parmesão ralado por cima.\n"
            "7. Asse em forno pré-aquecido a 180°C por 30 minutos."
        )

        preparation_label = Label(text='Modo de Preparo:\n' + preparation, size_hint_y=None, height=400, color=[1, 1, 1, 1])
        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        top_layout = BoxLayout(orientation='horizontal', size_hint_y=100, height=500, size_hint_x=1.5)
        bottom_layout = BoxLayout(orientation='vertical', size_hint_y=None,size_hint_x =1, height=400)

        foto_lasanha = Image(source='lasanha.png', size_hint=(2, 1))
        botao_voltar = Button (text='Voltar', halign='center',color=[1, 1, 1, 1],size_hint_y=None, height=50, size_hint_x=0.9,pos=(300, 50))
        botao_voltar.bind(on_press=self.voltar)

        bottom_layout.add_widget(preparation_label)
        bottom_layout.add_widget(botao_voltar)
        top_layout.add_widget(foto_lasanha)

        top_layout.add_widget(BoxLayout())

        main_layout.add_widget(top_layout)
        main_layout.add_widget(bottom_layout)

        return main_layout
     
     def voltar(self,instance):
        self.clear_widgets()
        self.principal()
     
class TelaStrogonoff(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.clearcolor = (0.9, 0.5, 0, 0)
        self.orientation = 'vertical'
        self.padding = 10
        self.principal()

    def principal(self):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        ingredients = [
            '1- 500g de peito de frango cortado em cubos',
            '2- 1 cebola picada',
            '3- 2 dentes de alho picados',
            '4- 1 colher de sopa de óleo vegetal',
            '5- 1 lata de creme de leite',
            '6- 1 lata de molho de tomate',
            '7- 1/2 xícara de ketchup',
            '8- Sal e pimenta a gosto',
            'Arroz branco para acompanhar',
        ]

        ingredient_label = Label(text='Ingredientes:\n' + '\n'.join(ingredients), size_hint_y=400, height=300, color=[1, 1, 1, 1])

        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        top_layout = BoxLayout(orientation='horizontal', size_hint_y=100, height=500, size_hint_x=1.5)
        bottom_layout = BoxLayout(orientation='vertical', size_hint_y=None, height=400)

        foto_strogonoff = Image(source='strogonoff.png.jpg', size_hint=(2, 1))
        input_receita = TextInput(
            hint_text='Adicione um comentário',
            size_hint_y=50, height=50, size_hint_x=0.9,
            pos=(200, 50),
            multiline=True
        )

        botao_modo_preparo = Button(
            text='Modo de Preparo',
            halign='center',
            color=[1, 1, 1, 1],
            size_hint_y=50, height=50, size_hint_x=0.9,
            pos=(300, 50),
            on_press=self.modopreparo
        )

        bottom_layout.add_widget(ingredient_label)
        bottom_layout.add_widget(input_receita)
        bottom_layout.add_widget(botao_modo_preparo)
        top_layout.add_widget(foto_strogonoff)
        top_layout.add_widget(layout)

        main_layout.add_widget(top_layout)
        main_layout.add_widget(bottom_layout)

        self.add_widget(main_layout)

    def modopreparo(self, instance):
        self.clear_widgets()
        self.add_widget(self.Janela_Modo_Preparo())

    def Janela_Modo_Preparo(self):
        preparation = (
            """
            Em uma panela grande, aqueça a manteiga e o óleo em fogo médio.
            Adicione a cebola e o alho picados, e refogue até que estejam dourados e perfumados.
            Acrescente o frango em cubos à panela, e tempere com sal e pimenta a gosto. Refogue até que o frango esteja dourado por todos os lados.
            Adicione o molho de tomate e o ketchup à panela, e mexa bem para incorporar os ingredientes.
            Reduza o fogo para médio-baixo e deixe o molho cozinhar por cerca de 10 minutos, mexendo ocasionalmente.
            Depois que o molho estiver bem incorporado e o frango estiver cozido, adicione o creme de leite à panela e mexa bem para misturar.
            Se estiver usando champignon em conserva, adicione-o à panela neste momento.
            Cozinhe por mais 2-3 minutos, apenas para aquecer o champignon e garantir que todos os ingredientes estejam bem aquecidos.
            Prove e ajuste o tempero, se necessário.
            Sirva o Strogonoff de frango quente acompanhado de arroz branco e batata palha, se desejar.
            Bom apetite!
            """
        )

        preparation_label = Label(text='Modo de Preparo:\n' + preparation, font_size=12, size_hint_y=None, height=400, color=[1, 1, 1, 1])
        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        top_layout = BoxLayout(orientation='horizontal', size_hint_y=100, height=500, size_hint_x=1.5)
        bottom_layout = BoxLayout(orientation='vertical', size_hint_y=None, size_hint_x=1, height=400)

        foto_strogonoff = Image(source='strogonoff.png.jpg', size_hint=(2, 1))
        botao_voltar = Button(
            text='Voltar',
            halign='center',
            color=[1, 1, 1, 1],
            size_hint_y=None, height=50, size_hint_x=0.9,
            pos=(300, 50)
        )
        botao_voltar.bind(on_press=self.voltar)

        bottom_layout.add_widget(preparation_label)
        bottom_layout.add_widget(botao_voltar)
        top_layout.add_widget(foto_strogonoff)

        main_layout.add_widget(top_layout)
        main_layout.add_widget(bottom_layout)

        return main_layout

    def voltar(self, instance):
        self.clear_widgets()

      
     
    
         
class TelaVeganos(BoxLayout): 
     def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.clearcolor = (0.9, 0.5, 0, 0)
        self.orientation = 'vertical'
        self.padding = 10

        label_titulo = Label(
            text="Veganos", 
            size_hint=(1, 0.1),
            color=[1, 1, 1, 1],
            font_size=45
        )
        self.add_widget(label_titulo)

        foto_macarrao = Image(
            source='macarrao.jpeg',
            size_hint=(1, 0.4)
        )
        self.add_widget(foto_macarrao)

        botao_macarrao = Button(
            text='Confira já', 
            background_color=get_color_from_hex('#5e2129'),
            size_hint=(1, 0.1)
        )
        self.add_widget(botao_macarrao)

        foto_tofu = Image(
            source='Captura de tela 2024-06-11 003701.png',
            size_hint=(1, 0.4)
        )
        self.add_widget(foto_tofu)

        botao_tofu = Button(
            text='Confira já',
            background_color=get_color_from_hex('#5e2129'), 
            size_hint=(1, 0.1)
        )
        self.add_widget(botao_tofu)

class TelaSobremesas(BoxLayout): 
     def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.clearcolor = (0.9, 0.5, 0, 0)
        self.orientation = 'vertical'
        self.padding = 10

        label_titulo = Label(
            text="Sobremesas", 
            size_hint=(1, 0.1),
            color=[1, 1, 1, 1],
            font_size=45
        )
        self.add_widget(label_titulo)

        foto_pudim = Image(
            source='C:/Users/aluno.sesipaulista/Downloads/08_LASANHA_FINAL-1-min.webp',
            size_hint=(1, 0.4)
        )
        self.add_widget(foto_pudim)

        botao_pudim = Button(
            text='Confira já', 
            background_color=get_color_from_hex('#5e2129'),
            size_hint=(1, 0.1)
        )
        self.add_widget(botao_pudim)

        foto_pave = Image(
            source='C:/Users/aluno.sesipaulista/Downloads/download (2).jpg',
            size_hint=(1, 0.4)
        )
        self.add_widget(foto_pave)

        botao_pave = Button(
            text='Confira já',
            background_color=get_color_from_hex('#5e2129'), 
            size_hint=(1, 0.1)
        )
        self.add_widget(botao_pave)

class TelaAperitivos(BoxLayout): 
     def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.clearcolor = (0.9, 0.5, 0, 0)
        self.orientation = 'vertical'
        self.padding = 10

        label_titulo = Label(
            text="Aperitivos", 
            size_hint=(1, 0.1),
            color=[1, 1, 1, 1],
            font_size=45
        )
        self.add_widget(label_titulo)

        foto_carne = Image(
            source='C:/Users/aluno.sesipaulista/Downloads/08_LASANHA_FINAL-1-min.webp',
            size_hint=(1, 0.4)
        )
        self.add_widget(foto_carne)

        botao_carne = Button(
            text='Confira já', 
            background_color=get_color_from_hex('#5e2129'),
            size_hint=(1, 0.1)
        )
        self.add_widget(botao_carne)

        foto_tabua = Image(
            source='C:/Users/aluno.sesipaulista/Downloads/download (2).jpg',
            size_hint=(1, 0.4)
        )
        self.add_widget(foto_tabua)

        botao_tabua = Button(
            text='Confira já',
            background_color=get_color_from_hex('#5e2129'), 
            size_hint=(1, 0.1)
        )
        self.add_widget(botao_tabua)

    

class Aplicativos_de_receitas(App):
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
         screen_veganos = Screen (name='Veganos')
         screen_sobremesas = Screen (name = 'Sobremesas')
         screen_aperitivos = Screen (name= 'Aperitivos')
         screen_lasanha = Screen (name= 'Lasanha')
         screen_strogonoff = Screen (name= 'Strog')
         
         screen_login.add_widget(tela_login)
         screen_cadastro.add_widget(tela_cadastro)
         screen_home.add_widget(tela_home)
         screen_pratos.add_widget(tela_pratos)
         screen_entradas.add_widget(TelaEntradas())  
         screen_veganos.add_widget(TelaVeganos())
         screen_sobremesas.add_widget(TelaSobremesas())
         screen_aperitivos.add_widget(TelaAperitivos())
         screen_lasanha.add_widget(TelaLasanha())
         screen_strogonoff.add_widget(TelaStrogonoff())


         sm.add_widget(screen_home)
         sm.add_widget(screen_login)
         sm.add_widget(screen_cadastro)
         sm.add_widget(screen_pratos)
         sm.add_widget(screen_entradas)
         sm.add_widget(screen_veganos)
         sm.add_widget(screen_sobremesas)
         sm.add_widget(screen_aperitivos)
         sm.add_widget(screen_lasanha)
         sm.add_widget(screen_strogonoff)
         
         return sm

if __name__ == '__main__':
     Aplicativos_de_receitas().run()
