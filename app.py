from flask import Flask, jsonify, request, abort
# from algor1 import *
from NextUp import PlaylistManipulator

app = Flask(__name__)

PM = PlaylistManipulator(filename="votes.json")

@app.route('/')
def home():
    return "Hello World"


@app.route('/songs/votes')
def song_dict():
    songs = PM.get_list()
    return jsonify(songs)


@app.route('/songs/ordered')
def ordered_songs():
    songs = PM.best_songs()
    return jsonify(songs)


@app.route('/songs/best')
def best_song():
    songs = PM.most_popular()
    return jsonify(songs)


@app.route('/reset')
def reset_songs():
    songs = PM.reset_votes()
    return jsonify(songs)


@app.route('/vote', methods=['POST'])
def cast_vote():
    song = request.args.get('song')
    PM.vote_for_song(song)
    return "Voted for song"
