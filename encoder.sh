#!/bin/sh  

if [ -z $2 ]; then
	echo "Syntax: $0 input output"
	exit 1
fi    
          
#TESTING="-y -ss 00:00:40 -t 00:00:15"
TESTING=""

# baseline level 1.3 is for 1st generation iPod Touch compatibility
# 25 fps
# 720x400
# optimizations for kids cartoons

#EXTRA_OPTIONS='-vcodec libx264 -profile:v baseline -level 1.3 -vf crop=in_w:in_h-176,scale=720:400 -r 25 -partitions +parti4x4+parti8x8+parti4x4+partp8x8+partb8x8 -me_method hex -subq 7 -trellis 1 -refs 5 -deblock -1,-1  -qmin 16 -me_range 12 -g 250 -keyint_min 25 -sc_threshold 40 -i_qfactor 0.71 -weightp 0 -psy-rd 1.00,0.15 -bufsize 1500 -maxrate 896 -acodec aac -strict experimental -ac 2 -ar 44100 -ab 128k'

# widescreen for iPad, no crop
#EXTRA_OPTIONS='-vcodec libx264 -profile:v baseline -level 1.3 -vf scale=640:360 -aspect 16:9 -r 25 -partitions +parti4x4+parti8x8+parti4x4+partp8x8+partb8x8 -me_method hex -subq 7 -trellis 1 -refs 5 -deblock -1,-1  -qmin 16 -me_range 12 -g 250 -keyint_min 25 -sc_threshold 40 -i_qfactor 0.71 -weightp 0 -psy-rd 1.00,0.15 -bufsize 1500 -maxrate 896 -acodec aac -strict experimental -ac 2 -ar 44100 -ab 128k'


#very wide film for iphone 6
EXTRA_OPTIONS='-vcodec libx264 -profile:v baseline -level 3.0 -vf scale=720:304
-aspect 240:112 -r 23.976 -partitions +parti4x4+parti8x8+parti4x4+partp8x8+partb8x8 -me_method hex -subq 7 -trellis 1 -refs 5 -deblock -1,-1  -qmin 16 -me_range 12 -g 250 -keyint_min 25 -sc_threshold 40 -i_qfactor 0.71 -weightp 0 -psy-rd 1.00,0.15 -bufsize 1500 -maxrate 896 -acodec aac -strict experimental -ac 2 -ar 44100 -ab 128k'

ffmpeg -i "$1" $TESTING $EXTRA_OPTIONS "$2" 
