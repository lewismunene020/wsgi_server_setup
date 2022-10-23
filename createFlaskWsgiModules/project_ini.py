#!/bin/python3

import os
from sys import argv 
__DIR__ = argv[1]

def  makeProjectIni(directory):
    data ="[uwsgi]\\nmodule = wsgi:app\\nmaster = true\\n"
    data+="processes = 5\\n"
    data+="socket =  project.sock \\nchmod-socket = 660 \\n"
    data+="vacuum = true\\n"
    data+="die-on-term = true\\n"
    data+="logto = "+directory+ "/project.log"
    return data

print(makeProjectIni(argv[1]))

    