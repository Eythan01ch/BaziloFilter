import os
import sys


try:
	PATH_API_JSON = os.environ.get("PATH_API_JSON", '/Users/eythanchelly/dev_data(api)/baziloo_config.json')
except KeyError:
   print("Please set the environment variable PATH_API_JSON")
   sys.exit(1)