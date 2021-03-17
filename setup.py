import os.path
from setuptools import setup
from setuptools import find_packages

# PACKAGE NAME AND VERSION
_name = "pytest-artifacts"
_version = "2021.3.17"


HERE = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(HERE, 'README.md'), encoding='utf-8') as f:
    _long_description = f.read()

_description = "Plugin for py.test to collect test artifacts"

if __name__ == "__main__":
    setup(
        name=_name,
        version=_version,
        description=_description,
        long_description=_long_description,
        author="Florian Schaeffeler",
        author_email="hello@fschaeffeler.de",
        entry_points={
            "console_scripts": [],
            "pytest11": ["pytest-artifacts = pytest_artifacts"],
        },
        packages=find_packages(),
        package_data={
            # If any package contains *.txt or *.rst files, include them:
            "": ["**/*.*"],
        },
        install_requires=["pytest"],
        extras_require={
            "dev": ["flake8", "black8"],
        },
        tests_require=["pytest"],
        cmdclass={},
    )
