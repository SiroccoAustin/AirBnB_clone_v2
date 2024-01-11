#!/usr/bin/python3
"""compress before sending the file"""

from fabric import task

@task
def do_pack():
    """create a archive file"""
    date = datetime.utcnow()
    archive_file = "versions/web_static_{}{}{}{}{}{}.tgz".format(date.year, date.month, date.day, date.hour, date.minute, date.second)

    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(archive_file)).failed is True:
        return None
    return archive_file

