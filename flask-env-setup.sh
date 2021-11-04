#!/bin/bash 

#development environment setup for FLASK

export FLASK_APP=server       #server.py
export FLASK_ENV=development  #to enable the live refresh and debugging features 

flask run