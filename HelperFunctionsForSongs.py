#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys
import re
try:
    import zopfli
except:
    get_ipython().system('pip install zopfli')
from zopfli.zlib import compress
from zlib import decompress
import sys
import os
import pandas as pd
import numpy as np
import re


# simple song preprocessor for our hindi songs
def preprocessSong(song):
    listOfWords = re.split(r'[;,\s...\n()\'!?.]\s*',song)
    processedSong = ''
    for word in listOfWords:
        word = word.lower()
        if word == 'x2':
            continue
        if word == 'x4':
            continue
        processedSong+=word
    return processedSong

# gets the compressability of the songs ( bits compressed )
def getCompressionFromSong(song):
    compress_size = sys.getsizeof(compress(song))
    uncomressed_song_size = sys.getsizeof(song.encode())
    compression = (100-(compress_size/uncomressed_song_size)*100)
    return compression

# assumes songs datafield has "Lyrics" as one of the features
# returns the compression ( more the repetition, more the compression)
# some songs are not encoded in proper ascii format, hence we use average compression. These songs are <10 (<.1% of the dataset, hence reasonable assumption)
def getCompressionFromAllSongs(songsDF, breakPoint = 0):
    compressions = []
    songs = []
    if (breakPoint <= 0) or (breakPoint > len(songsDF)):
        breakPoint = len(songsDF)
    breaker = 0
    for song in list(songsDF.Lyrics):
        try:
            processedSong = preprocessSong(song) 
            compressions.append(getCompressionFromSong(processedSong))
        except:
            compressions.append(63.00) 
        breaker+=1
        if breaker == breakPoint:
            break
    return compressions
    
    


