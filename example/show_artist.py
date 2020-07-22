from pynindo import api

for artist in api.charts.youtube.small.json():
    print(api.artist[artist['artistID']])
