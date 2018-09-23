import json
import psutil
def to_gb(num_bytes):
    return str(round(float(num_bytes) / 1073741824, 2) )+'GB'

class Ram():
  memory = psutil.virtual_memory()
  swap = psutil.swap_memory()
  json=json.dumps({
    'memory': {
      'total':  to_gb(memory.total),
      'available':  to_gb(memory.available),
      'percent': str(memory.percent)+'%',
      'used':  to_gb(memory.used),
      'free': to_gb(memory.free)
    },'swap': {
      'total':  to_gb(swap.total),
      'percent': str(swap.percent)+'%',
      'used':  to_gb(swap.used),
      'free': to_gb(swap.free)
    }

    })