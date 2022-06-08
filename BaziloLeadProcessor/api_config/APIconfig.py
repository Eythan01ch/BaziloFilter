import json

from BaziloLeadProcessor.api_config import PATH_API_JSON
from BaziloLeadProcessor.api_config.api_access import APIAccess
from BaziloLeadProcessor.models import APIUtils


class APIConfig:
	def __init__(self):
		with open(PATH_API_JSON, 'r') as f:
			json_file = json.load(f)
			self.json_file = json_file

			self.zerobounce_json = self.json_file.get('zerobounce')
			self.hlr_json = self.json_file.get('hlr')
			self.twilio_json = self.json_file.get('twilio')
			self.mailgun_json = self.json_file.get('mailgun')

			self.email_api = APIAccess(
				name='zerobounce',
				token=self.zerobounce_json.get('token'),
				password=self.zerobounce_json.get('password'),
				url=self.zerobounce_json.get('url'),
				sec_url=self.zerobounce_json.get('sec_url'),
				extra=self.zerobounce_json.get('extra'),
			)

			self.phone_api = APIAccess(
				name='hrl',
				url=self.hlr_json.get('url'),
				sec_url=self.hlr_json.get('sec_url'),
				extra=self.hlr_json.get('extra'),
				token=self.hlr_json.get('token'),
				password=self.hlr_json.get('password'),
			)


			self.twilio_api = APIAccess(
				name='twilio',
				url=self.twilio_json.get('url'),
				sec_url=self.twilio_json.get('sec_url'),
				extra=self.twilio_json.get('extra'),
				token=self.twilio_json.get('token'),
				password=self.twilio_json.get('password'),
			)
			self.mailgun_api = APIAccess(
				name='mailgun',
				url=self.mailgun_json.get('url'),
				sec_url=self.mailgun_json.get('sec_url'),
				extra=self.mailgun_json.get('extra'),
				token=self.mailgun_json.get('token'),
				password=self.mailgun_json.get('password'),
			)

