from BaziloLeadProcessor.LeadProcessor.phoneProcessor.phoneExceptions import (BasePhoneException,
                                                                              CouldNotAuthenticateException,
                                                                              OutOfCreditsException,
                                                                              PhoneAlreadyRegisteredException,
                                                                              PhonePatternInvalidException,
                                                                              SoonOutOfCreditsException, )
from BaziloLeadProcessor.LeadProcessor.phoneProcessor.phoneProcessor import PhoneProcessor
from BaziloLeadProcessor.LeadProcessor.utils.sms_sender import SmsSender


class PhoneHandler(PhoneProcessor):
	def __init__(self, phone):
		super(PhoneHandler, self).__init__(phone)
		self.phone_data_dict = {}
		self.phone = phone

		self.double = None
		self.valid = None
		self.phone_status = None
		self.sms_handler = SmsSender()
		self.is_phone_pattern_valid_method_called = None
		self.is_double_phone_method_called = None
		self.is_phone_valid_method_called = None

	def is_double_phone(self):
		try:
			self.is_phone_exist()
		except PhoneAlreadyRegisteredException as error:
			self.double = True
			self.valid = False
			self.phone_status = f'{error}'
		finally:
			self.is_double_phone_method_called = True
			self.update_data_of_class()

	def is_phone_pattern_valid(self):
		try:
			self.is_possible_phone()
		except PhonePatternInvalidException as error:
			self.valid = False
			self.phone_status = f'{error}'
		finally:
			self.is_phone_pattern_valid_method_called = True
			self.update_data_of_class()

	def is_phone_valid(self):
		self.is_phone_valid_method_called = True
		"""will run only if all the above called before"""
		if not self.is_phone_pattern_valid_method_called:
			self.is_phone_pattern_valid()
		if not self.is_double_phone_method_called:
			self.is_double_phone()

		if self.valid == False:
			return False

		try:
			self.get_phone_details()

			if self.phone_json_response.get('Status'):
				self.phone_status = self.phone_json_response.get('Status')
				self.valid = self.phone_json_response.get('Status') == 'Valid'
			else:
				self.phone_status = self.phone_json_response.get('ERR')

		except SoonOutOfCreditsException as error:
			self.phone_status = f'{error}'
			self.sms_handler.send_sms(error)

		except (OutOfCreditsException, CouldNotAuthenticateException) as error:
			self.valid = True
			self.phone_status = f'{error}'
			self.sms_handler.send_sms(error)

		except BasePhoneException as error:
			self.valid = False
			self.phone_status = f'{error}'


		finally:
			self.update_data_of_class()

	def update_data_of_class(self):
		self.phone_data_dict = {
			'valid':    self.valid,
			'status':   self.phone_status,
			'api_data': self.phone_json_response,
			'double':   self.double,
		}
