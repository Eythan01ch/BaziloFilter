import re

import requests

from BaziloLeadProcessor.LeadProcessor.emailProcessor.EmailUtils import EmailUtils
from BaziloLeadProcessor.LeadProcessor.emailProcessor.emailExceptions import (BaseEmailException,
                                                                              EmailAlreadyRegisteredException,
                                                                              EmailInvalidKey,
                                                                              EmailOutOfCredits,
                                                                              EmailPatternInvalidException, )


class EmailProcessor(EmailUtils):
	"""email Process needs email and optional IP address"""

	def __init__(self, email, ip):
		super(EmailProcessor, self).__init__(email)
		self.ip = ip
		self.email = email
		self.request_params = {
			"email":      self.email,
			"ip_address": self.ip,
			'api_key':    self.email_api.token
		}

		# email pattern that we use to check if the email is valid'
		self.email_pattern = re.compile("(.*)@(\w*\d*)\.[\w]{2,}")

		self.email_json_response = {}

	def is_email_exist(self):
		"""checked if the email already exist in our database'' if yes- raise email exist"""
		emails = self.get_emails()
		if self.email in emails:
			raise EmailAlreadyRegisteredException(self.email)

	def is_possible_email(self):
		"""checked if the email is exactly how to pattern supposed to be"""
		if 4 < len(self.email) < 40 and self.email_pattern.match(self.email):
			return True
		else:
			raise EmailPatternInvalidException(email=self.email)

	def get_email_details(self):
		""" PLEASE call is_possible_email is_email_exist BEFORE running this Method! """
		# if the email return status code 200, its means that the email is valid, add -1
		# to the credits and add the email
		# needs email and possibly ip address for more info
		email_response = requests.get(self.email_api.url, self.request_params)
		if email_response.status_code == 200:
			self.email_api.raise_amount_of_usage()

			email_json_response = email_response.json()

			# if the response return errors we checked which error it is,
			# out of credits or problem with the email valid
			if email_json_response.get('error'):
				amount_credits = self.get_credits()
				if amount_credits == -1:
					raise EmailInvalidKey(self.email)
				raise EmailOutOfCredits(self.email, api_credits=amount_credits)
			else:
				self.email_json_response = email_response.json()
			self.is_low_on_credits()
		else:
			raise BaseEmailException(self.email, message=f'status_code {email_response.status_code}')
