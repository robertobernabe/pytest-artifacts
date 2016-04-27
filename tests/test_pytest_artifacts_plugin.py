import pytest
import sys

pytest_plugins = "pytester",  # to get testdir fixture

runsOnlyOnWindows = pytest.mark.skipif(
    not (sys.platform == 'win32'), reason="Runs only on Windows")
runsOnlyOnLinux = pytest.mark.skipif(
    not (sys.platform == 'linux'), reason="Runs only on Linux")


def test_pytest_artifacts_no_arguments(testdir):
    result = testdir.runpytest()
    assert 'Collected the following artifacts' in result.stdout.str()


def test_pytest_artifacts_collect_in_cwd(testdir):
    f = testdir.tmpdir.join("test.log")
    f.write("content")
    f = testdir.tmpdir.join("test.md5")
    f.write("content")

    result = testdir.runpytest(
        "--collect-artifacts",
        "*.log",
        "*.md5")
    assert 'Collected the following artifacts' in result.stdout.str()
    assert "test.log" in result.stdout.str()
    assert "test.md5" in result.stdout.str()


def test_pytest_artifacts_collect_in_custom_path(testdir):
    f = testdir.tmpdir.join("test.log")
    f.write("content")
    f = testdir.tmpdir.join("test.md5")
    f.write("content")

    result = testdir.runpytest(
        "--collect-artifacts",
        r"%s\*.log" % str(testdir.tmpdir),
        r"%s\*.md5" % str(testdir.tmpdir))
    assert 'Collected the following artifacts' in result.stdout.str()
    assert "test.log" in result.stdout.str()
    assert "test.md5" in result.stdout.str()

