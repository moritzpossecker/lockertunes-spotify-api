import spotipy
from models.playlist import Playlist
from models.track import Track
from track_searcher import create_track_element


def get_track_list(playlist_id: str, access_token: str) -> list[Track] | None:
    spotify_object = spotipy.Spotify(auth=access_token)
    if playlist_id is None:
        return None

    results = spotify_object.playlist_items(playlist_id, limit=None)

    track_list = []
    for item in results['items']:
        track = item['track']
        track_list.append(create_track_element(track))
    return track_list


def get_playlists(access_token: str, user_id: str) -> list[Playlist]:
    spotify_object = spotipy.Spotify(auth=access_token)

    playlists = []
    results = spotify_object.user_playlists(user=user_id)

    while results:
        playlists.extend(results['items'])
        results = spotify_object.next(results)

    playlists_result = []
    for playlist in playlists:
        try:
            image_url = playlist["images"][0]["url"]
        except IndexError:
            image_url = None
        playlists_result.append(Playlist(
            name=playlist["name"],
            description=playlist["description"],
            public=playlist["public"],
            collaborative=playlist["collaborative"],
            id=playlist["id"],
            image_url=image_url
        ))

    return playlists_result
