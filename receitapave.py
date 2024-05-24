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
           '''1 pacote de biscoito tipo maisena
              1 lata de leite condensado (395g)
              2 latas de leite (utilize a lata de leite condensado como medida)
              3 gemas de ovos
              2 colheres de sopa de amido de milho (maisena)
              4 colheres de sopa de cacau em pó ou chocolate em pó
              200g de chocolate meio amargo picado
              1 lata de creme de leite sem soro (reserve o soro para umedecer os biscoitos)'''
        ]

        ingredient_label = Label(text='Ingredientes:\n' + '\n'.join(ingredients), size_hint_y=400, height=300, color=[1,1,1,1])

        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        top_layout = BoxLayout(orientation='horizontal', size_hint_y=100, height=500, size_hint_x=1.5)
        bottom_layout = BoxLayout(orientation='vertical', size_hint_y=None, height=400)

        foto_lasanha = Image(source='pave.jpg', size_hint= (2, 1))
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
          Em uma panela, misture o leite condensado, as gemas de ovos, o amido de milho e o cacau em pó até obter uma mistura homogênea.
            Adicione as 2 latas de leite à mistura e leve ao fogo médio, mexendo sempre, até que engrosse e vire um creme. Reserve e deixe esfriar.
            Em uma tigela, derreta o chocolate meio amargo picado em banho-maria ou no micro-ondas, mexendo de vez em quando até ficar completamente derretido e liso. Deixe esfriar um pouco.
            Misture o chocolate derretido com o creme de leite sem soro até obter um creme de chocolate homogêneo. Reserve.
            Em um refratário ou forma de sua preferência, faça uma camada de biscoitos maisena umedecidos no soro do creme de leite.
            Em seguida, coloque uma camada do creme de chocolate sobre os biscoitos.
            Continue alternando camadas de biscoitos umedecidos e creme de chocolate até terminar com uma camada de creme.
            Leve o pavê à geladeira e deixe gelar por pelo menos 4 horas, ou até que esteja firme.
            Antes de servir, você pode decorar o pavê com raspas de chocolate, cacau em pó peneirado ou outros ingredientes de sua preferência.
"""
        )

        preparation_label = Label(text='Modo de Preparo:\n' + preparation,font_size=12, size_hint_y=None, height=400, color=[1,1,1,1])
        top_layout = self.main_layout.children[1]
        bottom_layout = self.main_layout.children[0]

        top_layout.clear_widgets()
        bottom_layout.clear_widgets()

        foto_lasanha = Image(source='pave.jpg', size_hint= (2, 1))
        
        bottom_layout.add_widget(preparation_label)
        top_layout.add_widget(foto_lasanha)
        top_layout.add_widget(BoxLayout())


    def go_back_to_main(self, instance):
        self.main_layout.clear_widgets()
        self.main_layout = self.create_main_layout()
        self.root.add_widget(self.main_layout)

if __name__ == '__main__':
    RecipeApp().run()
