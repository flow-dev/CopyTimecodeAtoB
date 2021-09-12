import subprocess

import ffmpeg


class VideoFfmpegUtils:
    def __init__(self):
        # pip install ffmpeg-python (https://pypi.org/project/ffmpeg-python/)
        return

    def get_video_info(self, path):
        self.video_info = ffmpeg.probe(path)
        return self.video_info

    def get_timecode(self, path):
        self.get_video_info(path)
        self.timecode = self.video_info.get("streams")[2]["tags"]["timecode"]
        return self.timecode

    def get_fps(self, path):
        self.get_video_info(path)
        self.fps = self.video_info.get("streams")[0]["r_frame_rate"]
        fraction = int(self.fps[:self.fps.find('/')])
        denominator = int(self.fps[self.fps.find('/')+1:])
        self.fps_float = (fraction / denominator)
        return self.fps_float
    
    def run_ProResHQ_enc(self, in_video_path, out_video_path="output.mov", timecode="00:00:00:00"):
        fps = self.get_fps(in_video_path)
        "https://ottverse.com/ffmpeg-convert-to-apple-prores-422-4444-hq/"
        result = subprocess.call(["ffmpeg", "-r", str(fps), "-i", in_video_path,
                                 "-timecode", timecode, "-y", "-c:v", "prores_ks", "-pix_fmt", "yuv422p10le",
                                 "-bits_per_mb" ,"8000" , "-vendor", "ap10",
                                 "-r", str(fps), out_video_path])
        return result

    def run_hevc_nvenc(self, in_video_path, out_video_path="output.mp4", timecode="00:00:00:00"):
        fps = self.get_fps(in_video_path)
        "h265 GPU encoding"
        result = subprocess.call(["ffmpeg", "-r", str(fps), "-i", in_video_path,
                                 "-timecode", timecode, "-y", "-vcodec", "hevc_nvenc", "-pix_fmt", "yuv444p16le",
                                 "-crf" ,"10" , "-tag:v", "hvc1",
                                 "-r", str(fps), out_video_path])
        return result
