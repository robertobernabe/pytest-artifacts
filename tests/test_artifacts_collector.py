import pytest
from py._path.local import LocalPath
from pytest_artifacts.artifacts_collector import ArtifactCollector


@pytest.fixture
def directoryWithCollectableFiles(tmpdir):
    (LocalPath(tmpdir) / "file1.test").write("")
    (LocalPath(tmpdir) / "file2.test").write("")
    return tmpdir


class TestArtifactCollector(object):

    def test_collect_files(self, directoryWithCollectableFiles):
        a = ArtifactCollector()
        a.add_search_pattern("%s/*" % directoryWithCollectableFiles)

        for collection in a.collect_using_glob():
            assert len(collection) == 2
