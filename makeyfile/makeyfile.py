
from . import registry
from .discovery import Discovery
from .loader import Loader
from .resolver import Resolver


class Makeyfile(object):

    def __init__(self):
        self.registry = registry
        for runner in self.registry["runner"]:
            if isinstance(self.registry["runner"][runner], type):
                self.registry[
                    "runner"][runner] = self.registry["runner"][runner](self)
        self.discovery = Discovery()
        self.loader = Loader()
        self.filepath = self.discovery.find()
        self.makey = self.loader.load(self.filepath)
        self.resolver = Resolver(self)
