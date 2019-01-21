import os
import logging

from cv2 import VideoWriter, VideoWriter_fourcc

from . import builder

log = logging.getLogger("timelapse.video")


class VideoMaker(builder.Consumer):
    def __init__(self, filename, width, height, fps=24, is_color=True):
        self._filename = filename
        self._width = width
        self._height = height
        self._fps = fps
        self._is_color = is_color

    def consume(self, generator):
        format = "XVID"
        fourcc = VideoWriter_fourcc(*format)
        vid = VideoWriter(
            self._filename,
            fourcc,
            float(self._fps),
            (self._width, self._height),
            self._is_color,
        )
        log.info("Video creation started...")
        for image in generator:
            vid.write(image)
            log.info("Image added...")
        vid.release()
        log.info("Video released.")
