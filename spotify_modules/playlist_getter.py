import spotipy
from models.playlist import Playlist


def get_playlists(access_token: str, user_id: str) -> list[Playlist]:
    spotify_object = spotipy.Spotify(auth=access_token)

    playlists = []
    results = spotify_object.user_playlists(user=user_id)

    while results:
        playlists.extend(results['items'])
        results = spotify_object.next(results)

    playlists_result = []
    for playlist in playlists:
        image_url = None
        if playlist["images"]:
            if playlist["images"][0]:
                image_url = playlist["images"][0]["url"]
        playlists_result.append(Playlist(
            name=playlist["name"],
            description=playlist["description"],
            public=playlist["public"],
            collaborative=playlist["collaborative"],
            id=playlist["id"],
            image_url=image_url,
        ))

    return playlists_result
