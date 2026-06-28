from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle

import screens.data as data


class SettingsScreen(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


        self.orientation = "vertical"
        self.spacing = 20
        self.padding = 40


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


        self.titulo = Label(
            text="CONFIGURAÇÕES",
            font_size=38,
            bold=True,
            color=(0.1,0.4,0.8,1)
        )


        self.status = Label(
            text=self.status_text(),
            font_size=24,
            bold=True,
            color=(0,0.5,0,1)
        )


        testar_audio = Button(
            text="TESTAR ÁUDIO",
            size_hint=(1,0.18),
            background_normal="",
            background_color=(0,0.55,0.2,1),
            color=(1,1,1,1)
        )


        testar_vibra = Button(
            text="TESTAR VIBRAÇÃO",
            size_hint=(1,0.18),
            background_normal="",
            background_color=(0,0.55,0.2,1),
            color=(1,1,1,1)
        )


        voltar = Button(
            text="VOLTAR",
            size_hint=(1,0.18),
            background_normal="",
            background_color=(0,0.45,0.45,1),
            color=(1,1,1,1)
        )


        testar_audio.bind(
            on_press=self.testar_audio
        )


        testar_vibra.bind(
            on_press=self.testar_vibracao
        )


        voltar.bind(
            on_press=self.voltar_home
        )


        self.add_widget(self.titulo)
        self.add_widget(self.status)
        self.add_widget(testar_audio)
        self.add_widget(testar_vibra)
        self.add_widget(voltar)



    def status_text(self):

        return (
            "RECURSOS DE ACESSIBILIDADE\n\n"
            "Áudio de navegação ATIVO\n\n"
            "Vibração ATIVA"
        )



    def on_pre_enter(self):

        self.status.text = self.status_text()



    def testar_audio(self, instance):

        self.status.text = (
            self.status_text()
            +
            "\n\nÁUDIO TESTADO"
        )



    def testar_vibracao(self, instance):

        self.status.text = (
            self.status_text()
            +
            "\n\nVIBRAÇÃO TESTADA"
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