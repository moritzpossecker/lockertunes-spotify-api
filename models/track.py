"""Track model"""


class Track:
    def __init__(self, url: str, title: str, artist: str, duration_ms: int, image_url: str, preview_url: str):
        self.url = url
        self.title = title
        self.artist = artist
        self.duration_ms = duration_ms
        self.image_url = image_url
        self.preview_url = preview_url

    def to_dict(self):
        return {
            "url": self.url,
            "title": self.title,
            "artist": self.artist,
            "duration_ms": self.duration_ms,
            "image_url": self.image_url,
            "preview_url": self.preview_url}

    def __repr__(self):
        return (f"{self.title} by {self.artist}\n"
                f"Duration: {self.duration_ms}\n"
                f"Cover: {self.image_url}\n"
                f"Uri: {self.url}")
