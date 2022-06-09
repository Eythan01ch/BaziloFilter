import json

from rest_framework.authtoken.admin import User
from rest_framework.authtoken.models import Token

from django.test import TestCase
from rest_framework.test import APIClient

from BaziloLeadProcessor.models import APIUtils


class TestUtils(TestCase):
	def __init__(self, *args, **kwargs):
		token = Token.objects.get(user__username='user')
		self.my_client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

		super(TestUtils, self).__init__(*args, **kwargs)

		self.CONTENT_TYPE = 'application/json'
		self.VALID_PHONE = '0987654321'
		self.INVALID_PHONE = '0007654321'
		self.VALID_EMAIL = 'blackhat2203@gmail.com'
		self.INVALID_EMAIL = 'blackhat03@gmail.com'
		self.TEST_STR = 'TEST'
		self.IP = '1.2.3.4'
		self.POST_LEAD_PATH = '/api/process_lead/'

	@staticmethod
	def response_to_json(response):
		return json.loads(response.content.decode('utf8').replace("'", "'"))

	def setup_init(self):
		self.my_client = APIClient()

		APIUtils.objects.create(
			name='hrl',
			status=0,
			credits=0,
		)
		APIUtils.objects.create(
			name='mailgun',
			status=0,
			credits=0,
		)
		APIUtils.objects.create(
			name='zerobounce',
			status=0,
			credits=0,
		)
		APIUtils.objects.create(
			name='twilio',
			status=0,
			credits=0,
		)
		User.objects.create(
			username='user',
			password='password',
		)
		Token.objects.create(
			user_id=1,
			key='1'
		)

	def response_ok_validation(self, response):
		self.assertEqual(response.status_code, 201)

	def create_response(self, body):
		response = self.my_client.post(
			path=self.POST_LEAD_PATH,
			data=json.dumps(body),
			content_type=self.CONTENT_TYPE
		)
		self.response_ok_validation(response=response)
		return self.response_to_json(response)
