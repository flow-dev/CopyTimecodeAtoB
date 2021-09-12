# CopyTimecodeAtoB
Copy the time code of A file to B file and write it out with ffmpeg

## Run Test Code

1. Install dependencies
```sh
pip install -r requirements.txt
```

2. run
```python
python3 copy_timecode.py \
    --video-src "PATH_TO_VIDEO_SRC" \
    --video-out "PATH_TO_VIDEO_OUT" \
    --codec h265 \
    --copy-tc \
```

