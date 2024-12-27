import os
from utils import *

def main(playlist_url):
    playlist_name, tracks = get_playlist_name_and_tracks(playlist_url)

    output_dir = os.path.join("output", playlist_name)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    csv_path = os.path.join(output_dir, "tracks.csv")

    save_tracks_to_csv(tracks, csv_path)
    parsed_tracks = parse_tracks_csv(csv_path)

    for track in parsed_tracks:
        if track['YouTube URL']:
            download_and_convert_to_mp3(track, output_dir)

    if os.path.exists(csv_path):
        os.remove(csv_path)

    
    print(f"Tracks downloaded and saved in: {output_dir}")

if __name__ == "__main__":
    playlist_url = input("Enter Spotify playlist URL: ").strip()
    main(playlist_url)
