import yt_dlp

url = input("Enter the youtube video url: ")
saving_path = input("Enter the saving path: ")

ydl_opts = {
    'outtmpl' : f'{saving_path}/%(title)s.%(ext)s',
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

print(f"Video downloaded is successfully")

print(f"Video saved to {saving_path}")