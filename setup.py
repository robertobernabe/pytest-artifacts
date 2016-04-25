import os
import sys
import io
from setuptools import setup
from setuptools import find_packages

HERE = os.path.dirname(__file__)
buildNumberFile = os.path.join(HERE, "BUILD_NUMBER")
versionFile = os.path.join(HERE, "VERSION")

# PACKAGE NAME AND VERSION
_name = "pytest-artifacts"
_base_version = "1.0.{buildNumber}"

_description = "Avira SWAT APL RS Tests"

# WILL BE USED IF BUILD LOCALLY
buildNumber = "dev"

if os.path.exists(versionFile):
    with io.open(versionFile, "r") as f:
        _version = f.read().split("=")[1]
else:
    _version = _base_version.format(buildNumber=buildNumber)


if __name__ == "__main__":

    if "--buildNumber" in sys.argv:
        i = sys.argv.index("--buildNumber") + 1
        buildNumber = sys.argv[i]
        print("Found build number '{0}'".format(buildNumber))
        print("Try to create build number file: {0}".format(buildNumberFile))
        with open(buildNumberFile, 'w') as f:
            f.write(buildNumber)
        _version = _base_version.format(buildNumber=buildNumber)
        sys.argv.remove("--buildNumber")
        sys.argv.remove(buildNumber)

        with open(versionFile, 'w') as f:
            print("Try to create version file: {0}".format(versionFile))
            f.write("version={0}".format(_version))

    setup(
        name=_name, version=_version,
        description=_description,
        author='Florian Schaeffeler',
        author_email='florian.schaeffeler@gmail.com',
        entry_points={
            "console_scripts": [],
            "pytest11": [
                'pytest-artifacts = pytest_artifacts'
            ]
        },
        packages=find_packages(),
        # include_package_dara=True, # use MANIFEST.in during install
        package_data={
            # If any package contains *.txt or *.rst files, include them:
            '': ['**/*.*'], },
        install_requires=['pytest'],
        extras_require={
            ':sys_platform == "win32"': [],
            ':"linux" in sys_platform': []
        },
        tests_require=['pytest'],
        cmdclass={}
    )
