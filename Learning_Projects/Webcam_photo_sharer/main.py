from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from filesharer import FileSharer
from kivy.core.clipboard import Clipboard
import webbrowser
import time


Builder.load_file('frontend.kv')

class CameraScreen(Screen):

    def start(self):
        """Uruchamia kamerę oraz zmienie napis na przycisku"""
        self.ids.camera.opacity = 1
        self.ids.camera.play = True
        self.ids.camera_button.text = 'STOP CAMERA'
        
    def stop(self):
        """Wyłącza kamerę oraz zmienie napis na przycisku"""
        self.ids.camera.opacity = 0
        self.ids.camera.play = False
        self.ids.camera_button.text = 'START CAMERA'
        self.ids.camera.texture = None
        
    def capture(self):
        """Tworzy plik z aktualną datą i czasem, w którym zapisuje obraz uchwycony przez kamerę"""
        curr_time = time.strftime('%Y%m%d-%H%M%S')
        self.filepath = f"Files/{curr_time}.png"
        self.ids.camera.export_to_png(self.filepath)
        self.manager.current = 'image_screen'
        self.manager.current_screen.ids.img.source = self.filepath

class ImageScreen(Screen):

    link_message = "CREATE A LINK TO THE IMAGE FIRST !" #zmienna klasowa

    def create_link(self):
        """Twprzy link do zdjęcia które zostało wykonane i umieszczone w sieci poprzez klucz API dla filestack"""
        file_path = App.get_running_app().root.ids.camera_screen.filepath
        fileshare = FileSharer(filepath = file_path )
        self.url = fileshare.share()
        self.ids.link.text = self.url
    
    def copy_link(self):
        """Kopiuje link jeśli takowy istnieje, jeśli nie, wyświetla wiadomość o konieczności stworzenia go"""
        try:
            Clipboard.copy(self.url)
        except:
            self.ids.link.text = self.link_message

    def open_link(self):
        """Otwiera w przeglądarce link jeśli takowy istnieje, jeśli nie, wyświetla wiadomość o konieczności stworzenia go"""
        try:
            webbrowser.open(self.url)
        except:
            self.ids.link.text = self.link_message

class RootWidget(ScreenManager):
    pass

class MainApp(App):
    def build(self):
        return RootWidget()
    
MainApp().run()