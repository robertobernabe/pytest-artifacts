# pytest-artifacts
[![Project Status: WIP - Initial development is in progress, but there has not yet been a stable, usable release suitable for the public.](http://www.repostatus.org/badges/latest/wip.svg)](http://www.repostatus.org/#wip)
[![Build Status](https://travis-ci.org/robertobernabe/pytest-artifacts.svg?branch=master)](https://travis-ci.org/robertobernabe/pytest-artifacts)
[![Build status](https://ci.appveyor.com/api/projects/status/u39nq236gl0xl9pf?svg=true)](https://ci.appveyor.com/project/robertobernabe/pytest-artifacts)

pytest-artifacts is a plugin for [py.test](https://pytest.org) which is able to collect artifacts after the testrun.


## Requirements:

You will need the following prerequisites in order to use pytest-artifacts:

- Python 2.7, 3.4 or 3.5



## Installation:
    
    pip install pytest-artifacts


## Usage:

    py.test --collect-artifacts C:\ProgramData\Dropbox\Update\Log\*.log* tests\
    
This command line will run tests located in `tests\` and collect all files with the extension `.log` after the testrun finished.
  
 
     
    ============================= test session starts =============================
    platform win32 -- Python 3.4.1, pytest-2.9.1, py-1.4.31, pluggy-0.3.1
    rootdir: C:\, inifile:
    plugins: artifacts-1.0.dev0
    collected 0 items
    
    Collected the following artifacts: ['C:\\ProgramData\\Dropbox\\Update\\Log\\DropboxUpdate.log-2016-04-27-10-17-00-081-9024-finished', 'C:\\ProgramData\\Dropbox\\Update\\Log\\DropboxUpdate.log-2016-04-27-11-17-00-064-11620-finished']
    Copied artifacts to C:\Users\User\tmp\pytest-artifacts\pytest-artifacts
    ======================== no tests ran in 0.07 seconds =========================


You are also able to compress the found artifacts with `--compress-artifacts`
        
    

    ============================= test session starts =============================
    platform win32 -- Python 3.4.1, pytest-2.9.1, py-1.4.31, pluggy-0.3.1
    rootdir: C:\, inifile:
    plugins: artifacts-1.0.dev0
    collected 0 items
    
    Collected the following artifacts: ['C:\\ProgramData\\Dropbox\\Update\\Log\\DropboxUpdate.log-2016-04-27-10-17-00-081-9024-finished', 'C:\\ProgramData\\Dropbox\\Update\\Log\\DropboxUpdate.log-2016-04-27-11-17-00-064-11620-finished']
    Compressed artifacts to C:\Users\User\tmp\pytest-artifacts\pytest-artifacts\pytest-artifacts.zip
    ======================== no tests ran in 0.11 seconds =========================