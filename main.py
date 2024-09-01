import os
import re
import pyperclip

playlistLink = "https://www.youtube.com/watch_videos?video_ids="
cmpLink = playlistLink
videoNumber = 1


while True:
    videoLink = input("Paste in Youtube Video Link {0} (or press Enter to finish): ".format(videoNumber))

    # Check if user presses enter
    if videoLink.isspace() or videoLink == "":
        break

    try:
        videoLink = re.search(r"v=([^&]+)", videoLink).group(1)
        playlistLink += videoLink + ","
        videoNumber += 1
    except AttributeError:
        print("Invalid Youtube Link. Please try again")
        continue

# Remove the trailing ","
playlistLink = playlistLink.strip(',')


# Check if there was any YouTube links provided
if len(playlistLink) > len(cmpLink):
    print(f"\nYouTube Playlist Generated: {playlistLink}")
    cpyToClip = input("Do you want to copy your playlist to clipboard? (y/N): ")
    if cpyToClip.lower() == "y":
        pyperclip.copy(playlistLink)
        print("Copied to Clipboard!")
elif len(playlistLink) <= len(cmpLink):
    print("No valid YouTube links were provided.")

os.system('pause')
