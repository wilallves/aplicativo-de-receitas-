from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

kv = '''
<BoxLayout>:
    canvas.before:
        Color:
            rgba: 1, 0.5, 0, 1  # cor laranja
        Rectangle:
            pos: self.pos
            size: self.size
<Label>:
    color: 0, 0, 0, 1  # fonte de texto preta
    font_size: '18sp'
    halign: 'left'
    valign: 'top'
    text_size: self.width, None
'''

Builder.load_string(kv)

class RecipeApp(App):
    def build(self):
        self.main_layout = self.create_main_layout()
        return self.main_layout

    def create_main_layout(self):
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

        ingredient_label = Label(text='Ingredientes:\n' + '\n'.join(ingredients), size_hint_y=400, height=300, color=[1,1,1,1])

        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        top_layout = BoxLayout(orientation='horizontal', size_hint_y=100, height=500, size_hint_x=1.5)
        bottom_layout = BoxLayout(orientation='vertical', size_hint_y=None, height=400)

        foto_lasanha = Image(source='pudim.jpg', size_hint= (2, 1))
        input_receita = TextInput (
            hint_text='Adicione um comentário', 
            size_hint_y=50, height=50, size_hint_x=0.9,
            pos= (200, 50),
            multiline= True
            )

        self.botao_modo_preparo = Button (
            text='Modo de Preparo', 
            halign= 'center',
            color= [1,1,1,1],
            size_hint_y=50, height=50, size_hint_x=0.9,
            pos= (300, 50),
            on_press= self.go_to_preparation_mode
            )

        bottom_layout.add_widget(ingredient_label)
        bottom_layout.add_widget(input_receita)
        bottom_layout.add_widget(self.botao_modo_preparo)
        top_layout.add_widget(foto_lasanha)
        top_layout.add_widget(BoxLayout())

        main_layout.add_widget(top_layout)
        main_layout.add_widget(bottom_layout)

        return main_layout

    def go_to_preparation_mode(self, instance):
        preparation = (
            

            """
            suponha o açúcar e a água em uma fôrma de pudim grande (28 cm) e misture até o açúcar dissolver.

Leve ao fogo baixo e deixe cozinhar, sem mexer, por 10 minutos, ou até o caramelo estar marrom. Retire do fogo e com o auxílio das costas de uma colher, espalhe o caramelo por toda a fôrma. Reserve.

Preaqueça o forno em temperatura média (180° C).

No copo do liquidificar, coloque o leite condensado, o leite, os ovos e o amido de milho MAIZENA . Bata até obter uma mistura homogênea.

Transfira a mistura à fôrma de pudim já caramelizada e cubra-a com papel-alumínio.

Coloque a fôrma de pudim dentro de uma assadeira e leve ao forno em banho-maria, por 1 hora, ou até que o pudim esteja assado.

Retire do forno, tire a fôrma de pudim de dentro da assadeira e deixe esfriar. Leve à geladeira, por no mínimo 2 horas.
"""
        )

        preparation_label = Label(text='Modo de Preparo:\n' + preparation,font_size=12, size_hint_y=None, height=400, color=[1,1,1,1])
        top_layout = self.main_layout.children[1]
        bottom_layout = self.main_layout.children[0]

        top_layout.clear_widgets()
        bottom_layout.clear_widgets()

        foto_lasanha = Image(source='pudim.jpg', size_hint= (2, 1))
        
        bottom_layout.add_widget(preparation_label)
        top_layout.add_widget(foto_lasanha)
        top_layout.add_widget(BoxLayout())
      
