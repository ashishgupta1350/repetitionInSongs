{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import sys\n",
    "import re\n",
    "try:\n",
    "    import zopfli\n",
    "except:\n",
    "    !pip install zopfli\n",
    "from zopfli.zlib import compress\n",
    "from zlib import decompress\n",
    "import sys\n",
    "import os\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "import re\n",
    "import numpy as np\n",
    "from scipy.stats import norm\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "\n",
    "# simple song preprocessor for our hindi songs\n",
    "def preprocessSong(song):\n",
    "    listOfWords = re.split(r'[;,\\s...\\n()\\'!?.]\\s*',song)\n",
    "    processedSong = ''\n",
    "    for word in listOfWords:\n",
    "        word = word.lower()\n",
    "        if word == 'x2':\n",
    "            continue\n",
    "        if word == 'x4':\n",
    "            continue\n",
    "        processedSong+=word\n",
    "    return processedSong\n",
    "\n",
    "# gets the compressability of the songs ( bits compressed )\n",
    "def getCompressionFromSong(song):\n",
    "    compress_size = sys.getsizeof(compress(song))\n",
    "    uncomressed_song_size = sys.getsizeof(song.encode())\n",
    "    compression = (100-(compress_size/uncomressed_song_size)*100)\n",
    "    return compression\n",
    "\n",
    "# assumes songs datafield has \"songLyrics\" as one of the features\n",
    "# returns the compression ( more the repetition, more the compression)\n",
    "\n",
    "def getCompressionFromAllSongs(songsDF):\n",
    "    compressions = []\n",
    "    songs = []\n",
    "\n",
    "    breaker = 0\n",
    "    for song in list(df.songLyrics):\n",
    "        processedSong = preprocessSong(song) \n",
    "        compressions.append(getCompressionFromSong(processedSong))\n",
    "    \n",
    "    return compressions\n",
    "\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
