# Import necessary libraries
import yt_dlp
import yaml
from yt_dlp.utils import DownloadError
import logging

# Set up logging to file with level of INFO
logging.basicConfig(filename='app.log', level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def download_playlist(playlist_url, config):
    # Wrap the entire process in a try/except block to catch and handle exceptions
    try:
        # Open and read the configuration file
        with open(config, 'r') as file:
            ydl_opts = yaml.safe_load(file)

        # Use yt_dlp to download the playlist
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([playlist_url])

        # Print a message to the console upon successful download
        print('Download completed successfully')
        print(f"Playlist saved to {ydl_opts['outtmpl']}")

        # Log the download success
        logging.info('Playlist downloaded successfully')

    # Handle specific exceptions
    except FileNotFoundError:

        # Handle case where YAML configuration file cannot be found
        print('The specified YAML configuration file could not be found.')
        logging.error('The specified YAML configuration file could not be found.')

    except DownloadError:

        # Handle case where there's an error in the download process
        print('There was an error downloading the video(s). Make sure the URL is correct and the video(s) are accessible')
        logging.error('There was an error downloading the video(s). Make sure the URL is correct and the video(s) are accessible')

    except Exception as e:
        
        # Handle any other unexpected exceptions
        print(f'An unexpected error occurred: {e}')
        logging.error(f'An unexpected error occurred: {e}')

# Get the URL of the playlist from the user
playlist_url = input("Enter the YouTube playlist URL: ")

# Define the path to the configuration file
config = 'config.yaml'

# Call the function to download the playlist
download_playlist(playlist_url, config)