from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle


class HomeScreen(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.orientation = "vertical"
        self.spacing = 20
        self.padding = 40


        with self.canvas.before:
            Color(0.95, 0.95, 0.95, 1)

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
            font_size=38,
            bold=True,
            color=(0,0,0,1)
        )


        subtitulo = Label(
            text="Seu guia pela cidade",
            font_size=28,
            color=(0.1,0.4,0.8,1)
        )


        self.add_widget(titulo)
        self.add_widget(subtitulo)


        botoes = [
            "FALAR DESTINO",
            "LOCAIS PRÓXIMOS",
            "FAVORITOS",
            "CONFIGURAÇÕES"
        ]


        for texto in botoes:

            botao = Button(
                text=texto,
                size_hint=(1,0.18),
                font_size=20,
                background_normal="",
                background_color=(0,0.45,0.45,1),
                color=(1,1,1,1)
            )


            if texto == "FALAR DESTINO":
                botao.bind(
                    on_press=self.abrir_voz
                )


            elif texto == "LOCAIS PRÓXIMOS":
                botao.bind(
                    on_press=self.abrir_places
                )


            elif texto == "FAVORITOS":
                botao.bind(
                    on_press=self.abrir_favorites
                )


            elif texto == "CONFIGURAÇÕES":
                botao.bind(
                    on_press=self.abrir_config
                )


            self.add_widget(botao)



    def pegar_manager(self):

        tela = self.parent

        while tela and not hasattr(tela,"current"):
            tela = tela.parent

        return tela



    def abrir_voz(self, instance):

        manager = self.pegar_manager()

        if manager:
            manager.current = "voice"



    def abrir_places(self, instance):

        manager = self.pegar_manager()

        if manager:
            manager.current = "places"



    def abrir_favorites(self, instance):

        manager = self.pegar_manager()

        if manager:
            manager.current = "favorites"



    def abrir_config(self, instance):

        manager = self.pegar_manager()

        if manager:
            manager.current = "settings"



    def update_rect(self,*args):

        self.rect.pos = self.pos
        self.rect.size = self.size