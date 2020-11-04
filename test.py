#!/usr/bin/env python3
# PYTHON_PREAMBLE_START_COPYRIGHT:{{{
# Christopher David Cotton (c)
# http://www.cdcotton.com
# PYTHON_PREAMBLE_END:}}}

# cd to the directory where you would like to hold the projects. It should probably be empty to avoid issues.
# Then run the following commands:
"""
git clone https://github.com/c-d-cotton/mysubmodules-testoverallfolder.git
python3 mysubmodules-testoverallfolder/test.py
"""

# The commands do the following:
# clone this project to the directory where you would like to save the multiple projects.
# Then run the script.

import os
import subprocess
import sys

# necessary to get mysubmodules project:
subprocess.call(['git', 'clone', 'https://github.com/c-d-cotton/mysubmodules.git', 'getmysubmodules'])

# add actual desired modules in project:
projects = ['mysubmodules-testoverallfolder', 'infrep', 'filelist']
if os.path.isdir('infrep'):
    subprocess.call(['git', 'pull', 'origin', 'master'])
else:
    subprocess.call(['git', 'clone', 'https://github.com/c-d-cotton/infrep.git'])

if os.path.isdir('filelist'):
    subprocess.call(['git', 'pull', 'origin', 'master'])
else:
    subprocess.call(['git', 'clone', 'https://github.com/c-d-cotton/filelist.git'])

# add submodules:
subprocess.call(['getmysubmodules/allgitmodules.py', '--deletegetsubmodules'])

for module in [module for module in os.listdir('.') if module not in projects]:
    print(module + ' appears to no longer be necessary.')
