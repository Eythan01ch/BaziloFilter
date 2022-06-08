
#
import json
from copy import copy

from BaziloLeadProcessor.Tests.TestUtils import TestUtils
from BaziloLeadProcessor.api_config import PATH_API_JSON

with open(PATH_API_JSON, 'r') as json_file:
	json_object = json.load(json_file)
	hlr_password_path = json_object['hlr']['password']
	hlr_password = copy(hlr_password_path)
	hlr_password_path = hlr_password_path[0:-1]

	hlr_password_path = hlr_password_path[0:-1]
	print(hlr_password)
	print(json_object)


class TestSMSSender(TestUtils):
	def setUp(self):
		self.setup_init()
		with open(PATH_API_JSON, 'r') as json_keys:
			json_object = json.load(json_keys)
			hrl_password = copy(json_object['hrl']['password'])
			json_object['hrl']['password'] = json_object['hrl']['password'][0:-1]
			print(hrl_password)
			print(json_object)






