# lockertunes-spotify-api

Get and post data from [spotify API](https://developer.spotify.com/documentation/web-api).

## How to use

This API contains following endpoints:

- /search-tracks-by-name/`access_token: string`/`track_name: string`/`country: string`

### Formatting
In general should be applied to all user input values, e.g. `track_name`

- Slashes should be replaced with `SLASH`
- Spaces should be replaced with `SPACE`
