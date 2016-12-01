#!/bin/bash

outfile="durations.csv"

if [ -f $outfile ];
then
   rm $outfile
fi

#for f in *.avi
#for f in {*.avi,*.mp4,*.m4v}
for f in {*.avi,*.mp4,*.m4v}
do
  echo "getting duration for $f"
  duration="$(ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 "$f")"
  width="$(ffprobe -v error -show_entries stream=width -of default=noprint_wrappers=1:nokey=1 "$f")"
  height="$(ffprobe -v error -show_entries stream=height -of default=noprint_wrappers=1:nokey=1 "$f")"
  aspect="$(ffprobe -v error -show_entries stream=display_aspect_ratio -of default=noprint_wrappers=1:nokey=1 "$f")"
  
  echo "\"$f\"","$duration","$width","$height","$aspect" >> ${outfile}
  #echo "\"$f\"","$duration" >> ${outfile}
done

