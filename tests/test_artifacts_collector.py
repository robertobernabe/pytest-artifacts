import pytest
from py._path.local import LocalPath
from pytest_artifacts.artifacts_collector import ArtifactCollector


@pytest.fixture
def directoryWithCollectableFiles(tmpdir):
    (LocalPath(tmpdir) / "file1.test").write("")
    (LocalPath(tmpdir) / "file2.test").write("")
    return tmpdir


class TestArtifactCollector(object):

    def test_find_files(self, directoryWithCollectableFiles):
        a = ArtifactCollector()
        a.add_search_path(directoryWithCollectableFiles)
        a.collect()

        for collection in a.collect():
            assert len(collection) == 2
