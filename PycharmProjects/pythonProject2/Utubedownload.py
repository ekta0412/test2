import pytube as pt

click="https://www.youtube.com/watch?v=Dppl6iA2G8Q"
video= pt.YouTube(click)

print("The thumbnail is",video.thumbnail_url)
print(video.title)

resolution_info=video.streams.all()
st_list=list(enumerate(resolution_info))
for i in st_list:
    print(i)
User_input=int(input("Enter the category of streaming:"))
resolution_info[User_input].download()
Print("success")