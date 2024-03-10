#!/usr/bin/python3
"""compress before sending the file"""
from datetime import datetime
from fabric.api import local
from os.path import isdir

def do_pack():
    """create a archive file"""
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
        file_name = "versions/web_static_{}.tgz".format(date)
        local("tar -czvf {} web_static".format(file_name))
        return file_name
    except:
        return None
