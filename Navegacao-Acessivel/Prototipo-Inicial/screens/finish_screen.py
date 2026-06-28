from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle

import screens.data as data


class FinishScreen(BoxLayout):

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
            text="NAVEGAÇÃO\nACESSÍVEL",
            font_size=38,
            bold=True,
            color=(0,0,0,1),
            size_hint=(1,0.20)
        )


        destino = Label(
            text="DESTINO\nALCANÇADO",
            font_size=30,
            bold=True,
            color=(0.1,0.4,0.8,1),
            size_hint=(1,0.18)
        )


        audio = (
            "ÁUDIO ATIVO"
            if data.audio_ativo
            else "ÁUDIO DESATIVADO"
        )


        vibra = (
            "VIBRAÇÃO ATIVA"
            if data.vibracao_ativa
            else "VIBRAÇÃO DESATIVADA"
        )


        self.info = Label(
            text=
            f"{audio}        {vibra}\n\n"
            "Você chegou ao destino.\n\n"
            "Farmácia São João",
            font_size=22,
            bold=True,
            color=(0,0,0,1),
            size_hint=(1,0.25)
        )


        self.status = Label(
            text="",
            font_size=20,
            bold=True,
            color=(0,0.5,0,1),
            size_hint=(1,0.10)
        )


        salvar = Button(
            text="SALVAR NOS FAVORITOS",
            size_hint=(1,None),
            height=45,
            font_size=22,
            bold=True,
            background_normal="",
            background_color=(0,0.45,0.45,1),
            color=(1,1,1,1)
        )


        finalizar = Button(
            text="FINALIZAR",
            size_hint=(1,None),
            height=45,
            font_size=22,
            bold=True,
            background_normal="",
            background_color=(0,0.45,0.45,1),
            color=(1,1,1,1)
        )


        salvar.bind(
            on_press=self.salvar
        )


        finalizar.bind(
            on_press=self.voltar_home
        )


        self.add_widget(titulo)
        self.add_widget(destino)
        self.add_widget(self.info)
        self.add_widget(self.status)
        self.add_widget(salvar)
        self.add_widget(finalizar)



    def on_pre_enter(self):

        self.montar()



    def salvar(self, instance):

        local = "Farmácia São João"


        if local not in data.favoritos:

            data.favoritos.append(local)

            self.status.text = (
                "LOCAL SALVO NOS FAVORITOS"
            )


        else:

            self.status.text = (
                "LOCAL JÁ ESTÁ NOS FAVORITOS"
            )



    def voltar_home(self, instance):

        tela = self.parent


        while tela and not hasattr(tela,"current"):

            tela = tela.parent


        if tela:

            tela.current = "home"



    def update_rect(self,*args):

        self.rect.pos = self.pos
        self.rect.size = self.size