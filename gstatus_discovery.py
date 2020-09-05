#!/usr/bin/python3
import json
import subprocess
import sys

gluster_volume_names = []
gstatus_output = subprocess.check_output('gstatus -a -o json ', shell=True).decode()
gluster_info = json.loads(gstatus_output)
volume_list = gluster_info["data"]["volume_summary"]


nargs = len(sys.argv)

if nargs == 1:
    for volume in volume_list:
        gluster_volume_names.append({"{#VOLUME_NAME}": volume["name"]})
    print(json.dumps({'data': gluster_volume_names}))

elif nargs == 2:
    print(gluster_info["data"][sys.argv[1]])

elif nargs == 3:
    for volume in volume_list:
        if volume.get('name') and sys.argv[2] == volume["name"]:
            print(volume[sys.argv[1]])
            break
    else:
        if sys.argv[1] == "state":
            print('down')
        else:
            print()

else:
    print('Wrong arguments')

