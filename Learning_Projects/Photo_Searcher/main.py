from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
import wikipedia
import requests 


Builder.load_file('frontend.kv')

class FirstScreen(Screen):

    def search_image(self):
        # pobiera wpisana wartość
        query = self.manager.current_screen.ids.user_query.text
        #wyszukanie wpisanej frazy 
        page = wikipedia.page(query)
        #wybór obrazu
        image_link = page.images[0]

        #pobranie obrazu
        req = requests.get(image_link)
        imagepath = 'image.jpg'
        with open(imagepath, 'wb') as file:
            file.write(req.content)
        
        self.manager.current_screen.ids.img.source = imagepath



class RootWidget(ScreenManager):
    pass


class MainApp(App):

    def build(self):
        return RootWidget()

MainApp().run()