
from django.test import TestCase

from BaziloLeadProcessor.Tests.TestUtils import TestUtils


class TestHelper(TestUtils):
	"""Functions for helping make tests"""

	def verify_param_valid(self, r_json, param_tested):
		self.assertTrue(r_json.get(f'{param_tested}_valid'), msg=f'{param_tested} was suppose to be valid')

	def verify_param_invalid(self, r_json, param_tested):
		self.assertFalse(r_json.get(f'{param_tested}_valid'), msg=f'{param_tested} was suppose to be invalid')

	def verify_lead_invalid(self, r_json):
		self.assertFalse(r_json.get(f'valid'), msg=f'Lead was suppose to be invalid')

	def verify_lead_valid(self, r_json):
		for param in ['email', 'phone','name']:
			self.verify_param_valid(r_json, param)
		self.verify_is_double(r_json)
		self.assertTrue(r_json.get(f'valid'), msg=f'Lead was suppose to be valid')

	def verify_is_double(self, r_json):
		self.assertFalse(r_json.get('double'), msg='lead is double')

	def verify_is_not_double(self, r_json):
		self.assertTrue(r_json.get('double'), msg='lead is NOT double')

