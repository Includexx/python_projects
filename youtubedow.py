from pytube import YouTube
link = "https://youtu.be/948HV9e4piw?si=Dhee2wDg3aRH9F_8"
youtube_1 = YouTube(link)

#print(youtube_1.title)
#print(youtube_1.thumbnail_url)
videos = youtube_1.streams.all()
vid = list(enumerate(videos))
for i in vid :
    print(i)
    
print()
strm = int(input( "ENTER :"))
videos[strm].download()
print(" succefully ")    