from BaziloLeadProcessor.LeadProcessor.emailProcessor.EmailProcessor import EmailProcessor
from BaziloLeadProcessor.LeadProcessor.emailProcessor.emailExceptions import (BaseEmailException,
                                                                              EmailAlreadyRegisteredException,
                                                                              EmailInvalidKey, EmailOutOfCredits,
                                                                              EmailPatternInvalidException,
                                                                              EmailSoonOutOfCredits, )
from BaziloLeadProcessor.LeadProcessor.utils.sms_sender import SmsSender


class EmailHandler(EmailProcessor):
    def __init__(self, email, ip):
        super(EmailHandler, self).__init__(email, ip)
        self.email_data_dict = {}
        self.ip = ip
        self.email = email
        self.double = None
        self.valid = None
        self.email_status = None
        self.sms_handler = SmsSender()
        self.is_email_pattern_valid_method_called = None
        self.is_double_email_method_called = None
        self.is_email_valid_method_called = None


    def is_double_email(self):
        """is email already in DB? if so will catch an error"""
        try:
            self.is_email_exist()
        except EmailAlreadyRegisteredException as error:
            self.double = True
            self.valid = False
            self.email_status = f'{error}'
        finally:
            self.is_double_email_method_called = True
            self.update_data_of_class()


    def is_email_pattern_valid(self):
        try:
            self.is_possible_email()
        except EmailPatternInvalidException as error:
            self.valid = False
            self.email_status = f'{error}'
        finally:
            self.is_email_pattern_valid_method_called = True
            self.update_data_of_class()



    def is_email_valid(self):
        self.is_email_valid_method_called = True
        """will run only if all the above called before"""
        if not self.is_email_pattern_valid_method_called:
            self.is_email_pattern_valid()
        if not self.is_double_email_method_called:
            self.is_double_email()

        if self.valid == False:
            return False

        try:
            self.get_email_details()
            self.email_status = self.email_json_response.get('sub_status')
            self.valid = self.email_json_response.get('status') == 'valid'

        except EmailSoonOutOfCredits as error:
            self.email_status = error
            self.sms_handler.send_sms(error)
            self.valid = self.email_json_response.get('status') == 'valid'

        except (EmailInvalidKey, EmailOutOfCredits) as error:
            self.valid = True
            self.email_status = error
            self.sms_handler.send_sms(error)

        except BaseEmailException as error:
            self.valid = True
            self.email_status = error
            self.sms_handler.send_sms(error)

        finally:
            self.update_data_of_class()


    def update_data_of_class(self):
        self.email_data_dict = {
            'valid': self.valid,
            'status': self.email_status,
            'api_data': self.email_json_response,
            'double': self.double,
        }

