# Download the helper library from https://www.twilio.com/docs/python/install
import datetime

from twilio.rest import Client

from BaziloLeadProcessor.api_config.APIconfig import APIConfig


class SmsSender(APIConfig):

	def __init__(self, to='+972587471095'):
		super(SmsSender, self).__init__()
		self.from_ = self.twilio_api.extra
		self.to = to
		self.client = None
		self.client = Client(self.twilio_api.password, self.twilio_api.token)

	def send_sms(self, body):
		message = self.client.messages.create(
			#  the full text of the message you want to send,
			#  limited to 1600 characters.
			body=f'BAZILOO API MESSAGE from {datetime.datetime.now()}\n'
			     f'{body}\n'
			     f'Please Verify!',

			#  the Twilio phone number that we put in our account,
			#  formatted with a '+' and country code, e.g.
			from_=self.from_,
			# to - the destination phone number for your SMS message
			to=self.to
		)
		return message
