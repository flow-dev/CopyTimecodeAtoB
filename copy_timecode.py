import argparse
import glob
import os

from video_ffmpeg_utils import VideoFfmpegUtils


"""
Copy Timecode and enc ProResHQ or h265
Example:
    python3 copy_timecode.py \
        --video-src "PATH_TO_VIDEO_SRC" \
        --video-out "PATH_TO_VIDEO_OUT" \
        --codec h265 \
        --copy-tc \
"""

# --------------- Arguments ---------------


parser = argparse.ArgumentParser(description='Copy Timecode')

parser.add_argument('--video-src', type=str, required=True)
parser.add_argument('--video-out', type=str, default="output.mov", help="Path to video onto which to encode the output")
parser.add_argument('--codec', type=str, default='h265', choices=['proreshq', 'h265'])
parser.add_argument('--copy-tc', action='store_true', help="Used when copying timecode")

args = parser.parse_args()


# --------------- Main ---------------

if __name__ == '__main__':
    
    video_utils = VideoFfmpegUtils()

    # Get Video Info by ffprobe
    video_info = video_utils.get_video_info(args.video_src)
    print("Check video_src_info:",video_info)

    # enc ProResHQ or h265
    if args.codec == 'proreshq':
        print("run_ProResHQ_enc")
        if args.copy_tc:
            timecode = video_utils.get_timecode(args.video_src)
            print("video_src_timecode:", timecode)
            video_utils.run_ProResHQ_enc(args.video_src, args.video_out, timecode)
        else:
            video_utils.run_ProResHQ_enc(args.video_src, args.video_out)

    if args.codec == 'h265':
        print("run_hevc_nvenc")
        if args.copy_tc:
            timecode = video_utils.get_timecode(args.video_src)
            print("video_src_timecode:", timecode)
            video_utils.run_hevc_nvenc(args.video_src, args.video_out, timecode)
        else:
            video_utils.run_hevc_nvenc(args.video_src, args.video_out)

    # Check video_out_info
    video_info = video_utils.get_video_info(args.video_out)
    print("Check video_out_info:",video_info)
