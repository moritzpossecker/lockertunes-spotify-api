import spotipy
from models.track import Track


def search_track_by_name(access_token: str, track_name: str, country: str) -> Track | None:
    spotify_object = spotipy.Spotify(auth=access_token)
    result = spotify_object.search(q=track_name, type='track', limit=1, market=country)

    if result['tracks']['items']:
        track = result['tracks']['items'][0]
        return Track(track['uri'], track['name'], track['artists'][0]['name'],
                     track['duration_ms'], track['album']['images'][0]['url'])
    else:
        return None
