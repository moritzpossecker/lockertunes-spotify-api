from flask import Flask, jsonify
from flask_cors import CORS
from spotify_modules.track_searcher import search_tracks_by_name
app = Flask(__name__)
CORS(app)


def format_wildcard_strings(value: str) -> str:
    value = value.replace('SPACE', ' ')
    return value.replace('SLASH', '/')


@app.route('/search-tracks-by-name/<string:access_token>/<string:track_name>/<string:country>', methods=['GET'])
def request_search_tracks_by_name(access_token: str, track_name: str, country: str):
    tracks_dict = []
    tracks = search_tracks_by_name(access_token, format_wildcard_strings(track_name), country)
    for track in tracks:
        tracks_dict.append(track.to_dict())
    return jsonify(tracks_dict), 201


if __name__ == '__main__':
    app.run(debug=True, port=5001)
