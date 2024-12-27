import os
import csv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from pytube import Search
import yt_dlp as youtube_dl

# Spotify credentials
SPOTIPY_CLIENT_ID = '2ec43e9f84a845b4a3bf191509dc1bdb'
SPOTIPY_CLIENT_SECRET = '8624508c65644a8b8f3c641c22de6f3d'
SPOTIPY_REDIRECT_URI = 'http://localhost:8888/callback'

# Initialize Spotify client
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id=SPOTIPY_CLIENT_ID, 
    client_secret=SPOTIPY_CLIENT_SECRET
))

def get_playlist_name_and_tracks(playlist_url):
    playlist_id = playlist_url.split("/")[-1].split("?")[0]
    playlist = sp.playlist(playlist_id)
    playlist_name = playlist['name']
    tracks = playlist['tracks']['items']
    return playlist_name, tracks

def search_youtube(track_name, artist_name):
    query = f"{track_name} {artist_name}"
    search = Search(query)
    results = search.results
    if results:
        return results[0].watch_url
    return None

def save_tracks_to_csv(tracks, csv_path):
    with open(csv_path, mode='w', encoding='utf-8', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["Title", "Artist", "YouTube URL"])

        for item in tracks:
            track = item['track']
            track_name = track['name']
            artist_name = track['artists'][0]['name']
            youtube_url = search_youtube(track_name, artist_name)

            print(f"\nTrack: {track_name} by {artist_name}")
            print(f"YouTube URL: {youtube_url}\n")

            writer.writerow([track_name, artist_name, youtube_url])

def parse_tracks_csv(file_path):
    with open(file_path, mode='r', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        return [row for row in reader]

def download_and_convert_to_mp3(track, output_dir):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(output_dir, f"{track['Title']}.%(ext)s"),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([track['YouTube URL']])

    original_file_path = os.path.join(output_dir, f"{track['Title']}.webm")
    mp3_file_path = os.path.join(output_dir, f"{track['Title']} - {track['Artist']}.mp3")

    if os.path.exists(original_file_path):
        os.rename(original_file_path, mp3_file_path)

    print(f"Downloaded and converted: {track['Title']} - {track['Artist']}")
