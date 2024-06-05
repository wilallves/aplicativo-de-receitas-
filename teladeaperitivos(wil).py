from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.utils import get_color_from_hex

Window.size = (360, 640)

class LoginApp(App):
    def build(self):
        Window.clearcolor = (0.9, 0.5, 0, 0)
        
        layout_principal = FloatLayout()

        label_titulo = Label(
            text="Aperitivos", 
            size_hint=(0.2, 0.1),
            pos_hint={'center_x': 0.5, 'center_y': 0.85},
            color=[1, 1, 1, 1],
            halign='center',
            font_size=45
        )
        layout_principal.add_widget(label_titulo)

        label_pizza = Label(
            text="pizza de beringela", 
            size_hint=(0.2, 0.1),
            pos_hint={'center_x': 0.6, 'center_y': 0.65},
            color=[1, 1, 1, 1],
            halign='center',
            font_size=25
        )
        layout_principal.add_widget(label_pizza)

        label_carnes = Label(
            text="tábua de carnes", 
            size_hint=(0.2, 0.1),
            pos_hint={'center_x': 0.6, 'center_y': 0.45},
            color=[1, 1, 1, 1],
            halign='center',
            font_size=25
        )
        layout_principal.add_widget(label_carnes)

        foto_pizza = Image(
            source='C:/Users/aluno.sesipaulista/Desktop/bubble/pizzaa.jpg',
            pos_hint={'center_x': 0.2, 'center_y': 0.6},
            size_hint=(0.3, 0.4)
        )
        layout_principal.add_widget(foto_pizza)

        foto_carne = Image(
            source='C:/Users/aluno.sesipaulista/Desktop/bubble/carnes.jpg',
            pos_hint={'center_x': 0.2, 'center_y': 0.4},
            size_hint=(0.3, 0.4)
        )
        layout_principal.add_widget(foto_carne)

        botao_pizza = Button(
            text='Confira já', 
            background_color=get_color_from_hex('#5e2129'),
            size_hint=(0.20, 0.05),
            pos_hint={'center_x': 0.6, 'center_y': 0.6}
        )
        botao_pizza.bind(on_press=self.on_button_press)
        layout_principal.add_widget(botao_pizza)

        botao_carne = Button(
            text='Confira já',
            background_color=get_color_from_hex('#5e2129'), 
            size_hint=(0.20, 0.05),
            pos_hint={'center_x': 0.6, 'center_y': 0.4}
        )
        botao_carne.bind(on_press=self.on_button_press)
        layout_principal.add_widget(botao_carne)

        return layout_principal

    def on_button_press(self, instance):
        print("Botão pressionado!")

if __name__ == '__main__':
    LoginApp().run()
