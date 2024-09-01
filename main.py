import re, pyperclip, os

playlistString = "www.youtube.com/watch_videos?video_ids="

try:
    noOfVideos = int(input("Enter the number of videos you want to create a playlist of: "));
except:
    print("Please type a numeric value!");

for video in range(1, noOfVideos+1):
    linkOfVideo = input(f"Paste in the Youtube Video Link {video}:");
    # Extract Video ID from link of video using regex

    videoID = re.search(r"v=([^&]+)", linkOfVideo).group(1);
    playlistString += videoID + ","

print(f"Youtube Playlist Generated: {playlistString}");
pyperclip.copy(playlistString);
print("Copied to Clipboard!");

os.system('pause');

