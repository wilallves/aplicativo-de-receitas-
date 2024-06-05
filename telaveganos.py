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
            text="Pratos Principais", 
            size_hint=(0.2, 0.1),
            pos_hint={'center_x': 0.5, 'center_y': 0.85},
            color=[1, 1, 1, 1],
            halign='center',
            font_size=45
        )
        layout_principal.add_widget(label_titulo)

        label_macarrão = Label(
            text="Macarrão", 
            size_hint=(0.2, 0.1),
            pos_hint={'center_x': 0.6, 'center_y': 0.65},
            color=[1, 1, 1, 1],
            halign='center',
            font_size=30
        )
        layout_principal.add_widget(label_macarrão)

        label_tofu = Label(
            text="Tofu", 
            size_hint=(0.2, 0.1),
            pos_hint={'center_x': 0.6, 'center_y': 0.45},
            color=[1, 1, 1, 1],
            halign='center',
            font_size=30
        )
        layout_principal.add_widget(label_tofu)

        foto_macarrão = Image(
            source='C:\\Users\\aluno.sesipaulista\\mamai\\WhatsApp Image 2024-05-30 at 12.57.05.jpeg',
            pos_hint={'center_x': 0.2, 'center_y': 0.6},  
            size_hint=(0.3, 0.4)
        )
        layout_principal.add_widget(foto_macarrão)

        foto_tofu = Image(
            source='C:\\Users\\aluno.sesipaulista\\mamai\\WhatsApp Image 2024-05-30 at 12.55.37.jpeg',
            pos_hint={'center_x': 0.2, 'center_y': 0.4},  
            size_hint=(0.3, 0.4)
        )
        layout_principal.add_widget(foto_tofu)

        botao_macarrão = Button(
            text='Confira já', 
            background_color=get_color_from_hex('#5e2129'),
            size_hint=(0.20, 0.05),
            pos_hint={'center_x': 0.6, 'center_y': 0.6}
        )
        layout_principal.add_widget(botao_macarrão)

        botao_tofu = Button(
            text='Confira já',
            background_color=get_color_from_hex('#5e2129'), 
            size_hint=(0.20, 0.05),
            pos_hint={'center_x': 0.6, 'center_y': 0.4}
        )
        layout_principal.add_widget(botao_tofu)

        return layout_principal

if __name__ == '__main__':
    LoginApp().run()
