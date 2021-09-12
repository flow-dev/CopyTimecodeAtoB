# CopyTimecodeAtoB
Copy the timecode of file A to file B and export it in h265 or ProResHQ with ffmpeg. (Bit depth is 10bit).

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
    --codec h265 \  #h265 or proreshq
    --copy-tc \
```

