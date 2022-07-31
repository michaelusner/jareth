#!/bin/bash

echo black...
black --check jareth.py

echo flake8...
flake8 jareth.py

echo mypy...
mypy jareth.py
