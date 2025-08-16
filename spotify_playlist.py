import os 
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy 
import matplotlib.pyplot as plt
import pandas as pd
import mysql.connector
import re
import json




#Load the environment Variables
load_dotenv()
client_id=os.getenv("CLIENT_ID")
client_secret=os.getenv("CLIENT_SECRET")

sp=spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id,client_secret=client_secret))


playlist_url="https://open.spotify.com/playlist/3DX6xEolboOkN3npV2dNaW"
playlist_id=re.search(r'(?:playlist|track)/([a-zA-z0-9]+)',playlist_url).group(1) #Takes the ID only

results=sp.playlist_tracks(playlist_id)

#Connecting  the Database
conn=mysql.connector.connect(
     host="localhost",
     user="root",
     password="root",
     database="spotify_db"
)
cursor=conn.cursor()

#This below commented code is to view the json format of the playlist:

# with open("playlist.txt",'w',encoding='utf-8') as f:
#     json.dump(results,f,ensure_ascii=False,indent=4)
# print("The playlist added to the dataset")


# Cleaning the name of the Tracks
def clean_name(name,max_length=20):
     name=re.sub(r"\(.*?\)","",name)
     name=re.sub(r"\[.*?\]","",name)
     name=name.split("-")[0].strip()
     if len(name)>max_length:
          name=name[:max_length-3]+"..."
     return name.strip()

all_tracks=[]

for item in results['items']:
    track=item['track']

    try:
        artist_id=track['artists'][0]['id'] # getting the artist Id for the Genres
        artist=sp.artist(artist_id)
        genres=", ".join(artist['genres']) if  artist['genres'] else "unknown" 
        track_data=(clean_name(track['name']),
                    track['artists'][0]['name'],
                    genres,
                    track['album']['name'],
                    track['popularity'],
                    round(track['duration_ms']/60000,2))
        try:
            cursor.execute("""insert into spotify_tracks (Track,Artist,Genre,Album,Popularity,Duration_minutes) values (%s,%s,%s,%s,%s,%s)""",track_data)
        except  mysql.connector.Error as e:
             print(f'Duplicate Skipped :',{e}) 

        all_tracks.append(track_data)

    except Exception as e:
            print(f"error processing {track['name']}, error:{e}")
            continue
    
conn.commit()

print(f"Data Has been Successfully Inserted!")
cursor.close()
conn.close()




#Adding the data to csv
df=pd.DataFrame(all_tracks,columns=['Track','Artist','Genre','Album','Popularity','Duration (minutes)',])
df.to_csv("playlist_tracks_list.csv",index=False,encoding="utf-8")


#Visualizing the tracks By Popularity
df_sorted=df.sort_values(by='Popularity',ascending=False)
plt.figure(figsize=(20,10))
plt.bar(df_sorted['Track'],df_sorted['Popularity'],color="violet",edgecolor='Black')
plt.title("Track Popularity")
plt.xlabel("Track")
plt.ylabel("Popularity")
plt.xticks(rotation=45, ha='right')
plt.subplots_adjust(bottom=0.3)
plt.savefig("popularity_chart.png", dpi=300)
plt.show()