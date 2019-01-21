import logging


from cv2 import resize


class SimpleResize:
    def __init__(self, width, height):
        self._width = width
        self._height = height
        self._log = logging.getLogger("timelapse.simpleresize")

    def process(self, generator):
        for image in generator:
            yield resize(image, (self._width, self._height))
