"""Track model"""


class Track:
    def __init__(self, uri, title, artist, duration_ms, image_url):
        self.uri = uri
        self.title = title
        self.artist = artist
        self.duration_ms = duration_ms
        self.image_url = image_url

    def __repr__(self):
        return (f"{self.title} by {self.artist}\n"
                f"Duration: {self.duration_ms}\n"
                f"Cover: {self.image_url}\n"
                f"Uri: {self.uri}")
