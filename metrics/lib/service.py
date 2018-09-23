import json
import psutil
class Service():
  procs = {p.pid: p.info for p in psutil.process_iter(attrs=['pid', 'name', 'username','exe','cmdline','cpu_percent'])}
  json=json.dumps({'services': procs  })

