import pytest

OPTION_COLLECT_ARTIFACTS = "--collect-artifacts"


def pytest_addoption(parser):
    """register argparse-style options and ini-style config values.
    This function must be implemented in a plugin and is called once at the beginning of a test run.
    http://pytest.org/latest/plugins.html?highlight=hooks#_pytest.hookspec.pytest_addoption
    """
    group = parser.getgroup('pytest artifacts')

    group.addoption(
        OPTION_COLLECT_ARTIFACTS,
        default=True,
        help=""
    )


def pytest_terminal_summary(terminalreporter):
    _ = "Collected the following artifacts:\n"
    terminalreporter.write_line(_)
