from bs4 import BeautifulSoup
import requests
import csv
from tqdm import tqdm

lyricsname = 'data'
lyrics_writer = csv.writer(open(lyricsname, 'w'))

logsname = 'log'
logs_writer = csv.writer(open(logsname, 'w'))

pages = 16
for page in range(13, pages+1):
    pageLink = 'https://www.lyricsmint.com/albums?page='+str(page)

    # Request to access the page
    try:
        source = requests.get(pageLink, timeout=60).text
        soup = BeautifulSoup(source, 'lxml')

    except:
        log = ["page", page, pageLink]
        logs_writer.writerow(log)
        continue
        
  	
    for movie in tqdm(soup.find_all('a', class_='h-auto w-full block text-black bg-white no-underline mt-1')):
	    movieName = movie.h3.text
	    movieLink = 'https://www.lyricsmint.com' + movie['href']
	    
	    # Request to acces the movie
	    try:
	        movieSource = requests.get(movieLink, timeout=60).text
	        movieSoup = BeautifulSoup(movieSource, 'lxml')

	    except:
	        log = ["movie", movieName, movieLink]
	        logs_writer.writerow(log)
	        continue
	        
	
	    for song in movieSoup.find_all('a', class_='h-auto w-full block text-black no-underline'):
	        
	        songName = song.h3.text
	        songLink = 'https://www.lyricsmint.com' + song['href']
	        metadata = song.find_all('span', class_='block mt-1 w-full')

	        try:
	            songSinger = metadata[0].text.split(':')[1].split('\n')[1]
	        except:
	            songSinger = ""
	        try:
	            songMusic = metadata[1].text.split(':')[1].split('\n')[1]
	        except:
	            songMusic = ""
	        try:
	            songLyricist = metadata[2].text.split(':')[1].split('\n')[1]
	        except:
	            songLyricist = ""
	        
	        # Request to access the song
	        try:
	        	songSource = requests.get(songLink, timeout=60).text
	        	songSoup = BeautifulSoup(songSource, 'lxml')

	        	englishDiv = songSoup.find('div', class_='text-base lg:text-lg pb-2')

	        	songLyrics = ""
	        	for br in englishDiv.find_all('br'):
	        		if str(br.previous_sibling) == r'<br/>':
	        			songLyrics += '\n'
	        		else:
	        			songLyrics += str(br.previous_sibling) + '\n'
	        	songLyrics += str(br.next_sibling)

	        	data = [movieName, songName, songSinger, songMusic, songLyricist, songLyrics]

	        	lyrics_writer.writerow(data)

	        except:
	            log = ["song", songName, songLink]
	            logs_writer.writerow(log)
	            continue	       	

    print("Page ", page, "Completed")