#!/bin/python3

from sys import argv
__DIR__ = argv[1]

def createProjectService(directory):
        data = "\\n[Unit]\\nDescription=uWSGI to serve  flask  PROJECT"
        data+="\\nAfter = network.target \\n[Service]"
        data+="\\nUser=root\nGroup=www-data"
        data+="\\nWorkingDirectory="+directory
        data+="\\nEnvironment="+directory+"/.venv/bin"
        data+="\\nExecStart="+directory+"/.venv/bin/uwsgi --ini project.ini"
        data+="\\n[Install]\\nWantedBy=multi-user.target"
        return data
print(createProjectService(__DIR__))

    