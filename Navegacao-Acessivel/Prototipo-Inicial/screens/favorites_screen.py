from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.graphics import Color, Rectangle

import screens.data as data



class FavoritesScreen(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.orientation = "vertical"
        self.spacing = 15
        self.padding = 35


        with self.canvas.before:

            Color(0.95,0.95,0.95,1)

            self.rect = Rectangle(
                size=self.size,
                pos=self.pos
            )


        self.bind(
            size=self.update_rect,
            pos=self.update_rect
        )


        self.montar()



    def montar(self):

        self.clear_widgets()



        titulo = Label(
            text="FAVORITOS",
            font_size=36,
            bold=True,
            color=(0.1,0.4,0.8,1),
            size_hint=(1,None),
            height=70
        )


        self.add_widget(titulo)



        lista = BoxLayout(
            orientation="vertical",
            spacing=20,
            size_hint_y=None
        )


        lista.bind(
            minimum_height=lista.setter("height")
        )



        if data.favoritos:


            for local in data.favoritos:


                card = BoxLayout(
                    orientation="vertical",
                    spacing=8,
                    size_hint_y=None,
                    height=170
                )


                nome = Label(
                    text=local,
                    font_size=26,
                    bold=True,
                    color=(0,0,0,1),
                    size_hint_y=None,
                    height=45
                )


                info = Label(
                    text="Local salvo\nRota disponível",
                    font_size=18,
                    color=(0.2,0.2,0.2,1),
                    size_hint_y=None,
                    height=55
                )


                remover = Button(
                    text="REMOVER",
                    size_hint_y=None,
                    height=45,
                    background_normal="",
                    background_color=(0.8,0.2,0.2,1),
                    color=(1,1,1,1)
                )


                remover.bind(
                    on_press=lambda x, item=local:
                    self.remover_favorito(item)
                )


                card.add_widget(nome)
                card.add_widget(info)
                card.add_widget(remover)


                lista.add_widget(card)



        else:

            vazio = Label(
                text="NENHUM LOCAL SALVO",
                font_size=24,
                bold=True,
                color=(0,0,0,1),
                size_hint_y=None,
                height=80
            )


            lista.add_widget(vazio)




        scroll = ScrollView(
            size_hint=(1,1)
        )


        scroll.add_widget(lista)


        self.add_widget(scroll)



        voltar = Button(
            text="VOLTAR",
            size_hint=(1,None),
            height=70,
            font_size=22,
            bold=True,
            background_normal="",
            background_color=(0,0.45,0.45,1),
            color=(1,1,1,1)
        )


        voltar.bind(
            on_press=self.voltar_home
        )


        self.add_widget(voltar)





    def remover_favorito(self, local):

        if local in data.favoritos:

            data.favoritos.remove(local)


        self.montar()




    def voltar_home(self, instance):

        tela = self.parent


        while tela and not hasattr(tela,"current"):

            tela = tela.parent



        if tela:

            tela.current="home"





    def update_rect(self,*args):

        self.rect.pos=self.pos
        self.rect.size=self.size