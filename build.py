import os
import sys
import platform
from conan.packager import ConanMultiPackager


def system(command):
    retcode = os.system(command)
    if retcode != 0:
        raise Exception("Error while executing:\n\t %s" % command)


if __name__ == "__main__":
    builder = ConanMultiPackager(username="albertosm27")
    builder.run()
