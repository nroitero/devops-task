import json
import re

def rx_tx_dump():
  networks={}
  with open('/proc_host/net/dev') as f:

    for line in f.readlines():
      if ":" in line:
        data=line.split()
        networks[data[0]]={}
        networks[data[0]]["Receive"]=[int(x) for x in data[1:9]]
        networks[data[0]]["Transmit"]=[int(x) for x in data[9:]]


  return networks


class Network():


  json=json.dumps({

  'networks':rx_tx_dump()

  })