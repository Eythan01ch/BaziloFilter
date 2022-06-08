# Download the helper library from https://www.twilio.com/docs/python/install
import datetime

import requests

from BaziloLeadProcessor.api_config.APIconfig import APIConfig


class EmailSender(APIConfig):

	def __init__(self, body, title, ):
		super(EmailSender, self).__init__()
		self.title = title
		self.from_ = self.mailgun_api.extra
		self.to = 'blackhat2203@gmail.com'
		print(self.to)
		self.default_message = \
			f'BAZILOO API MESSAGE from {datetime.datetime.now()}\n{body}\nPlease Verify!',


	def send_simple_message(self):
		response = requests.post(
			self.mailgun_api.url,
			auth=('api', self.mailgun_api.token),
			data={
				"from":    self.from_,
				"to":      self.to,
				"subject": self.title,
				"text":    self.default_message
			})
		return response

