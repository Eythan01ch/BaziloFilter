from BaziloLeadProcessor.models import APIUtils


class APIAccess:
	def __init__(self, token, password, url, sec_url, extra, name):
		self.name = name
		self.password = password
		self.token = token
		self.sec_url = sec_url
		self.url = url
		self.extra = extra


	def get_usage_amount(self):

		"""trying to get how many times we use the api(for the database)"""
		return APIUtils.objects.get(name=self.name).usage

	def raise_amount_of_usage(self):
		"""every time we run, count +1 and saving the new count"""

		api = APIUtils.objects.get(name=self.name)
		api.usage += 1
		api.save()

	def save_credits(self, credits):

		api = APIUtils.objects.get(name=self.name)
		api.credits = credits
		api.save()

