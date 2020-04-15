#!/bin/bash
# we want to exit on errors
set -e

VIRTUALENV_BIN=`which virtualenv-2.7 || which virtualenv`
"$VIRTUALENV_BIN" --python=/usr/local/bin/python2.7 .

# Let's enter the virtualenv
. bin/activate
./bin/pip install -r requirements.txt
