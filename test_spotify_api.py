import spotipy
import sys
from spotipy.oauth2 import SpotifyClientCredentials

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id='fd63f6cdd7b34c4e8fbd7def9d4487b3',client_secret='f954aa59c7dd468ca6867d2b3024433b'))

if len(sys.argv) > 1:
    name = ' '.join(sys.argv[1:])
else:
    name = 'Dhvani Bhanushali'

results = spotify.search(q='artist:' + name, type='artist')
items = results['artists']['items']
# if len(items) > 0:
    # artist = items[0]
    # print(artist['uri'])
    # print(artist['name'], artist['images'][0]['url'])

# artist_uri = "spotify:artist:2WX2uTcsvV5OnS0inACecP"

print(items[0])

results = spotify.artist_top_tracks(items[0]['uri'])
# final_result=results['tracks'][:10]
# for track in results['tracks'][:1]:
#     print(track)
