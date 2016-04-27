import os
import glob
import zipfile


class ArtifactCollector(object):
    def __init__(self):
        self.lookupPlanGlob = []

    @staticmethod
    def _glob(searchPattern):
        return glob.glob(searchPattern)

    def add_search_pattern(self, searchPattern):
        self.lookupPlanGlob.append(searchPattern)

    def collect_using_glob(self):
        for pattern in self.lookupPlanGlob:
            yield glob.glob(pattern)

    def zip_artifact_collection(self, zipFilePath, artifactsToCompress):
        with zipfile.ZipFile(str(zipFilePath), 'w', compression=zipfile.ZIP_DEFLATED) as zip:
            for artifactFilePath in artifactsToCompress:
                zip.write(
                    str(artifactFilePath),
                    os.path.basename(str(artifactFilePath)))


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
    pass
