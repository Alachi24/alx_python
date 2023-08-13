"""
you need the 'sys' & 'requests' for this task
"""

import requests
import sys

req = requests.get("https://intranet.hbtn.io")

print(req.headers)  # it will show list of things available
print(req.headers["X-Request-Id"])
