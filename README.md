sudo docker build -t yt-dl-archive-channels .
sudo docker run -v /tmp/downloads:/downloads -v /home/saponace/git-repositories/yt-dl-archive-channels/yt-dl-archive-channels.conf:/config/yt-dl-archive-channels.conf -v /home/saponace/git-repositories/yt-dl-archive-channels/archive.txt:/data/archive.txt --name=eee yt-dl-archive-channels


TODO: documentation
