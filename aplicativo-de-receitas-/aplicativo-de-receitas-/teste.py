from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Rectangle
from kivy.core.window import Window
from kivy.uix.image import Image

Window.size = (900,500)

class LoginApp(App):
    def build(self):
        Window.clearcolor=(0.9, 0.5, 0, 0)
        
        layout_principal = FloatLayout()

        label_titulo = Label(
            text="Prato Principais", 
            size_hint=(.2, .5),
            pos=(495, 420),
            color = [1,1,1,1],
            halign = ('center'),
            font_size = 45
        )
        layout_principal.add_widget(label_titulo)

        label_lasanha = Label(
            text="Lasanha", 
            size_hint=(.2, .5),
            pos=(450, 370),
            color = [1,1,1,1],
            halign = ('center'),
            font_size = 35
        )
        layout_principal.add_widget(label_lasanha)

        label_strogonoff = Label(
            text="Strogonoff", 
            size_hint=(.2, .5),
            pos=(450, 220),
            color = [1,1,1,1],
            halign = ('center'),
            font_size = 35
        )
        layout_principal.add_widget(label_strogonoff)

        label_cuscuz = Label(
            text="Cuscuz", 
            size_hint=(.2, .5),
            pos=(450, 25),
            color = [1,1,1,1],
            halign = ('center'),
            font_size = 35
        )
        layout_principal.add_widget(label_cuscuz)

        foto_lasanha = Image(
            source='C:/Users/aluno.sesipaulista/Downloads/08_LASANHA_FINAL-1-min.webp',
            pos=(100, 350),
            size_hint= (.2, .5)

            )
        layout_principal.add_widget(foto_lasanha)

        foto_strogonoff = Image(
            source='C:/Users/aluno.sesipaulista/Downloads/meat-strogonoff-with-rice-and-straw-potato-over-wooden-table.webp',
            pos=(100, 180),
            size_hint= (.2, .5)
            )
        
        layout_principal.add_widget(foto_strogonoff)

        foto_cuscuz = Image(
            source='C:/Users/aluno.sesipaulista/Downloads/cuscuz-nordestino-recheado-2.jpg',
            pos=(100, 0),
            size_hint= (.2, .5)
            )
        
        layout_principal.add_widget(foto_cuscuz)

        botao_lasanha= Button(
            text='Confira já', 
            size_hint = (.2, .1),
            pos_hint = {'center_x':.5,'center_y':.75}
        )
        layout_principal.add_widget(botao_lasanha)

        botao_strogonoff= Button(
            text='Confira já', 
            size_hint = (.2, .1),
            pos_hint = {'center_x':.5,'center_y':.50}
        )

        layout_principal.add_widget(botao_strogonoff)

        botao_cuscuz = Button(
            text='Confira já', 
            size_hint = (.2, .1),
            pos_hint = {'center_x':.5, 'center_y':.20}
        )
        
        layout_principal.add_widget(botao_cuscuz)

        
        return layout_principal


LoginApp().run()