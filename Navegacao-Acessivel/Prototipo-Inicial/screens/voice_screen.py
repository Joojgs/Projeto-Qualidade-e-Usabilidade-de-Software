from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle

import screens.data as data



class MicrofoneWidget(Button):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.text = "MICROFONE"

        self.font_size = 30
        self.bold = True

        self.background_normal = ""

        self.background_color = (
            0,
            0.55,
            0.55,
            1
        )

        self.color = (
            1,
            1,
            1,
            1
        )





class VoiceScreen(BoxLayout):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


        self.orientation = "vertical"

        self.spacing = 12

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



        titulo = Label(
            text="NAVEGAÇÃO\nACESSÍVEL",
            font_size=34,
            bold=True,
            color=(0,0,0,1),
            size_hint=(1,None),
            height=90
        )



        comando = Label(
            text="DIZER DESTINO",
            font_size=28,
            bold=True,
            color=(0.1,0.4,0.8,1),
            size_hint=(1,None),
            height=55
        )



        microfone = MicrofoneWidget(
            size_hint=(1,None),
            height=130
        )



        self.status = Label(
            text="",
            font_size=22,
            bold=True,
            color=(0,0,0,1),
            size_hint=(1,None),
            height=70
        )



        falar = Button(
            text="TOQUE PARA FALAR",
            size_hint=(1,None),
            height=45,
            font_size=22,
            bold=True,
            background_normal="",
            background_color=(0,0.45,0.45,1),
            color=(1,1,1,1)
        )



        cancelar = Button(
            text="CANCELAR",
            size_hint=(1,None),
            height=45,
            font_size=22,
            bold=True,
            background_normal="",
            background_color=(0,0.45,0.45,1),
            color=(1,1,1,1)
        )


        falar.bind(
            on_press=self.abrir_navegacao
        )


        cancelar.bind(
            on_press=self.voltar
        )



        self.add_widget(titulo)
        self.add_widget(comando)
        self.add_widget(microfone)
        self.add_widget(self.status)
        self.add_widget(falar)
        self.add_widget(cancelar)



        self.atualizar_status()






    def on_pre_enter(self):

        self.atualizar_status()






    def atualizar_status(self):

        audio = (
            "ÁUDIO ATIVO"
            if data.audio_ativo
            else
            "ÁUDIO DESATIVADO"
        )


        vibra = (
            "VIBRAÇÃO ATIVA"
            if data.vibracao_ativa
            else
            "VIBRAÇÃO DESATIVADA"
        )


        self.status.text = (
            audio +
            "\n" +
            vibra
        )






    def abrir_navegacao(self, instance):

        tela = self.parent


        while tela and not hasattr(tela,"current"):

            tela = tela.parent


        if tela:

            tela.current="navigation"






    def voltar(self, instance):

        tela = self.parent


        while tela and not hasattr(tela,"current"):

            tela = tela.parent


        if tela:

            tela.current="home"






    def update_rect(self,*args):

        self.rect.pos=self.pos

        self.rect.size=self.size