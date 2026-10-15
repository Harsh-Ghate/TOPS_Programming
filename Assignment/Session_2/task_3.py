
"""Demonstrate the difference between single-line and multi-line comments in Python by writing a script that explains 
how a Spotify playlist recommendation system might work. 
Use # for single-line and triple quotes for multi-line comments"""


# Single-line comment: Importing no external libraries is needed for this example.

"""
Multi-line comment:
A Spotify playlist recommendation system can suggest songs
based on a user's listening history, favorite artists, genres,
and previously liked songs.
"""

# Store the user's favorite music genre
favorite_genre = "Dream Pop"

# Store the user's favorite artist
favorite_artist = "Lana Del Rey"

"""
The system uses the user's preferences to recommend songs.
In a real recommendation system, additional factors such as
listening history, song similarity, and user activity may
also be considered.
"""

# Display the user's preferences
print("Favorite Genre:", favorite_genre)
print("Favorite Artist:", favorite_artist)

# Recommend a playlist based on the favorite genre
recommended_playlist = favorite_genre + " Hits Playlist"

print("Recommended Playlist:", recommended_playlist)
