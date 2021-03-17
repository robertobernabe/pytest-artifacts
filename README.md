# pytest-artifacts
[![Project Status: WIP - Initial development is in progress, but there has not yet been a stable, usable release suitable for the public.](http://www.repostatus.org/badges/latest/wip.svg)](http://www.repostatus.org/#wip)
[![Python package](https://github.com/robertobernabe/pytest-artifacts/actions/workflows/python-package.yml/badge.svg)](https://github.com/robertobernabe/pytest-artifacts/actions/workflows/python-package.yml)

pytest-artifacts is a plugin for [py.test](https://pytest.org) which is able to collect artifacts after the testrun.


## Requirements:

You will need the following prerequisites in order to use pytest-artifacts:

- Python 3.x


## Usage:

    pytest tests\
    
This command line will run tests located in `tests\` and collect all files with the extension `.log` after the testrun finished.
  
 
     
    ===================================================================== test session starts ====================================================================== 
    platform win32 -- Python 3.7.9, pytest-6.2.2, py-1.10.0, pluggy-0.13.1
    rootdir: C:\Users\florian.schaeffeler\git\robertobernabe\pytest-artifacts
    plugins: artifacts-2021.3.17
    collected 6 items                                                                                                                                                

    tests\test_artifacts_collector.py .                                                                                                                       [ 16%] 
    tests\test_collector.py .                                                                                                                                 [ 33%] 
    tests\test_pytest_artifacts_plugin.py ....                                                                                                                [100%] 

    Collected the following artifacts: ['requirements.txt']
    Copied artifacts to C:\Users\florian.schaeffeler\git\robertobernabe\pytest-artifacts\pytest-artifacts
    ====================================================================== 6 passed in 0.45s ======================================================================= 


You are also able to compress the found artifacts with `--compress-artifacts`
        
    

    ============================= test session starts =============================
    platform win32 -- Python 3.4.1, pytest-2.9.1, py-1.4.31, pluggy-0.3.1
    rootdir: C:\, inifile:
    plugins: artifacts-1.0.dev0
    collected 0 items
    
    Collected the following artifacts: ['C:\\ProgramData\\Dropbox\\Update\\Log\\DropboxUpdate.log-2016-04-27-10-17-00-081-9024-finished', 'C:\\ProgramData\\Dropbox\\Update\\Log\\DropboxUpdate.log-2016-04-27-11-17-00-064-11620-finished']
    Compressed artifacts to C:\Users\User\tmp\pytest-artifacts\pytest-artifacts.zip
    ======================== no tests ran in 0.11 seconds =========================
