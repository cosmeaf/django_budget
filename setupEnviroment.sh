#!/bin/bash

if [-d "env"]
then
  echo "Python virtual env exists"
else
  python3 -m venv env
fi

echo $PWD
source env/bin/activate
pip install -r requirements.txt