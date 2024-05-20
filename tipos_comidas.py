from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.uix.label import Label

class MyScreen(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.clearcolor = get_color_from_hex("#ff8e31")
        self.cols = 2
        self.size_hint = (1, 1)

        self.title_label = Label(text="Menu", font_size="30sp", halign="justify", valign="top", size_hint=(0, 1), height="50dp", pos_hint={'center_x': 0.6, 'center_y': 0.5})
        self.add_widget(self.title_label)

        # Adicione as imagens e botões
        self.image_layout = GridLayout(cols=2)
        self.add_widget(self.image_layout)
        self.add_pratos_de_entrada_image_and_button()
        self.add_veganos_image_and_button()
        self.add_sobremesa_image_and_button()
        self.add_aperitivo_image_and_button()

    def add_pratos_de_entrada_image_and_button(self):
        self.image1 = Image(source=r'C:\Users\aluno.sesipaulista\Desktop\aplicativo-de-receitas-\1.jpeg', size_hint=(1, None), height='200dp', pos_hint={'center_x': 0.5, 'center_y': 0.6})
        self.button1 = Button(text='pratos de entrada', size_hint=(0.5, None), height='30dp', background_color=('#010101'), color=(1, 1, 1, 1), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        self.button1.bind(on_release=self.on_button_release)
        self.layout1 = BoxLayout(orientation='vertical')
        self.layout1.add_widget(self.image1)
        self.layout1.add_widget(self.button1)
        self.add_widget(self.layout1)

    def add_veganos_image_and_button(self):
        self.image2 = Image(source=r'C:\Users\aluno.sesipaulista\Desktop\aplicativo-de-receitas-\2.jpeg', size_hint=(1, None), height='200dp')
        self.button2 = Button(text='veganos', size_hint=(0.5, None), height='30dp', background_color=('#010101'), color=(1, 1, 1, 1), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        self.layout2 = BoxLayout(orientation='vertical')
        self.button2.bind(on_release=self.on_button_release)
        self.layout2.add_widget(self.image2)
        self.layout2.add_widget(self.button2)
        self.add_widget(self.layout2)

    def add_sobremesa_image_and_button(self):
        self.image3 = Image(source=r'C:\Users\aluno.sesipaulista\Desktop\aplicativo-de-receitas-\3.jpeg', size_hint=(1, None), height='200dp')
        self.button3= Button(text='sobremesas', size_hint=(0.5, None), height='30dp', background_color=('#010101'), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        self.layout3 = BoxLayout(orientation='vertical')
        self.button3.bind(on_release=self.on_button_release)
        self.layout3.add_widget(self.image3)
        self.layout3.add_widget(self.button3)
        self.add_widget(self.layout3)

    def add_aperitivo_image_and_button(self):
        self.image4 = Image(source=r'C:\Users\aluno.sesipaulista\Desktop\aplicativo-de-receitas-\4.jpeg', size_hint=(1, None), height='200dp')
        self.button4 = Button(text='aperitivos', size_hint=(0.5, None), height='30dp', background_color=('#010101'), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        self.button4.bind(on_release=self.on_button_release)
        self.layout4 = BoxLayout(orientation='vertical')
        self.layout4.add_widget(self.image4)
        self.layout4.add_widget(self.button4)
        self.add_widget(self.layout4)

    def on_button_release(self, instance):
        print('Botão liberado')

class MyApp(App):
    def build(self):
        return MyScreen()

if __name__ == '__main__':
    MyApp().run()