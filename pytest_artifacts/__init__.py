import os
import pytest
import _pytest
from py._path.local import LocalPath
from pytest_artifacts.artifacts_collector import ArtifactCollector

OPTION_COLLECT_ARTIFACTS = "--collect-artifacts"



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
        default=None,
        help=""
    )


def pytest_sessionfinish(session, exitstatus):
    """ whole test run finishes. """
    collectArtifactsArgs = session.config.getoption(OPTION_COLLECT_ARTIFACTS)
    if collectArtifactsArgs:
        outputPath = LocalPath(os.getcwd()).join("pytest_artifacts")
        outputPath.mkdir()
        zipFileOutputPath = outputPath.join("artifacts.zip")
        a = ArtifactCollector()
        for ext in collectArtifactsArgs.split(";"):
            a.add_search_path(os.getcwd(), ext, recursive=True)
        collectedArtifacts = [item for item in a.collect()]
        a.zip_artifact_collection(zipFileOutputPath)


def pytest_terminal_summary(terminalreporter):
    _ = "Collected the following artifacts:\n"
    terminalreporter.write_line(_)
