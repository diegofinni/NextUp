import sys
import spotipy
import spotipy.util as util
import json
from private_token import get_token

# This object contains the functions for interacting with the votes on the site
# Input:
#   - filename (str) - the file to import the json of votes
class PlaylistManipulator(object):
    def __init__(self, filename):
        self.filename = filename
        self.dict = self.get_list()
        self.token = get_token()
        self.spotify = spotipy.Spotify(auth=self.token)
        self.username = ""
        self.playlist = ""
        self.track_ids = [""]


    # Change the json file that votes are being loaded from
    def reset_filename(self, filename):
        self.filename = filename

    # Retrieve a list of current votes from the json file
    def get_list(self):
        with open(self.filename) as file:
            return json.load(file)

    # Add a song to the dictionary of songs, starting with a single vote
    def add_new_to_list(self, song):
        song['votes'] = 1
        self.dict[song['id']] = song
        self.set_list()

    # Update the json file to reflect new votes
    def set_list(self):
        with open(self.filename, 'w') as file:
            return json.dump(self.dict, file, indent=2)

    # Returns all of the songs sorted by votes
    def best_songs(self):
        result = list(self.dict.values())
        result.sort(key=lambda song: song['votes'])
        result.reverse()
        return result

    # Increments the number of votes for the specified song
    def vote_for(self, song):
        self.dict[song]['votes'] += 1
        self.set_list()

    def reset_votes(self):  # sets all song votes to zero
        for song in self.dict:
            self.dict[song] = 0
        self.set_list()

    # Retrieves the current most popular song from the dictionary
    def most_popular(self):
        popularVote = 0
        popular = None
        for song in self.dict:
            if popular == None:  # for first song in the list, sets to best
                popular = song
                popularVote = self.dict[song]
            # if equal votes, returns first song in list (ie higher in queue)
            if self.dict[
                song] > popularVote:  # if song has more votes, sets to best
                popularVote = self.dict[song]
                popular = song
        return popular  # returns the string

    # Returns a dictionary of song IDs and names in a given playlist
    def show_tracks(self, tracks):
        result = {}
        for i, item in enumerate(tracks['items']):
            track = item['track']
            result[track['id']] = {
                'id': track['id'],
                'name': track['name'],
                # 'artist': track['artist'],
            }
        return result

    # Takes in a Spotify object and a list of song ids, then sorts the song ids
    # by the number of current votes
    def reorder_playlist(self, song_ids):
        new_order = self.best_songs()
        for i in range(len(new_order) - 1, -1, -1):
            for j in range(len(song_ids)):
                if new_order[i]['id'] == song_ids[j]:
                    song_ids.insert(0, song_ids[j])
                    song_ids.pop(j + 1)
                    self.spotify.user_playlist_reorder_tracks(self.username, self.playlist, j, 0, 1)

    # Takes in a Spotify object and increments the votes for the specified song
    def vote_for_song(self, song):
        # sp = spotipy.Spotify(auth=token)
        self.spotify.trace = False
        results = self.spotify.user_playlist(self.username, self.playlist, fields="tracks,next")
        tracks = results['tracks']
        songs = self.show_tracks(tracks)

        if song not in songs:
            self.spotify.user_playlist_add_tracks(self.username, self.playlist, [song])

            results = self.spotify.user_playlist(self.username, self.playlist, fields="tracks,next")
            tracks = results['tracks']
            songs_new = self.show_tracks(tracks)

            self.add_new_to_list(songs_new[song])

        else:
            self.vote_for(song)

        self.reorder_playlist(list(songs.keys()))