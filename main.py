"""

This Program goes to a Youtube channel and then gets the transcripts for each
Youtube video on the channel and then it puts said transcripts into text files.

The program then searches for a word or multiple words in the text files to see
how many times those words were said across the channel.

"""

# If you are using IDLE, run in 3.7

from apiclient.discovery import build
from youtube_transcript_api import YouTubeTranscriptApi
from pytube import YouTube
import os

# Your Google API Key
api_key = "Your Youtube API"
# The Youtube channel you want to extract data from
channel_id = "YouTube Channel"
# Youtube Build
youtube = build('youtube', 'v3', developerKey=api_key)

def get_channel_videos(channel_id):
 
    # get Uploads playlist id
    res = youtube.channels().list(id=channel_id,
                                  part='contentDetails').execute()
    playlist_id = res['items'][0]['contentDetails']['relatedPlaylists']['uploads']
    videos = []
    next_page_token = None
 
    while 1:
        res = youtube.playlistItems().list(playlistId=playlist_id,
                                           part='snippet',
                                           maxResults=50,
                                           pageToken=next_page_token).execute()
        videos += res['items']
        next_page_token = res.get('nextPageToken')
 
        if next_page_token is None:
            break
 
    return videos
 
videos = get_channel_videos(channel_id)
video_ids = []  # list of all video_id of channel
video_titles = []

# Word to search for
word1 = "firework"

# Counter for the text files
counter = 1

for video in videos:
    video_ids.append(video['snippet']['resourceId']['videoId'])

# Loops through every video on the youtube channel
for video_id in video_ids:
    try:
        # Gets the transcripts of youtube videos. Only gets English transcripts.
        responses = YouTubeTranscriptApi.get_transcript(
            video_id, languages=['en'])

        # Get's the youtube video's link
        yt = YouTube("https://www.youtube.com/watch?v="+str(video_id))
        
        #print('\n'+"Video: "+"https://www.youtube.com/watch?v="+str(video_id)+'\n'+'\n'+"Captions:")
        print("\n"+"Video Number: "+str(counter)+'\n'+"Video: "+"https://www.youtube.com/watch?v="+str(video_id)+'\n'+'Title: '+yt.title+'\n'+"Firework/s Wordcount:")

        
        # This is for text file generation
        filename = "video #" + str(counter) + ".txt"

        # Generates text file
        with open(filename, "w") as file:
            # Writes the title of the Youtube video at the top of the text file
            file.write(yt.title)
            # Whitespace
            file.write("\n")
            # Writes all the data grabbed from the transcripts into a text file
            # in text form.
            for i in responses:
                file.write("{}\n".format(i))
            counter += 1
            file.close()

            # This reads data from all the generated files,
            # then converts all the data within the file to lowercase,
            # then it counts the amount of times that the word you are searching
            # for is used within each file that is generated.
            fileTest = open(filename, "r")
            read_data = fileTest.read()
            word_count = read_data.lower().count(word1)
            file.close()

        # Prints out the word count.
        print(word_count)

        for response in responses:
            text = response['text']
     
    except Exception as e:
            print(e)


#for i in responses:


