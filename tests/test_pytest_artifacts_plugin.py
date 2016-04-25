
pytest_plugins = "pytester",  # to get testdir fixture


def test_swataplrstests_pytest_plugin_testproduct(testdir):
    result = testdir.runpytest(
        "--collect-artifacts",
        "*.log")
    assert 'Collected the following artifacts' in result.stdout.str()
