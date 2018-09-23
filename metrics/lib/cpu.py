import json
import psutil
class Cpu():
    json=json.dumps({

    'cpu_percent': psutil.cpu_percent(interval=1,percpu=True),
    'cpu_count': psutil.cpu_count(),
    })