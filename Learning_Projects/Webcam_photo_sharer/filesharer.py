from filestack import Client
class FileSharer: 
    """
    Dodanie opcji udostępnienia pliku przy pomocy filestack
    """
    def __init__(self, filepath, api_key = "AJsJnJy26RRiJpg1cIkfCz"):
        self.filepath = filepath
        self.api_key = api_key
    
    def share(self):

        client = Client(self.api_key)
        new_filelink = client.upload(filepath=self.filepath)
        return new_filelink.url