
import sys


from .base import BaseCommand


class Command(BaseCommand):

    def recurse_commands(self, command, level=0):
        handler, resolved = self.makeyfile.resolver.resolve(command)
        sys.stdout.write("%s>>> %s (%s): %s" % ("  " * level, command, handler, resolved))
        sys.stdout.write("\n")
        if handler == "sequence":
            for _command in resolved:
                self.recurse_commands(_command, level=level + 1)

    def run(self, **kwargs):
        self.recurse_commands(kwargs["command"])

    def parse_args(self, *args):
        return dict(command=args[0])
