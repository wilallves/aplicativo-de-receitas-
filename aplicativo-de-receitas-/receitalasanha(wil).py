from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen

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
            on_press= self.Janela_Modo_Preparo
            )
       

        bottom_layout.add_widget(ingredient_label)
        bottom_layout.add_widget(input_receita)
        bottom_layout.add_widget(self.botao_modo_preparo)
        top_layout.add_widget(foto_lasanha)


        top_layout.add_widget(BoxLayout())


    
        main_layout.add_widget(top_layout)
        main_layout.add_widget(bottom_layout)

        return main_layout

    def Janela_Modo_Preparo(self, instance):
        def build(self): 
            preparation = (
                "1. Cozinhe a massa conforme as instruções do pacote.\n"
                "2. Refogue a cebola e o alho no azeite.\n"
                "3. Adicione a carne moída e cozinhe até dourar.\n"
                "4. Adicione o molho de tomate e tempere com sal e pimenta.\n"
                "5. Em um refratário, alterne camadas de massa, molho, presunto e mussarela.\n"
                "6. Finalize com queijo parmesão ralado por cima.\n"
                "7. Asse em forno pré-aquecido a 180°C por 30 minutos."
            )

            preparation_label = Label(text='Modo de Preparo:\n' + preparation, size_hint_y=None, height=400, color=[1,1,1,1])
            main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
            top_layout = BoxLayout(orientation='horizontal', size_hint_y=100, height=500, size_hint_x=1.5)
            bottom_layout = BoxLayout(orientation='vertical', size_hint_y=None, height=400)


            foto_lasanha = Image(source='lasanha.png', size_hint= (2, 1))
            botao_voltar = Button (
            text='Voltar', 
            halign= 'center',
            color= [1,1,1,1],
            size_hint_y=50, height=50, size_hint_x=0.9,
            pos= (300, 50)
            )
        

            bottom_layout.add_widget(preparation_label)
            top_layout.add_widget(foto_lasanha)


            top_layout.add_widget(BoxLayout())


        
            main_layout.add_widget(top_layout)
            main_layout.add_widget(bottom_layout)

            return main_layout

if __name__ == '__main__':
    RecipeApp().run()

            preparation_label = Label(text='Modo de Preparo:\n' + preparation, size_hint_y=None, height=400)

if __name__ == '__main__':
    RecipeApp().run()
