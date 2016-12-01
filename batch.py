#!/usr/bin/python

import csv
import os
import string

# remove the start and end credits from a tv show

# how much to trim from the start, in seconds
start=int(13)

# how much to trim from the end, in seconds
end=int(14)

def format_filename(s):
    valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
    filename = ''.join(c for c in s if c in valid_chars)
    filename = filename.replace(' ','_')
    return filename

catfile = 'catlist.txt'

try:
    os.remove(catfile)
except OSError:
    pass
    
#-vf "%sscale=720:400" \
#-vf "%sscale=640:358" \
#-aspect "9:5" \
#-s 640x358 \

#deinterlace = 'yadif=3:1,mcdeint=2:1,'
#-aspect "9:5" \
#-vf "yadif=3:1,mcdeint=2:1,%sscale=624:352" \
#-vf "yadif=3:1,mcdeint=2:1,%sscale=768:576" \
#-vf "%sscale=768:576" \
#-vf "yadif=3:1,%sscale=768:576" \
#-vf "yadif=1:-1:0,%sscale=768:576" \
#-vf "%sscale=640:360" \

encode_options = '''-vcodec libx264 -profile:v baseline \
-level 1.3 \
-r 24 -partitions \
+parti4x4+parti8x8+parti4x4+partp8x8+partb8x8 \
-me_method hex -subq 7 -trellis 1 -refs 5 -deblock -1,-1 -qmin 16 \
-me_range 12 -g 250 -keyint_min 25 -sc_threshold 40 -i_qfactor 0.71 \
-weightp 0 -psy-rd 1.00,0.15 -bufsize 1500 -maxrate 896 \
-vf "%sscale=624:352" \
-aspect "16:9" \
-acodec aac -strict experimental -ac 2 -ar 44100 -ab 128k'''

with open('durations.csv', 'rb') as f:
    reader = csv.reader(f)
    data = map(tuple, reader)

f = open(catfile, 'a')

#width = '768'
#height = '576'
#aspect = '4:3'

for item in data:

    filename= item[0]
    duration = item[1]
    width = item[2]
    height = item[3]
    aspect = item[4]

    new_name = './trimmed/' + format_filename(filename) + '.mp4'

    new_dur=float(duration) - start - end
                 
    start_m,start_s = divmod(start, 60)
    start_point = "00:%02d:%02d.000" % (start_m, start_s)
    
    end_m,end_s = divmod(float(new_dur), 60)
    duration = "00:%02d:%02d.000" % (end_m, end_s)

    opts = ''
    if height == '576' and aspect == '5:4':
        opts = encode_options % 'crop=in_w:in_h-176,'
    elif height == '416': 
        opts = encode_options % 'crop=in_w:in_h-16,'
    elif height == '360' and (aspect == '16:9' or aspect == '0:1'): 
        opts = encode_options % 'crop=in_w:in_h-8,'
    elif height == '336' and aspect == '13:7': 
        opts = encode_options % 'pad=in_w:in_h+8,'
    else:
        opts = encode_options % ''

    cmd = 'ffmpeg -ss %s -t %s -i "%s" %s %s' % (start_point, duration, filename, opts, new_name)
    print cmd
    os.system(cmd)
    
    f.write("file '%s'\n" % new_name)

f.close()   

cmd = 'ffmpeg -f concat -i catlist.txt -c copy output.mp4'
print cmd
os.system(cmd)

