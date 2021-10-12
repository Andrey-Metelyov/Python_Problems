def tracklist(**kwargs):
    for artist, albums in kwargs.items():
        print(artist)
        # print(albums)
        for (album, track) in albums.items():
            print("ALBUM:", album, "TRACK:", track)

# tracks = {"Woodkid": {"The Golden Age": "Run Boy Run",
#                       "On the Other Side": "Samara"},
#           "Cure": {"Disintegration": "Lovesong",
#                    "Wish": "Friday I'm in love"}}
#
# tracklist(**tracks)
