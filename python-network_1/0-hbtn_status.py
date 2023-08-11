"""
imported my requests after installing it via the terminal
"""

import requests
"""
rename it to 'req'
"""
req = requests.get("https://alu-intranet.hbtn.io/status")
# when ascertaining the type, you use this code to get <class 'str'>
print(type(req.text))
# when ascertaining the text, you use this code to get 'ok'
print(req.text)
