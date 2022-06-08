from BaziloLeadProcessor.LeadProcessor.NameProcessor.NameHandler import NameHandler
from BaziloLeadProcessor.LeadProcessor.emailProcessor.EmailHandler import EmailHandler
from BaziloLeadProcessor.LeadProcessor.phoneProcessor.PhoneHandler import PhoneHandler
from BaziloLeadProcessor.serializers import LeadEmailInfoSerializer, LeadPhoneInfoSerializer, NewLeadSerializer


class LeadProcessor:
	"""
	class for processing Lead
	params_needed = phone, email, ip, fname, lname
	"""

	def __init__(self, phone, email, ip, fname, lname, **kwargs):
		self.name_status = None
		self.valid = None
		self.email_valid = None
		self.phone_valid = None
		self.name_valid = None
		self.fname = fname
		self.lname = lname
		self.phone_status = None
		self.email_status = None
		self.double = None
		self.ip = ip
		self.email = email
		self.phone = phone
		# the data received from the different api
		self.lead_dict_data = {}
		self.email_handler = EmailHandler(email=self.email, ip=self.ip)
		self.phone_handler = PhoneHandler(phone=self.phone)
		self.name_handler = NameHandler(fname=self.fname, lname=self.lname)

	def __str__(self):
		return f'\nvalid: {self.valid}' \
		       f'\nemail_valid: {self.email_valid}' \
		       f'\nphone_valid: {self.phone_valid}' \
		       f'\ndouble: {self.double}' \
		       f'\nphone_status: {self.phone_status}' \
		       f'\nemail_status: {self.email_status}'

	def save_email_info_to_db(self):
		email_data = self.lead_dict_data.get('email_data')
		email_serializer = LeadEmailInfoSerializer(data=email_data.get('api_data'))
		if email_serializer.is_valid():
			self.email_instance = email_serializer.save()

	def save_phone_info_to_db(self):
		phone_data = self.lead_dict_data.get('phone_data')
		phone_serializer = LeadPhoneInfoSerializer(data=phone_data.get('api_data'))
		if phone_serializer.is_valid():
			self.phone_instance = phone_serializer.save()

	def save_lead_info_to_db(self):
		lead_data = {
			'valid':           self.valid,
			'email_valid':     self.email_valid,
			'phone_valid':     self.phone_valid,
			'name_valid':      self.name_valid,
			'fname':           self.fname,
			'lname':           self.lname,
			'phone_status':    self.phone_status,
			'email_status':    self.email_status,
			'name_status':     self.name_status,
			'double':          self.double,
			'ip':              self.ip,
			'email':           self.email,
			'phone':           self.phone,
			'lead_email_info': self.email_instance.id,
			'lead_phone_info': self.phone_instance.id,
		}

		lead_serializer = NewLeadSerializer(data=lead_data)
		if lead_serializer.is_valid():
			return lead_serializer.save()
		else:
			raise lead_serializer.errors

	def save_validity(self):

		email_data = self.lead_dict_data.get('email_data')
		phone_data = self.lead_dict_data.get('phone_data')

		self.email_valid = email_data.get('valid')
		self.phone_valid = phone_data.get('valid')
		self.name_valid = self.name_handler.valid
		self.valid = self.email_valid and self.phone_valid and self.name_valid

		if not self.valid and email_data.get('double') or phone_data.get('double'):
			self.double = True

		self.email_status = email_data.get('status')
		self.phone_status = phone_data.get('status')
		self.name_status = self.name_handler.name_status

	def save_data(self):
		self.lead_dict_data['email_data'] = self.email_handler.email_data_dict
		self.lead_dict_data['phone_data'] = self.phone_handler.phone_data_dict
		self.save_validity()
		self.save_email_info_to_db()
		self.save_phone_info_to_db()
		return self.save_lead_info_to_db()

	def process_lead(self):
		self.name_handler.is_name_valid()
		self.email_handler.is_email_valid()
		self.phone_handler.is_phone_valid()
		return self.save_data()
