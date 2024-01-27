#!/bin/bash
# Tim H 2023

# create a virtual env, install specific version of libraries used in lab
# attempt to load the existing env if it exists
# if it does not exist, then create it and activate it
source ./.venv/bin/activate || python3 -m venv ./.venv && source ./.venv/bin/activate

# upgrade pip
pip3 install --quiet --upgrade pip

# install dependencies. ipykernel is required.
pip install --quiet -r requirements.txt

python3 main.py
