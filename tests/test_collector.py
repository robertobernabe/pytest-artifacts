from py._path.local import LocalPath
import pytest

from pytest_artifacts.collector import find_files


def create_subdirectories(path, amount, depth):
    path = str(path)
    for x in range(amount):
        p = LocalPath(path).join(str(depth))
        p.mkdir()
        for ext in [".a", ".b", ".c", ".d", ""]:
            _f = p.join("testfile%s" % ext)
            _f.write("")
        if not depth == 0:
            depth -= 1
            create_subdirectories(p, 1, depth)


@pytest.fixture
def testFilesSearchDirectory(tmpdir):
    for x in range(1):
        p = tmpdir.join(str(x))
        p.mkdir()
        create_subdirectories(p, 1, 50)
    return tmpdir


def test_find(testFilesSearchDirectory):
    _ = [f for f in find_files(testFilesSearchDirectory, "*.a")]
    assert len(_) == 51

    _ = [f for f in find_files(testFilesSearchDirectory, "*.b")]
    assert len(_) == 51

    _ = [f for f in find_files(testFilesSearchDirectory, "*.c")]
    assert len(_) == 51

    _ = [f for f in find_files(testFilesSearchDirectory, "*.d")]
    assert len(_) == 51

    _ = [f for f in find_files(testFilesSearchDirectory, "testfile")]
    assert len(_) == 51

    _ = [f for f in find_files(testFilesSearchDirectory, "*")]
    assert len(_) == 255

    _ = [f for f in find_files(testFilesSearchDirectory, "")]
    assert len(_) == 0
