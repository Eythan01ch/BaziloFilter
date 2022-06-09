from django.db import models


# Create your models here.

class LeadStoreBaseModel(models.Model):
	is_deleted = models.BooleanField(default=False)
	updated_at = models.DateTimeField(auto_now=True)
	date_created = models.DateTimeField(auto_now_add=True, null=False, blank=False)

	class Meta:
		abstract = True


# data we can extract from the lead initial data with email, ip, phone
class LeadEmailInfo(LeadStoreBaseModel):
	address = models.CharField(max_length=248, null=True, blank=True)
	status = models.CharField(max_length=248, null=True, blank=True)
	sub_status = models.CharField(max_length=248, null=True, blank=True)
	free_email = models.BooleanField(null=True, blank=True)
	did_you_mean = models.CharField(max_length=248, null=True, blank=True)
	account = models.CharField(max_length=248, null=True, blank=True)
	domain = models.CharField(max_length=248, null=True, blank=True)
	domain_age_days = models.CharField(max_length=248, null=True, blank=True)
	smtp_provider = models.CharField(max_length=248, null=True, blank=True)
	mx_record = models.CharField(max_length=248, null=True, blank=True)
	mx_found = models.CharField(max_length=248, null=True, blank=True)
	firstname = models.CharField(max_length=248, null=True, blank=True)
	lastname = models.CharField(max_length=248, null=True, blank=True)
	gender = models.CharField(max_length=248, null=True, blank=True)
	country = models.CharField(max_length=248, null=True, blank=True)
	region = models.CharField(max_length=248, null=True, blank=True)
	city = models.CharField(max_length=248, null=True, blank=True)
	zipcode = models.CharField(max_length=248, null=True, blank=True)
	processed_at = models.CharField(max_length=248, null=True, blank=True)

	def __str__(self):
		return f'{self.status}'


class LeadPhoneInfo(LeadStoreBaseModel):
	Status = models.CharField(max_length=248, null=True, blank=True)
	Region = models.CharField(max_length=248, null=True, blank=True)
	CountryCode = models.CharField(max_length=248, null=True, blank=True)
	Type = models.CharField(max_length=248, null=True, blank=True)
	Country_Name = models.CharField(max_length=248, null=True, blank=True)
	Area = models.CharField(max_length=248, null=True, blank=True)
	Original_Network = models.CharField(max_length=2048, null=True, blank=True)

	def __str__(self):
		return f'{self.Status}'


class Lead(LeadStoreBaseModel):
	# will be set after the validation of the lead
	valid = models.BooleanField(null=True)
	email_valid = models.BooleanField(null=True)
	name_valid = models.BooleanField(null=True)
	phone_valid = models.BooleanField(null=True)
	email_status = models.CharField(max_length=248, null=True, blank=True)
	phone_status = models.CharField(max_length=248, null=True, blank=True)
	name_status = models.CharField(max_length=248, null=True, blank=True)
	double = models.BooleanField(null=True)

	notes = models.CharField(max_length=10000, null=True, blank=True)

	# lead basic data we get from the form
	fname = models.CharField(max_length=255)
	lname = models.CharField(max_length=255)
	email = models.EmailField(max_length=255)
	phone = models.CharField(max_length=255)
	ip = models.GenericIPAddressField(max_length=255)

	# campaign landed by the lead, one to many
	lead_email_info = models.ForeignKey(to=LeadEmailInfo, on_delete=models.RESTRICT, null=True, blank=True)
	lead_phone_info = models.ForeignKey(to=LeadPhoneInfo, on_delete=models.RESTRICT, null=True, blank=True)

	def __str__(self):
		return f'{self.fname} {self.valid}'


class APIUtils(models.Model):
	name = models.CharField(max_length=248)
	usage = models.IntegerField(default=0, null=False, blank=False)
	status = models.CharField(default='OK', max_length=248, null=True, blank=True)
	credits = models.IntegerField(default=None, null=True, blank=True)

	def __str__(self):
		return f'{self.name} {self.status} usage: {self.usage} credits: {self.credits}'

	class Meta:
		db_table = 'APIUtils'


class InvalidName(models.Model):
	name = models.CharField(max_length=248, null=True, )

	def __str__(self):
		return f'  {self.name} '
