import os
os.environ["KIVY_GL_BACKEND"] = "angle_sdl2"


from kivy.app import App
from kivy.uix.screenmanager import Screen


from screens.home_screen import HomeScreen
from screens.voice_screen import VoiceScreen
from screens.navigation_screen import NavigationScreen
from screens.alert_screen import AlertScreen
from screens.finish_screen import FinishScreen
from screens.places_screen import PlacesScreen
from screens.favorites_screen import FavoritesScreen
from screens.settings_screen import SettingsScreen



class HomeWrapper(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.add_widget(
            HomeScreen()
        )



class VoiceWrapper(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.voice = VoiceScreen()

        self.add_widget(
            self.voice
        )


    def on_pre_enter(self):

        self.voice.atualizar_status()



class NavigationWrapper(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.add_widget(
            NavigationScreen()
        )



class AlertWrapper(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.alert = AlertScreen()

        self.add_widget(
            self.alert
        )


    def on_pre_enter(self):

        self.alert.montar()



class FinishWrapper(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.finish = FinishScreen()

        self.add_widget(
            self.finish
        )


    def on_pre_enter(self):

        self.finish.montar()



class PlacesWrapper(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.add_widget(
            PlacesScreen()
        )



class FavoritesWrapper(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.favorites = FavoritesScreen()

        self.add_widget(
            self.favorites
        )


    def on_pre_enter(self):

        self.favorites.montar()



class SettingsWrapper(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.settings = SettingsScreen()

        self.add_widget(
            self.settings
        )


    def on_pre_enter(self):

        self.settings.on_pre_enter()



class NavegacaoApp(App):

    def build(self):

        from kivy.uix.screenmanager import ScreenManager

        telas = ScreenManager()


        telas.add_widget(
            HomeWrapper(name="home")
        )


        telas.add_widget(
            VoiceWrapper(name="voice")
        )


        telas.add_widget(
            NavigationWrapper(name="navigation")
        )


        telas.add_widget(
            AlertWrapper(name="alert")
        )


        telas.add_widget(
            FinishWrapper(name="finish")
        )


        telas.add_widget(
            PlacesWrapper(name="places")
        )


        telas.add_widget(
            FavoritesWrapper(name="favorites")
        )


        telas.add_widget(
            SettingsWrapper(name="settings")
        )


        return telas



if __name__ == "__main__":

    NavegacaoApp().run()