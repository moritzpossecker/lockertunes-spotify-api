"""Playlist model"""


class Playlist:
    def __init__(self, name: str, description: str, public: bool, collaborative: bool, id: str = None, image_url: str = None):
        self.name = name
        self.description = description
        self.public = public
        self.collaborative = collaborative
        self.id = id
        self.image_url = image_url

    def __repr__(self):
        return (f"Playlist {self.name}: {self.description}\n"
                f"Id: {self.id}\n"
                f"Image URL: {self.image_url}\n"
                f"Collaborative: {self.collaborative}\n"
                f"Public: {self.public}")
