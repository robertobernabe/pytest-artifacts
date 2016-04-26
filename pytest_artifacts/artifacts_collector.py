import os
import zipfile
import logging
from py._path.local import LocalPath


log = logging.getLogger()


class ArtifactCollector(object):
    def __init__(self):
        self.lookupPlan = []

    @staticmethod
    def _collect(
            searchPath, extensions=None, recursive=False):
        assert isinstance(searchPath, LocalPath)
        """
        :rtype: int, list
        """
        artifacts = []
        items = sorted(searchPath.listdir())
        log.debug("look up for artifacts in %s" % searchPath)
        for itemPath in items:
            if recursive and os.path.isdir(str(itemPath)):
                artifacts.extend(
                    ArtifactCollector.
                    _collect(itemPath, extensions=extensions, recursive=recursive))
            if extensions:
                if any([str(itemPath).endswith(ext) for ext in extensions]):
                    log.debug("found %s size: %s" % (itemPath, human_readable_size(itemPath.size())))
                    artifacts.append(itemPath)
            else:
                artifacts.append(itemPath)
        return artifacts

    def add_search_path(self, searchPath, extensions=None, recursive=False):
        log.debug("add path %s for searching artifacts %s" % (searchPath, extensions))
        if isinstance(searchPath, str):
            searchPath = LocalPath(searchPath)
        self.lookupPlan.append((searchPath, extensions, recursive))

    def collect(self):
        for path, extensions, recursive in self.lookupPlan:
            if path.exists:
                yield self._collect(path, extensions, recursive=recursive)
            else:
                log.warning("collect path %s doesn't exists, ignoring" % path)

    def zip_artifact_collection(self, zipFilePath):
        _rZipFilePath = None
        with zipfile.ZipFile(str(zipFilePath), 'w', compression=zipfile.ZIP_DEFLATED) as zip:
            for collection in self.collect():
                if collection:
                    for artifactFilePath in collection:
                        zip.write(artifactFilePath, os.path.basename(artifactFilePath))
                    _rZipFilePath = os.path.abspath(LocalPath(zipFilePath))
        return _rZipFilePath


def human_readable_size(size):
    """Get human readable displayable size
    :param size: size in bytes
    :type size: int or float
    :returns: formatted string which is a readable version of size
    :rtype: str
    """
    for x in ['Bytes', 'KB', 'MB', 'GB']:
        if size < 1024.0:
            return "%3.1f %s" % (size, x)
        size /= 1024.0
    return "%3.1f %s" % (size, 'TB')


if __name__ == '__main__':
    logFileCollector = ArtifactCollector()
    logFileCollector.add_search_path(LocalPath(r"c:/tmp"), ["xml"], recursive=True)
    for collection in logFileCollector.collect():
        for artifact in collection:
            print(artifact)

