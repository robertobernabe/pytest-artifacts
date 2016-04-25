
pytest_plugins = "pytester",  # to get testdir fixture


def test_swataplrstests_pytest_plugin_testproduct(testdir):
    result = testdir.runpytest(
        "--collect-artifacts")
    assert 'passed' in result.stdout.str()
