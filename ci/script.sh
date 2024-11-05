#!/bin/bash

# Make sure the tests will FAIL if it has to
set -euxo pipefail

# Set up your Python environment
pip install virtualenv
virtualenv -p python3.12 venv
source venv/bin/activate

# You can install your deps, if any
pip install --upgrade pip
pip install numpy

# Run your tests
python main.py