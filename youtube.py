from pytube import YouTube

url = input("Enter YouTube video URL: ")
yt = YouTube(url)
print("Title:", yt.title)
print("Length:", yt.length, "seconds")

stream = yt.streams.get_highest_resolution()
stream.download()
print("✅ Video downloaded successfully!")
