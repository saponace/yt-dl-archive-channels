#!/usr/bin/env python3

import sys
import configparser
import json
import youtube_dl
from youtube_dl.utils import DateRange


configFilePath = sys.argv[1]

configParser = configparser.ConfigParser()
configParser.read(configFilePath)

downloadFromDate = json.loads(configParser.get('yt-dl-archive-channels', 'download-from-date'))
channels = json.loads(configParser.get('yt-dl-archive-channels', 'channels'))
downloadsDir = json.loads(configParser.get('yt-dl-archive-channels', 'downloads-dir'))
archiveFile = json.loads(configParser.get('yt-dl-archive-channels', 'archive-file'))
outputPattern = downloadsDir + '/%(uploader)s/%(title)s/%(title)s-%(id)s.%(ext)s'

ydl_opts = {
    'write_all_thumbnails': True,              # Download thumbnail
    'writesubtitles': True,                    # Download subtitles
    'writeautomaticsub': True,                 # Download automatically generated subtitles
    'subtitleslangs': 'en,fr',                 # Specify subtitles languages to download
    'add_metadata': True,                      # Inject metadata in mkv video container
    'ignoreerror': True,                       # Ignore errors for videos that can't be downloaded
    'daterange': DateRange(downloadFromDate),  # Only download videos uploaded after date
    'download_archive': archiveFile,           # Write video id in file when downloaded, and do not redownload videos which IDs are in the file
    'outtmpl': outputPattern                   # Specify download path (everything in a folder which name is with video name)
}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(channels)
