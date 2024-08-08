#!/bin/bash

# Encode video at 320x180 resolution with 200kbps bitrate
ffmpeg -y -i video_6m.mp4 -c:v libx264 -r 30 -x264opts 'keyint=48:min-keyint=48:no-scenecut' -vf scale=320:180 -b:v 200k -maxrate 200k -movflags faststart -bufsize 400k -profile:v main -preset fast -an "video_180p_200k.mp4"

# Encode video at 320x180 resolution with 400kbps bitrate
ffmpeg -y -i video_6m.mp4 -c:v libx264 -r 30 -x264opts 'keyint=48:min-keyint=48:no-scenecut' -vf scale=320:180 -b:v 400k -maxrate 400k -movflags faststart -bufsize 800k -profile:v main -preset fast -an "video_180p_400k.mp4"

# Encode video at 480x270 resolution with 600kbps bitrate
ffmpeg -y -i video_6m.mp4 -c:v libx264 -r 30 -x264opts 'keyint=48:min-keyint=48:no-scenecut' -vf scale=480:270 -b:v 600k -maxrate 600k -movflags faststart -bufsize 1200k -profile:v main -preset fast -an "video_270p_600k.mp4"

# Encode video at 640x360 resolution with 800kbps bitrate
ffmpeg -y -i video_6m.mp4 -c:v libx264 -r 30 -x264opts 'keyint=48:min-keyint=48:no-scenecut' -vf scale=640:360 -b:v 800k -maxrate 800k -movflags faststart -bufsize 1600k -profile:v main -preset fast -an "video_360p_800k.mp4"

# Encode video at 640x360 resolution with 1000kbps bitrate
ffmpeg -y -i video_6m.mp4 -c:v libx264 -r 30 -x264opts 'keyint=48:min-keyint=48:no-scenecut' -vf scale=640:360 -b:v 1000k -maxrate 1000k -movflags faststart -bufsize 2000k -profile:v main -preset fast -an "video_360p_1000k.mp4"

# Encode video at 768x432 resolution with 1500kbps bitrate
ffmpeg -y -i video_6m.mp4 -c:v libx264 -r 30 -x264opts 'keyint=48:min-keyint=48:no-scenecut' -vf scale=768:432 -b:v 1500k -maxrate 1500k -movflags faststart -bufsize 3000k -profile:v main -preset fast -an "video_432p_1500k.mp4"

# Encode video at 1024x576 resolution with 2500kbps bitrate
ffmpeg -y -i video_6m.mp4 -c:v libx264 -r 30 -x264opts 'keyint=48:min-keyint=48:no-scenecut' -vf scale=1024:576 -b:v 2500k -maxrate 2500k -movflags faststart -bufsize 5000k -profile:v main -preset fast -an "video_576p_2500k.mp4"

# Encode video at 1280x720 resolution with 4000kbps bitrate
ffmpeg -y -i video_6m.mp4 -c:v libx264 -r 30 -x264opts 'keyint=48:min-keyint=48:no-scenecut' -vf scale=1280:720 -b:v 4000k -maxrate 4000k -movflags faststart -bufsize 8000k -profile:v main -preset fast -an "video_720p_4000k.mp4"

#Generate mpd file
MP4Box -dash 4000 -rap -segment-name 'segment_$RepresentationID$_' -fps 30 \
video_180p_200k.mp4#video:id=180p_2000k \
video_180p_400k.mp4#video:id=180p_4000k \
video_270p_600k.mp4#video:id=270p_600k \
video_360p_800k.mp4#video:id=360p_800k \
video_360p_1000k.mp4#video:id=360p_1000k \
video_432p_1500k.mp4#video:id=432p_1500k \
video_576p_2500k.mp4#video:id=576p_2500k \
video_720p_4000k.mp4#video:id=720p_4000k \
-out dash/playlist.mpd
