import requests

from BaziloLeadProcessor.LeadProcessor.phoneProcessor.phoneExceptions import SoonOutOfCreditsException
from BaziloLeadProcessor.api_config.APIconfig import APIConfig
from BaziloLeadProcessor.models import Lead


class PhoneUtils(APIConfig):
    def __init__(self, phone):
        super(PhoneUtils, self).__init__()
        self.phone = phone

    @staticmethod
    def get_phones():
        """get the phones list from the phone values"""
        phones_query_set = Lead.objects.values('phone')
        phones_list = [phone_dict['phone'] for phone_dict in phones_query_set]
        return phones_list

    def format_phone(self):
        """checked the format phone (france phone)"""
        phone = self.phone
        # checking if the country code is included for the Phone number test
        if phone[0] == "0":
            new_tel = "33" + phone[1:]
            phone = new_tel
        return phone

    def get_usage_amount(self):
        """trying to get how many times we used the api"""
        return self.phone_api.get_usage_amount()

    def get_credits(self):
        """gets how many credits left"""
        full_api_url = self.phone_api.sec_url.format(self.phone_api.token, self.phone_api.password, self.phone)
        phone_response = requests.get(full_api_url)
        phone_json_response = phone_response.json()
        return phone_json_response.get('Credits')

    def is_low_on_credits(self):
        """checked if the credits about to run soon"""
        usage = self.get_usage_amount()
        if usage % 10 == 0:
            credits_left = self.get_credits()
            if credits_left < 1000:
                raise SoonOutOfCreditsException(self.phone, credits_left)

    def raise_amount_of_usage(self):
        """every time we run, count +1 and saving the new count"""
        self.phone_api.raise_amount_of_usage()
