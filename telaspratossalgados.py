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

        label_lasanha = Label(
            text="Lasanha", 
            size_hint=(0.2, 0.1),
            pos_hint={'center_x': 0.6, 'center_y': 0.65},
            color=[1, 1, 1, 1],
            halign='center',
            font_size=30
        )
        layout_principal.add_widget(label_lasanha)

        label_strogonoff = Label(
            text="Strogonoff", 
            size_hint=(0.2, 0.1),
            pos_hint={'center_x': 0.6, 'center_y': 0.45},
            color=[1, 1, 1, 1],
            halign='center',
            font_size=30
        )
        layout_principal.add_widget(label_strogonoff)

        label_cuscuz = Label(
            text="Cuscuz", 
            size_hint=(0.2, 0.1),
            pos_hint={'center_x': 0.6, 'center_y': 0.25},
            color=[1, 1, 1, 1],
            halign='center',
            font_size=30
        )
        layout_principal.add_widget(label_cuscuz)

        foto_lasanha = Image(
            source='C:/Users/aluno.sesipaulista/Downloads/08_LASANHA_FINAL-1-min.webp',
            pos_hint={'center_x': 0.2, 'center_y': 0.6},  # Adjusted position to separate from label
            size_hint=(0.3, 0.4)
        )
        layout_principal.add_widget(foto_lasanha)

        foto_strogonoff = Image(
            source='C:/Users/aluno.sesipaulista/Downloads/download (2).jpg',
            pos_hint={'center_x': 0.2, 'center_y': 0.4},  # Adjusted position to separate from label
            size_hint=(0.3, 0.4)
        )
        layout_principal.add_widget(foto_strogonoff)

        foto_cuscuz = Image(
            source='C:/Users/aluno.sesipaulista/Downloads/images (3).jpg',
            pos_hint={'center_x': 0.2, 'center_y': 0.2},  # Adjusted position to separate from label
            size_hint=(0.3, 0.4)
        )
        layout_principal.add_widget(foto_cuscuz)

        botao_lasanha = Button(
            text='Confira já', 
            background_color=get_color_from_hex('#5e2129'),
            size_hint=(0.20, 0.05),
            pos_hint={'center_x': 0.6, 'center_y': 0.6}
        )
        layout_principal.add_widget(botao_lasanha)

        botao_strogonoff = Button(
            text='Confira já',
            background_color=get_color_from_hex('#5e2129'), 
            size_hint=(0.20, 0.05),
            pos_hint={'center_x': 0.6, 'center_y': 0.4}
        )
        layout_principal.add_widget(botao_strogonoff)

        botao_cuscuz = Button(
            text='Confira já',
            background_color=get_color_from_hex('#5e2129'), 
            size_hint=(0.20, 0.05),
            pos_hint={'center_x': 0.6, 'center_y': 0.2}
        )
        layout_principal.add_widget(botao_cuscuz)

        return layout_principal

if __name__ == '__main__':
    LoginApp().run()