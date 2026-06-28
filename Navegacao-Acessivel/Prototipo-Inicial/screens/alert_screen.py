from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle

import screens.data as data


class AlertScreen(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.orientation="vertical"
        self.spacing=20
        self.padding=40


        with self.canvas.before:
            Color(0.95,0.95,0.95,1)

            self.rect=Rectangle(
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


        self.add_widget(
            Label(
                text="NAVEGAÇÃO\nACESSÍVEL",
                font_size=38,
                bold=True,
                color=(0,0,0,1)
            )
        )


        self.add_widget(
            Label(
                text="ALERTA",
                font_size=30,
                bold=True,
                color=(0.1,0.4,0.8,1)
            )
        )


        self.add_widget(
            Label(
                text="!",
                font_size=80,
                bold=True,
                color=(0.9,0.3,0.1,1)
            )
        )


        audio = "ÁUDIO ATIVO" if data.audio_ativo else "ÁUDIO DESATIVADO"

        vibra = "VIBRAÇÃO ATIVA" if data.vibracao_ativa else "VIBRAÇÃO DESATIVADA"


        self.add_widget(
            Label(
                text=f"{audio}        {vibra}\n\n"
                     "Mensagem de alerta:\n"
                     "Travessia próxima.\n"
                     "Prepare-se para atravessar.",
                font_size=22,
                bold=True,
                color=(0,0,0,1)
            )
        )


        botao=Button(
            text="OK",
            size_hint=(1,None),
            height=45,
            font_size=22,
            bold=True,
            background_normal="",
            background_color=(0,0.45,0.45,1),
            color=(1,1,1,1)
        )


        botao.bind(
            on_press=self.abrir_final
        )


        self.add_widget(botao)



    def on_pre_enter(self):

        self.montar()



    def abrir_final(self, instance):

        tela=self.parent

        while tela and not hasattr(tela,"current"):
            tela=tela.parent


        if tela:
            tela.current="finish"



    def update_rect(self,*args):

        self.rect.pos=self.pos
        self.rect.size=self.size