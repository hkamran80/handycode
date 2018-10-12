# Handy Code

try:
  import requests
except ImportError:
  req = False
  
import re
import os

__help__ = {"handycode.__help__": "This help menu", "handycode.get_ip_str(string_with_ip)": "Get IP from String", 
		"handycode.get_mac_str(string_with_mac)": "Get MAC from String", 
		"handycode.download_file(url, location, filename)": "Download file using REQUESTS, filename parameter optional",
        "handycode.listdir(directory_location)": "Lists directory provided WITHOUT any files starting with \".\""}

# Regex
def get_ip_str(str_with_ip):
	return re.findall(r'[0-9]+(?:\.[0-9]+){3}', str_with_ip)

def get_mac_str(str_with_mac):
	return re.search(r"(([a-f\d]{1,2}\:){5}[a-f\d]{1,2})", str_with_mac).groups()[0]

# Requests
if req:
  def download_file(url, location, filename=""):
      local_filename = url.split('/')[-1] if filename == "" else filename

      r = requests.get(url, stream=True)
      with open(location + local_filename, 'wb') as f:
          for chunk in r.iter_content(chunk_size=1024): 
              if chunk:
                  f.write(chunk)

      return local_filename

# OS
def listdir(directory_location):
    files = []

    for f in os.listdir(directory_location):
        if f.startswith("."):
            continue
        else:
            files.append(f)

    return files
