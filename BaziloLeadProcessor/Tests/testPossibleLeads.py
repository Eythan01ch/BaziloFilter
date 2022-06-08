from BaziloLeadProcessor.Tests.TestLeadsHelper import TestHelper




class TestPossibleLeads(TestHelper):

	def setUp(self):
		self.setup_init()
		self.valid_payload = {
			'fname': self.TEST_STR,
			'ip':    self.IP,
			'email': self.VALID_EMAIL,
			'phone': self.VALID_PHONE,
			'lname': self.TEST_STR
		}
		self.invalid_email_payload = {
			'fname': self.TEST_STR,
			'ip':    self.IP,
			'email': self.INVALID_EMAIL,
			'phone': self.VALID_PHONE,
			'lname': self.TEST_STR
		}
		self.invalid_phone_payload = {
			'fname': self.TEST_STR,
			'ip':    self.IP,
			'email': self.VALID_EMAIL,
			'phone': self.INVALID_PHONE,
			'lname': self.TEST_STR
		}
		self.invalid_email_phone_payload = {
			'fname': self.TEST_STR,
			'ip':    self.IP,
			'email': self.INVALID_EMAIL,
			'phone': self.INVALID_PHONE,
			'lname': self.TEST_STR
		}

	def test_create_valid_lead(self):
		response_json = self.create_response(self.valid_payload)
		self.verify_lead_valid(r_json=response_json)

	def test_create_invalid_email_lead(self):
		response_json = self.create_response(self.invalid_email_payload)
		self.verify_param_valid(r_json=response_json, param_tested='phone')
		self.verify_param_valid(r_json=response_json, param_tested='name')
		self.verify_param_invalid(r_json=response_json, param_tested='email')
		self.verify_lead_invalid(r_json=response_json)

	def test_create_invalid_phone_lead(self):
		response_json = self.create_response(self.invalid_phone_payload)
		self.verify_param_valid(r_json=response_json, param_tested='email')
		self.verify_param_valid(r_json=response_json, param_tested='name')
		self.verify_param_invalid(r_json=response_json, param_tested='phone')
		self.verify_lead_invalid(r_json=response_json)

	def test_create_invalid_email_phone_lead(self):
		response_json = self.create_response(self.invalid_email_phone_payload)
		self.verify_param_valid(r_json=response_json, param_tested='name')
		self.verify_param_invalid(r_json=response_json, param_tested='email')
		self.verify_param_invalid(r_json=response_json, param_tested='phone')
		self.verify_lead_invalid(r_json=response_json)

	def test_create_double_lead(self):
		first_response = self.create_response(self.valid_payload)
		second_response = self.create_response(self.valid_payload)
		self.verify_lead_valid(r_json=first_response)
		self.verify_is_not_double(r_json=second_response)
		self.verify_lead_invalid(r_json=second_response)

