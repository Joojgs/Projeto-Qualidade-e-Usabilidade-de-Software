from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle


class NavigationScreen(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.orientation = "vertical"
        self.spacing = 10
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
            size_hint=(1,0.18)
        )


        rota = Label(
            text="CONFIRMAR ROTA",
            font_size=28,
            bold=True,
            color=(0.1,0.4,0.8,1),
            size_hint=(1,0.15)
        )


        destino = Label(
            text="DESTINO:\n\nFARMÁCIA SÃO JOÃO\n\nDISTÂNCIA:\n300 m\n\nTEMPO ESTIMADO:\n3 MINUTOS",
            font_size=22,
            bold=True,
            color=(0,0,0,1),
            size_hint=(1,0.45)
        )


        voltar = Button(
            text="VOLTAR",
            size_hint=(1,0.12),
            background_normal="",
            background_color=(0,0.45,0.45,1),
            color=(1,1,1,1)
        )


        atualizar = Button(
            text="ATUALIZAR",
            size_hint=(1,0.12),
            background_normal="",
            background_color=(0,0.45,0.45,1),
            color=(1,1,1,1)
        )


        voltar.bind(
            on_press=self.voltar
        )


        
        atualizar.bind(
            on_press=self.abrir_alerta
        )


        self.add_widget(titulo)
        self.add_widget(rota)
        self.add_widget(destino)
        self.add_widget(voltar)
        self.add_widget(atualizar)



    def abrir_alerta(self, instance):

        tela = self.parent

        while tela and not hasattr(tela, "current"):
            tela = tela.parent


        if tela:
            tela.current = "alert"



    def voltar(self, instance):

        tela = self.parent

        while tela and not hasattr(tela, "current"):
            tela = tela.parent


        if tela:
            tela.current = "voice"



    def update_rect(self,*args):

        self.rect.pos = self.pos
        self.rect.size = self.size