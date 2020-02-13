# NextUp
CMU Hack112 Project

NextUp is a Hack112 (F18) project created by Diego San Miguel, Sean Prendi, Vignesh Rajmohan, and Mae Hoad

NextUp is web app that allows users to connect to a Spotify playlist and vote on what song they want next or add new songs
The website uses client data from the Spotify Developer website and Python scripts using the Spotipy module to complete this function


With regards to NextUp.py:
The purpose of this file is to update the local json file to include all the songs in the Spotify playlist, and then reorder the playlist to have the songs with the most votes appear first on the playlist.
Note this file does NOT add votes to the json file
For this file to work in conjunction with the app you MUST call the file, then add a username ("diegofinni" in our case), followed by an id of the playlist and then the ids of all the tracks you want to add to the playlist
Example of calling file on terminal: python3 NextUp.py diegofinni 5K3rtFT1Tq19lJ04wjuVBV 59WN2psjkt1tyaxjspN8fp
The client data needed for this file to work (CLIENT ID, SECRET, and REDIRECT_URI) are already given
