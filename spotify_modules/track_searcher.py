import spotipy
from models.track import Track


def create_track_element(track) -> Track:
    try:
        image_url = track['album']['images'][0]['url']
    except IndexError:
        image_url = None

    return Track(track['uri'], track['name'], track['artists'][0]['name'],
                 track['duration_ms'], image_url, track['preview_url'])


def search_tracks_by_name(access_token: str, track_name: str, country: str) -> list[Track]:
    spotify_object = spotipy.Spotify(auth=access_token)
    result = spotify_object.search(q=track_name, type='track', limit=3, market=country)

    print(result['tracks']['items'][0])

    if result['tracks']['items']:
        tracks = []
        for i in range(3):
            tracks.append(create_track_element(result['tracks']['items'][i]))
        return tracks
    else:
        return []
