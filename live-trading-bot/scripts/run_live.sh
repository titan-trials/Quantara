#!/bin/bash

# Activate the virtual environment
source venv/bin/activate

# Run the main trading bot script
python src/main.py

# Deactivate the virtual environment after execution
deactivate