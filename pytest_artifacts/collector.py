import os

import fnmatch
import logging
from py._path.local import LocalPath

log = logging.getLogger()


def find_files(directory, pattern):
    """Searching for pattern in specific directory.
    Returns an list with found files and directories according to
    given pattern.
    :param dirPathToSearch:
    :param pattern: No tilde expansion is done, but *, ?, and
    character ranges expressed with [] will be correctly matched.
    :return: yields a file path
    """
    directory = str(directory)
    log.info("Searching for %s in %s", pattern, directory)
    for root, dirs, files in os.walk(directory):
        for basename in files:
            if fnmatch.fnmatch(basename, pattern):
                filePath = os.path.join(root, basename)
                log.info("found %s", filePath)
                yield LocalPath(filePath)


if __name__ == '__main__':
    import sys
    log.addHandler(logging.StreamHandler(stream=sys.stdout))
    log.setLevel(logging.DEBUG)
    for filePath in find_files(os.path.expanduser("~"), r'*.zip'):
        print(filePath)
        assert filePath.isfile()
