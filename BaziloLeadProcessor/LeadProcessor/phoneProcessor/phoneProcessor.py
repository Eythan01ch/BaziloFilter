import re

import requests

from BaziloLeadProcessor.LeadProcessor.phoneProcessor.PhoneUtils import PhoneUtils
from BaziloLeadProcessor.LeadProcessor.phoneProcessor.phoneExceptions import (BasePhoneException,
                                                                              CouldNotAuthenticateException,
                                                                              OutOfCreditsException,
                                                                              PhoneAlreadyRegisteredException,
                                                                              PhonePatternInvalidException, )


class PhoneProcessor(PhoneUtils):
	"""
	 PhoneProcessor Working with HRL API
	"""

	def __init__(self, phone):
		super(PhoneProcessor, self).__init__(phone)
		self.phone = phone
		self.phone_pattern = re.compile("(33|0)([\d]){9}")
		self.phone_json_response = {}
		self.url = self.phone_api.url
		self.token = self.phone_api.token
		self.password = self.phone_api.password

	def is_phone_exist(self):
		"""checked if the phone already in the phones list and if so,
		 raise that the phone is already registered"""
		phones = self.get_phones()
		if self.phone in phones:
			raise PhoneAlreadyRegisteredException(self.phone)

	def is_possible_phone(self):
		"""checked if the phone pattern is exactly how It's supposed to be and if not'
		raise that the pattern is invalid"""
		if 4 < len(self.phone) < 15 and self.phone_pattern.match(self.phone):
			return True
		else:
			raise PhonePatternInvalidException(self.phone)

	def get_phone_details(self):
		"""gets phone details from HRL API"""
		phone = self.format_phone()
		full_api_url = self.url.format(self.token, self.password, phone)
		phone_response = requests.get(full_api_url)
		self.raise_amount_of_usage()

		if phone_response.status_code == 200:

			json_response = phone_response.json()
			# Checking if API worked as Expected
			error_type = json_response.get('ERR')

			if error_type:
				# Trying to see what problem caused it
				possible_errors = ['Could not authenticate', 'Invalid password', 'Invalid API key']
				if error_type in possible_errors:
					raise CouldNotAuthenticateException(self.phone)

				elif error_type == 'Insufficient credits':
					raise OutOfCreditsException(self.phone)
				else:
					raise BasePhoneException(self.phone, message=error_type)

			self.phone_json_response = json_response
			self.is_low_on_credits()
		else:
			raise BasePhoneException(self.phone, message=phone_response.status_code)
