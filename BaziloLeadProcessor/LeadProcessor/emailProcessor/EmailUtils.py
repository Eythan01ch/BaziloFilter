import requests

from BaziloLeadProcessor.LeadProcessor.emailProcessor.emailExceptions import EmailSoonOutOfCredits
from BaziloLeadProcessor.api_config.APIconfig import APIConfig
from BaziloLeadProcessor.models import Lead


class EmailUtils(APIConfig):
    def __init__(self, email):
        super(EmailUtils, self).__init__()
        self.email = email

    @staticmethod
    def get_emails():
        emails_query_set = Lead.objects.values('email')
        emails_list = [email_dict['email'] for email_dict in emails_query_set]
        return emails_list


    def get_credits(self):
        """get how many credits left in Zero Bounce API"""
        params = {'api_key': self.email_api.token}
        email_response = requests.get(self.email_api.sec_url, params)
        email_response_json = email_response.json()
        return int(email_response_json.get('Credits'))


    def is_low_on_credits(self):
        """checked if we have a credits or not every 10 credits,
        and if we don't have enough, rase exception that send an email that the credits out soon"""
        usage = self.email_api.get_usage_amount()
        if usage % 10 == 0:
            credits_left = self.get_credits()
            self.email_api.save_credits(credits_left)
            if credits_left < 100:
                raise EmailSoonOutOfCredits(self.email, credits_left)
