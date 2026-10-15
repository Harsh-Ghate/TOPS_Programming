
"""You received a dataset of ratings as strings from Spotify: ['4.5', '3.0', '5', '4.2']. 
Use type casting to convert these to floats, then find and print the highest rating.<br><br><em><strong>Hint:</strong> 
Use the float() function inside a loop or list comprehension.</em"""

Spotify_Ratings = ['4.5','3.0','5','4.2']
print(f"List before type casting: {Spotify_Ratings}")
for value in range(len(Spotify_Ratings)):
    Spotify_Ratings[value] = float(Spotify_Ratings[value])

print(f"Converted ratings: {Spotify_Ratings}")
print(f"Highest rating: {max(Spotify_Ratings)}")