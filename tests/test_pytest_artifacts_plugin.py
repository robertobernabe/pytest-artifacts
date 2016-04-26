
pytest_plugins = "pytester",  # to get testdir fixture


def test_pytest_artifacts_no_arguments(testdir):
    result = testdir.runpytest()
    assert 'Collected the following artifacts' in result.stdout.str()


def test_swataplrstests_pytest_plugin_testproduct(testdir):
    result = testdir.runpytest(
        "--collect-artifacts",
        "*.log")
    assert 'Collected the following artifacts' in result.stdout.str()
