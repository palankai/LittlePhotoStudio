class Source:
    def __init__(self, files=None):
        self._files = files or []

    def __len__(self):
        return len(self._files)

    @property
    def files(self):
        return self._files

    @classmethod
    def from_list_of_files(cls, files):
        return cls(files=files)
