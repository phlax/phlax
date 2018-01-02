
import json
import sys

from .base import BaseCommand


class Command(BaseCommand):

    def parse_args(self, *args):
        _args = dict(handler=args[0])
        if len(args) > 1:
            _args['command'] = args[1]
        return _args

    def run(self, **kwargs):
        if kwargs.get("command"):
            sys.stdout.write(
                json.dumps(
                    self.makeyfile.makey[
                        kwargs["handler"]][kwargs["command"]]))
        else:
            sys.stdout.write(
                json.dumps(
                    self.makeyfile.makey[kwargs["handler"]]))
        sys.stdout.write("\n")
