import os
import glob
import zipfile
import logging
from py._path.local import LocalPath

log = logging.getLogger()


class ArtifactCollector(object):
    def __init__(self):
        self.lookupPlanGlob = []

    @staticmethod
    def _glob(searchPattern):
        return glob.glob(searchPattern)

    def add_search_pattern(self, searchPattern):
        log.debug("add searchpattern %s" % searchPattern)
        self.lookupPlanGlob.append(searchPattern)

    def collect_using_glob(self):
        for pattern in self.lookupPlanGlob:
            yield glob.glob(pattern)

    def zip_artifact_collection(self, zipFilePath, artifactsToCompress):
        _rZipFilePath = None
        with zipfile.ZipFile(str(zipFilePath), 'w', compression=zipfile.ZIP_DEFLATED) as zip:
            for artifactFilePath in artifactsToCompress:
                zip.write(
                    str(artifactFilePath),
                    os.path.basename(str(artifactFilePath)))
                _rZipFilePath = os.path.abspath(zipFilePath)
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
    logFileCollector.add_search_pattern(r"C:\ProgramData\Avira\*\LOGFILES\*.log")
    logFileCollector.add_search_pattern(r"C:\ProgramData\Avira\*\JOBS\*.avj")
    c = []
    for collection in logFileCollector.collect_using_glob():
        c.extend(collection)

    logFileCollector.zip_artifact_collection(r"c:\tmp\test.zip", c)