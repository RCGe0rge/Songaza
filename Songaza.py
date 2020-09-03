from youtubesearchpython import SearchVideos
from pytube import YouTube
import json
import time
import youtube_dl
from pydub import AudioSegment
import colorama
from colorama import init,Style
from termcolor import colored
import requests
import eyed3                    
from eyed3.id3 import Tag       
from mutagen.easyid3 import EasyID3
import lyricsgenius
import os

def Search_Url(search_expression,max_results=10):
    """
    On console you choose one of the option and than it returns youtube link
    """
    for x in range(3):                                                    
        yts = SearchVideos(search_expression, offset = 1, mode = "json", max_results = max_results)
        yt = json.loads(yts.result())

        if  yt["search_result"]: break

        print(colored("[!]","yellow"),"Searching one more time",end="\n") # because sometimes its broken idk

    for x in range(max_results):
        print()
        print(colored([x+1],"green"),end=" ")
        print(yt["search_result"][x]["title"])
        print(Style.DIM+"---------------------------------------------------------------------------------------------------")
        print(Style.DIM+"===================================================================================================")

    print(colored("[?]","yellow"),end=" ")
    print("Choose one of the videos: ",end=" ")
    inn = int(input())
        

    err = True    
    while err:
        if inn == 1:
            err = False
        elif inn == 2:
            err = False
        elif inn == 3:
            err = False
        elif inn == 4:
            err = False
        elif inn == 5:
            err = False
        elif inn == 6:
            err = False
        elif inn == 7:
            err = False
        elif inn == 8:
            err = False
        elif inn == 9:
            err = False
        elif inn == 10:
            err = False
        else:
            print(colored("[!]","red"),end=" ")
            print("invalid input")
            print(colored("[?]","yellow"),end=" ")
            print("Choose one of the videos:",end=" ")
            inn = int(input())

    return yt["search_result"][inn-1]["link"]

def Download(url):
    """
    Download a song from yt url and returns List of title of the song and youtube search id \n
    Saves into currently working directory\n
    return {"title","id","extension"}\n
    """
    ytd = youtube_dl.YoutubeDL(params={'format': 'bestaudio/best','outtmpl': '%(id)s.%(ext)s'})
    ytd.download([url])

    a = ytd.extract_info(url, download=False).get("title")
    b = ytd.extract_info(url, download=False).get("id")
    c = ytd.extract_info(url, download=False).get("ext")
    return [a,b,c]

def Get_Tags(artist,song,api_key="API KEY HERE"):
    """
    Returns first 3 tags from last.fm\n
    if there is less than 5 tags returns all available tags\n
    needs your api_key from last.fm\n
    \[string\] artist
    \[string\] track
    """
    tags = ""
    url1 = "http://ws.audioscrobbler.com/2.0/?method=track.gettoptags&artist=" + artist + "&track=" + song + "&api_key="+ api_key +"&format=json" 
    print(url1)
    response1 = requests.request("POST", url1 ) 
    jresponse = json.loads(response1.text)
    for x in range(3):
        try:
            tags += jresponse["toptags"]["tag"][x]["name"] + ", "
        except:
            mymax = x
            break

    return tags

def Get_Deezer(song,artist="",api_key="API KEY HERE"):
    """
    On console you choose one of the option and than it returns metadata list\n
    Return None if nothing was found\n
    Need deezer api key\n
    return [songName, artistName, album, albumCoverLink]
    """
    url = "https://deezerdevs-deezer.p.rapidapi.com/search"
    querystring = {"q":song + " " + artist}
    headers = {'x-rapidapi-host': "deezerdevs-deezer.p.rapidapi.com",'x-rapidapi-key': api_key}
    response = requests.request("GET", url, headers=headers, params=querystring)
    #print(colored("[!] test","red"))
    myjson = json.loads(response.text)

    print(colored("[!]","yellow"),"Searching for metadatas")
    pocet = 0
    try:
        
        for x in range(5):
            if not myjson["data"][x]["title"]: break
            print(Style.DIM+"---------------------------------------------------------------------------------------------------")
            print(colored([x+1],"green"),end="\n")
            print("Song name:",myjson["data"][x]["title"])
            print("Artist:",myjson["data"][x]["artist"]["name"])
            print("Album:",myjson["data"][x]["album"]["title"])
            print("Album cover:",myjson["data"][x]["album"]["cover_big"])
            print(Style.DIM+"===================================================================================================",end="\n\n")
            pocet += 1

    except:
        if pocet == 0 :print(colored("[!]","red"),"nothing was found", end="\n\n")
        if pocet != 0 :print(colored("[!]","yellow"),"thats all", end="\n\n")

    if pocet == 0 : return None
    print(colored("[?]","yellow"),"Choose one of the metadatas",end=" ")
    inn = int(input())
        

    err = True    
    while err:
        if inn == 1:
            err = False
        elif inn == 2:
            err = False
        elif inn == 3:
            err = False
        elif inn == 4:
            err = False
        elif inn == 5:
            err = False
        else:
            print(colored("[!]","red"),end=" ")
            print("invalid input")
            print(colored("[?]","yellow"),end=" ")
            print("Choose one of the videos:",end=" ")
            inn = input()

    chose = [myjson["data"][inn-1]["title"], myjson["data"][inn-1]["artist"]["name"], myjson["data"][inn-1]["album"]["title"], myjson["data"][inn-1]["album"]["cover_big"]]

    return chose



    def __init__(self,song,artist=""):
        self.song = song
        self.artist = artist
        self.Glyrics = ""

    def __enter__(self):
        genius = lyricsgenius.Genius("hF2XZy0YGBYnEEk2_p61v-HgEjmreKQPtHa2FerpVigRSeoncaop5ZXDdB-ZPhPy")
        #song = genius.search_song(song,artist)
        #lyrics = ""
        #lyrics = song.lyrics
        
        self.Glyrics = genius.search_song(self.song,self.artist).lyrics
    
    def __str__(self):
        return self.Glyrics

    def __exit__(self):
        pass

def Get_Lyrics_Genius(song,artist="",api_key="API KEY HERE"):
    """
    Gets name of song and artist and returns lyrics in string\n
    Need api key from lyrics genius
    """
    genius = lyricsgenius.Genius(api_key)
    #song = genius.search_song(song,artist)
    #lyrics = ""
    #lyrics = song.lyrics
    
    return genius.search_song(song,artist).lyrics

colorama.init(autoreset=True)

print(colored("[?]","yellow"),"What song do you searching",end=" ")
song = input()
search = song

myfile = Download(Search_Url(search))

songfile = AudioSegment.from_file(myfile[1] + "." + myfile[2])   # any file (webm,m4a, ...)
print(colored("[!]","green"),"Loaded for converting")
songfile.export(myfile[0]+".mp3", format="mp3", bitrate="160k")
print(colored("[!]","green"),"Converted and saved as " + myfile[0] + ".mp3")

os.remove(myfile[1] + "." + myfile[2])


songfile = eyed3.load(myfile[0]+".mp3")
songfile.initTag()

metadeezer = Get_Deezer(search)
# print(metadeezer) for debug
if metadeezer != None:
    songfile.tag.title = metadeezer[0]
    songfile.tag.artist = metadeezer[1]
    songfile.tag.album = metadeezer[2]
    songfile.tag.genre = Get_Tags( metadeezer[1],metadeezer[0])

    lyrics = Get_Lyrics_Genius(metadeezer[1] + " " + metadeezer[0])
    if lyrics == None:
        print(colored("[!]","red"), "Lyrics not found")
    else :
        songfile.tag.lyrics.set(lyrics)

    img_data = requests.get(metadeezer[3]).content

    with open(metadeezer[0]+"_albumcover.png", 'wb') as handler:
        handler.write(img_data)

    songfile.tag.images.set(3, open(metadeezer[0]+"_albumcover.png",'rb').read(), 'image/png')

    songfile.tag.save()
    os.remove(metadeezer[0]+"_albumcover.png")
    print(colored("[!]","green"), "Metadatas was sucessfully writed")
else:
    print(colored("[!]","red"), "No metadatas were found")

print(colored("[!]","yellow"), "Press enter to close program")
input()
