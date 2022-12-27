import os
from typing import Iterator
from pathlib import Path
from sys import _getframe


class Config:

    def __init__(self, file: str = ""):
        self.file = Path(file)
        self.read()
        # r = dotenv_values('.env')
        # [setattr(self, key, value) for key, value in dotenv_values('.env').items()]

    def __getattr__(self, item):
        attr = os.environ.get(item.upper())
        setattr(self, item, attr) if attr is not None else ...
        return attr

    def read(self):
        res = self.find_config()
        print(self.file, res)
        # with open(self.file, 'r') as fh:
        #     print(fh.readlines())

    def find_config(self):
        filename = self.file.name or ".env"
        print(filename)
        current_file = __file__
        frame = _getframe()
        print(frame.f_code)
        while frame.f_code.co_filename == current_file:
            if frame.f_back is None:
                return False
            frame = frame.f_back
        frame_filename = frame.f_code.co_filename
        path = os.path.dirname(os.path.abspath(frame_filename))

        for dirname in self.walk_to_root(path):
            check_path = os.path.join(dirname, filename)
            print(check_path)
            if os.path.isfile(check_path):
                self.file = check_path
                return True
        return False

    def set_attributes(self, **kwargs):
        """
        Add attributes to the config object
        Args:
            **kwargs: Set attributes as keyword arguments

        Returns:

        """
        [setattr(self, i, j) for i, j in kwargs.items()]

    @staticmethod
    def walk_to_root(path: str) -> Iterator[str]:

        if not os.path.exists(path):
            raise IOError('Starting path not found')

        if os.path.isfile(path):
            path = os.path.dirname(path)

        last_dir = None
        current_dir = os.path.abspath(path)
        while last_dir != current_dir:
            yield current_dir
            parent_dir = os.path.abspath(os.path.join(current_dir, os.path.pardir))
            last_dir, current_dir = current_dir, parent_dir

env = Config()

# print(env.man)
# print(env.MAN)
# print(env.lop)
# print(env.__dict__)


