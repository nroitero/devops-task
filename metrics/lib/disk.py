import json
import psutil
def to_gb(num_bytes):
    return str(round(float(num_bytes) / 1073741824, 2) )+'GB'

class Disk():
    def usage(part):
      disk={}
      disk['device']= part[0]
      disk['mountpoint']= part[1]
      disk['fstype']= part[2]
      disk['opts']= part[3]
      usage=psutil.disk_usage(part[1])
      disk['total']= to_gb(usage[0])
      disk['used']= to_gb(usage[1])
      disk['free']= to_gb(usage[2])
      disk['percent']= str(usage[3])+'%'


      return disk
    disk_list=[t for t in psutil.disk_partitions(all=True) ]# if (t[2] == "ext4") ]
    json=json.dumps({'disks': [list(map(usage, disk_list))]})
