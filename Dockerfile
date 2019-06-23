FROM ubuntu:19.04
LABEL "Maintainer"="Remi Somdecoste-Lespoune <saponace@gmail.com>"

RUN apt-get update && apt-get -y install cron python3.7 python3-pip
RUN pip3 install youtube_dl


COPY yt-dl-archive-channels.py /bin

# Execute script daily at midnight
RUN touch /var/log/cron.log
RUN (crontab -l ; echo "0 0 * * * /bin/yt-dl-archive-channels.py /config/yt-dl-archive-channels.conf >> /var/log/cron.log 2>&1") | crontab

# Volumes
VOLUME ["/config/yt-dl-archive-channels.conf"]
VOLUME ["/downloads"]
VOLUME ["/data/archive.txt"]

# Call script once, and start cron scheduler
CMD /bin/yt-dl-archive-channels.py /config/yt-dl-archive-channels.conf && cron && tail -f /var/log/cron.log
