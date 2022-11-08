from pytube import YouTube

link = input("Enter The Youtube URL :: ")
yt = YouTube(link)
videos = yt.streams.all()

video =list(enumerate(videos))
for i in video:
    print(i)

print("Enter The Desired Download Format :: ")
dn_option = int (input("Enter The Option :: "))
dn_video = videos[dn_option]
dn_video.download()

print("Downloaded Successfully")
