import os
from py._path.local import LocalPath
from pytest_artifacts.artifacts_collector import ArtifactCollector

OPTION_COLLECT_ARTIFACTS = "--collect-artifacts"
OPTION_COMPRESS_ARTIFACTS = "--compress-artifacts"

PYTEST_ARTIFACTS = "pytest-artifacts"
PYTEST_ARTIFACTS_ZIP_FILENAME = "%s.zip" % PYTEST_ARTIFACTS


def pytest_addoption(parser):
    """register argparse-style options and ini-style config values.
    This function must be implemented in a plugin and is called once at
    the beginning of a test run.
    http://pytest.org/latest/plugins.html?
    highlight=hooks#_pytest.hookspec.pytest_addoption
    """
    group = parser.getgroup("artifacts")

    group.addoption(
        OPTION_COLLECT_ARTIFACTS,
        action="store",
        metavar='pattern',
        nargs="*",
        default=None,
        help="Search for artifacts /path/to/dir/file*pattern.ext"
    )

    group.addoption(
        OPTION_COMPRESS_ARTIFACTS,
        action="store_true",
        default=False,
        help="Compress collected artifacts with zip."
    )


def pytest_configure(config):
    """ called after command line options have been parsed
    and all plugins and initial conftest files been loaded.
    This hook is called for every plugin.
    """
    config._artifactsCollected = []
    config._artifactsZipFilename = PYTEST_ARTIFACTS_ZIP_FILENAME
    config._artifactsOutputPath = LocalPath(os.getcwd()).join(PYTEST_ARTIFACTS)
    config._artifactsZipFileOutputPath = config._artifactsOutputPath.join(
        PYTEST_ARTIFACTS_ZIP_FILENAME)


def pytest_sessionfinish(session, exitstatus):
    """ whole test run finishes. """
    collectArtifactsArgs = session.config.getoption(OPTION_COLLECT_ARTIFACTS)
    compressArtifacts = session.config.getoption(OPTION_COMPRESS_ARTIFACTS)
    if collectArtifactsArgs:
        a = ArtifactCollector()
        if session.config._artifactsOutputPath.exists:
            try:
                session.config._artifactsOutputPath.remove(ignore_errors=True)
            except:
                pass
        session.config._artifactsOutputPath.mkdir()

        for item in collectArtifactsArgs:
            a.add_search_pattern(item)

        for collection in a.collect_using_glob():
            session.config._artifactsCollected.extend(collection)

        if compressArtifacts:
            if len(session.config._artifactsCollected) > 0:
                a.zip_artifact_collection(
                    session.config._artifactsZipFileOutputPath,
                    session.config._artifactsCollected)
        else:
            for artifactFilePath in session.config._artifactsCollected:
                LocalPath(artifactFilePath).copy(
                    session.config._artifactsOutputPath)


def pytest_terminal_summary(terminalreporter):
    _ = "Collected the following artifacts: {0}".format(
        terminalreporter.config._artifactsCollected)

    if terminalreporter.config._artifactsZipFileOutputPath.exists():
        _ = "{0}\nCompressed artifacts to {1}".format(
            _, terminalreporter.config._artifactsZipFileOutputPath)
    else:
        if len(terminalreporter.config._artifactsCollected) > 0:
            _ = "{0}\nCopied artifacts to {1}".format(
                _, terminalreporter.config._artifactsOutputPath)

    terminalreporter.write_line(_)


def pytest_unconfigure(config):
    """ called before test process is exited.  """
    pass
