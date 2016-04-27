from setuptools import setup
from setuptools import find_packages

# PACKAGE NAME AND VERSION
_name = "pytest-artifacts"
_version = "0.1.0"

_description = "Plugin for py.test to collect test artifacts"

if __name__ == "__main__":
    setup(
        name=_name,
        version=_version,
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
