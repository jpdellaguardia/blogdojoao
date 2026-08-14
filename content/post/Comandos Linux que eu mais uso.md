


ffmpeg -i video.mp4 -an -vf "scale=1280:-2:flags=lanczos" -c:v libx264 -profile:v high -level 4.0 -pix_fmt yuv420p -crf 22 -movflags +faststart output.mp4

python -m venv venv
source venv/bin/activate