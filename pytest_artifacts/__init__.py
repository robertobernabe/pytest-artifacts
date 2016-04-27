import os
from py._path.local import LocalPath
from pytest_artifacts.artifacts_collector import ArtifactCollector

OPTION_COLLECT_ARTIFACTS = "--collect-artifacts"
OPTION_COMPRESS_ARTIFACTS = "--compress-artifacts"

COLLECTED_ARTIFACTS = []

def pytest_addoption(parser):
    """register argparse-style options and ini-style config values.
    This function must be implemented in a plugin and is called once at
    the beginning of a test run.
    http://pytest.org/latest/plugins.html?
    highlight=hooks#_pytest.hookspec.pytest_addoption
    """
    group = parser.getgroup('pytest artifacts')

    group.addoption(
        OPTION_COLLECT_ARTIFACTS,
        action="store",
        metavar='<path_to_search>:<filepattern_to_search_for>',
        nargs="*",
        default=None,
        help=""
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
    config._artifactsZipFilename = "pytest-artifacts.zip"
    config._artifactsOutputPath = LocalPath(os.getcwd()).join("pytest-artifacts")


def pytest_sessionfinish(session, exitstatus):
    """ whole test run finishes. """
    collectArtifactsArgs = session.config.getoption(OPTION_COLLECT_ARTIFACTS)
    compressArtifacts = session.config.getoption(OPTION_COMPRESS_ARTIFACTS)
    if collectArtifactsArgs:
        outputPath = session.config._artifactsOutputPath
        outputPath.mkdir()
        zipFileOutputPath = outputPath.join(
            session.config._artifactsZipFilename)
        a = ArtifactCollector()
        for item in collectArtifactsArgs:
            a.add_search_pattern(item)

        for collection in a.collect_using_glob():
            session.config._artifactsCollected.extend(collection)

        if compressArtifacts:
            zipFilePath = a.zip_artifact_collection(
                zipFileOutputPath, session.config._artifactsCollected)
            session.config._artifactsZipFilePath = zipFilePath
        else:
            for artifactFilePath in session.config._artifactsCollected:
                LocalPath(artifactFilePath).copy(outputPath)


def pytest_terminal_summary(terminalreporter):
    _ = "Collected the following artifacts: {0}".format(
        terminalreporter.config._artifactsCollected)
    terminalreporter.write_line(_)


def pytest_unconfigure(config):
    """ called before test process is exited.  """
    pass