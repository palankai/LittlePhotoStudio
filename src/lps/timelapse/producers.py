import os

from cv2 import imread

from . import builder


class FileListProducer(builder.Producer):
    def __init__(self, files):
        self._files = files

    def generate(self):
        for filename in self._files:
            yield filename

    @classmethod
    def from_list_of_files(cls, files):
        return cls(files=files)


class MakeImageFilter(builder.Processor):
    def process(self, generator):
        for filename in generator:
            if not os.path.exists(filename):
                raise FileNotFoundError(filename)

            yield imread(filename)
