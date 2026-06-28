from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle

import screens.data as data


class PlacesScreen(BoxLayout):

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


        self.montar_tela()



    def montar_tela(self):

        self.clear_widgets()


        titulo = Label(
            text="LOCAIS PRÓXIMOS",
            font_size=34,
            bold=True,
            color=(0.1,0.4,0.8,1),
            size_hint=(1,0.15)
        )


        self.add_widget(titulo)



        lugares = [
            ("Farmácia São João","300 metros"),
            ("Hospital Central","700 metros"),
            ("Mercado Bom Dia","1 km")
        ]



        for nome, distancia in lugares:


            bloco = BoxLayout(
                orientation="vertical",
                spacing=5,
                size_hint=(1,0.23)
            )


            texto = Label(
                text=f"{nome}\n{distancia}",
                font_size=22,
                bold=True,
                color=(0,0,0,1)
            )


            salvar = Button(
                text="SALVAR",
                size_hint=(1,0.35),
                background_normal="",
                background_color=(0,0.45,0.45,1),
                color=(1,1,1,1)
            )


            if nome in data.favoritos:
                salvar.text = "SALVO"



            salvar.bind(
                on_press=lambda x, local=nome, botao=salvar:
                self.salvar_local(local, botao)
            )


            bloco.add_widget(texto)
            bloco.add_widget(salvar)


            self.add_widget(bloco)



        voltar = Button(
            text="VOLTAR",
            size_hint=(1,0.12),
            background_normal="",
            background_color=(0,0.45,0.45,1),
            color=(1,1,1,1)
        )


        voltar.bind(
            on_press=self.voltar_home
        )


        self.add_widget(voltar)




    def salvar_local(self, local, botao):


        if local not in data.favoritos:

            data.favoritos.append(local)

            botao.text = "SALVO"




    def voltar_home(self, instance):

        tela = self.parent

        while tela and not hasattr(tela,"current"):
            tela = tela.parent


        if tela:
            tela.current = "home"




    def update_rect(self,*args):

        self.rect.pos = self.pos
        self.rect.size = self.size