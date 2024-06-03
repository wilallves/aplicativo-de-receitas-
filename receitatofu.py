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
            '1- 1 bloco de tofu firme',
            '2- 1 bloco de tofu firme',
            '3- 1 colher de sopa de óleo de gergelim',
            '4-1 colher de chá de alho em pó',
            '5- 1 colher de chá de gengibre em pó',
            '6- 1 colher de sopa de suco de limão',
            '7- Sal e pimenta a gosto',
        ]

        ingredient_label = Label(text='Ingredientes:\n' + '\n'.join(ingredients), size_hint_y=400, height=300, color=[1,1,1,1])

        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        top_layout = BoxLayout(orientation='horizontal', size_hint_y=100, height=500, size_hint_x=1.5)
        bottom_layout = BoxLayout(orientation='vertical', size_hint_y=None, height=400)

        foto_lasanha = Image(source='tofu.jpeg', size_hint= (2, 1))
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
            Pressione o tofu para remover o excesso de água enrolando-o em papel toalha e colocando algo pesado em cima por 15-20 minutos.

Enquanto isso, misture em uma tigela pequena: 2 colheres de sopa de molho de soja, 1 colher de sopa de óleo de gergelim, 1 colher de chá de alho em pó, 1 colher de chá de gengibre em pó, 1 colher de sopa de suco de limão, sal e pimenta a gosto.

Corte o tofu em fatias de 1 cm de espessura e coloque em um prato raso.

Despeje a marinada sobre as fatias de tofu, certificando-se de cobrir todos os lados. Deixe marinar por pelo menos 30 minutos, virando ocasionalmente.

Aqueça uma grelha ou frigideira em fogo médio-alto e unte levemente com óleo.

Grelhe as fatias de tofu por cerca de 5-7 minutos de cada lado, ou até dourar.

Sirva quente com seus acompanhamentos favoritos."""
        )

        preparation_label = Label(text='Modo de Preparo:\n' + preparation,font_size=12, size_hint_y=None, height=400, color=[1,1,1,1])
        top_layout = self.main_layout.children[1]
        bottom_layout = self.main_layout.children[0]

        top_layout.clear_widgets()
        bottom_layout.clear_widgets()

        foto_lasanha = Image(source='tofu.jpeg', size_hint= (2, 1))
        
        bottom_layout.add_widget(preparation_label)
        top_layout.add_widget(foto_lasanha)
        top_layout.add_widget(BoxLayout())


    def go_back_to_main(self, instance):
        self.main_layout.clear_widgets()
        self.main_layout = self.create_main_layout()
        self.root.add_widget(self.main_layout)

if _name_ == '_main_':
    RecipeApp().run()
