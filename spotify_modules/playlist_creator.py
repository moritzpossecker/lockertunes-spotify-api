import spotipy
from models.playlist import Playlist
from models.track import Track
import random


def add_required_tracks_to_playlist(required_tracks: list[Track], spotify_object: spotipy.Spotify,
                                    playlist_id: str) -> int:
    duration_ms = 0
    for track in required_tracks:
        duration_ms += track.duration_ms
        spotify_object.playlist_add_items(playlist_id, [track.url])

    return duration_ms


def add_optional_tracks_to_playlist(optional_tracks: list[Track], spotify_object: spotipy.Spotify, playlist_id: str,
                                    current_duration_ms: int, max_duration_ms) -> None:
    len_optional_tracks = len(optional_tracks)
    for i in range(len_optional_tracks):
        rand_index = random.randrange(0, len(optional_tracks))
        track = optional_tracks[rand_index]
        current_duration_ms += track.duration_ms
        if current_duration_ms > max_duration_ms:
            break
        spotify_object.playlist_add_items(playlist_id, [track.url])
        optional_tracks.remove(track)


def create_playlists(access_token: str, user_id: str, playlists: list[Playlist],
                     required_tacks: list[Track], optional_tracks: list[Track], duration_ms: int) -> None:
    spotify_object = spotipy.Spotify(auth=access_token)

    for playlist in playlists:
        playlist = spotify_object.user_playlist_create(user_id, playlist.name, False,
                                                       playlist.collaborative, playlist.description)
        current_duration_ms = add_required_tracks_to_playlist(required_tacks, spotify_object, playlist['id'])
        add_optional_tracks_to_playlist(optional_tracks, spotify_object, playlist['id'],
                                        current_duration_ms, duration_ms)
