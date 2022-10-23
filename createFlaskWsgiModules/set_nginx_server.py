#!/bin/python3

from sys import argv
__DIR__ = argv[1]
SERVER_NAME = argv[2]

def createNewServerBlock(directory , server_name):
        data = "\\nserver {"
        data+="\\n     listen 80;"
        data+="\\n     server_name "+server_name+";"
        data+="\\n        location / {"
        data+="\\n             include uwsgi_params;"
        data+="\\n            uwsgi_pass unix:"+directory+"/project.sock;"
        data+="\\n       }\\n}"
        return data
print(createNewServerBlock(__DIR__ , server_name=SERVER_NAME))




