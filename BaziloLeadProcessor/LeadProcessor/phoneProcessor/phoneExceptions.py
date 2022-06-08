class BasePhoneException(Exception):
    def __init__(self, phone, message=None):
        self.phone = phone
        self.message = message
        self.default_message = f"ERR Inconclusive phone: {self.phone}"

    def __str__(self):
        if self.message:
            return f'ERR phone: {self.phone}, {self.message} '
        else:
            return f'{self.default_message}'

    def get_error(self):
        return {'error': self.__str__()}


class PhoneAlreadyRegisteredException(BasePhoneException):
    def __init__(self, phone):
        message = 'Phone is already Registered'
        super(PhoneAlreadyRegisteredException, self).__init__(phone=phone, message=message)


class PhonePatternInvalidException(BasePhoneException):
    def __init__(self, phone):
        message = 'Phone does not match Phone pattern'
        super(PhonePatternInvalidException, self).__init__(phone=phone, message=message)


class PhoneInvalidException(BasePhoneException):
    def __init__(self, phone):
        message = 'API phone status: invalid'
        super(PhoneInvalidException, self).__init__(phone=phone, message=message)


class OutOfCreditsException(BasePhoneException):
    def __init__(self, phone):
        message = 'API is out of credits ADD MORE CREDITS Phones Cant be filtered!'
        super(OutOfCreditsException, self).__init__(phone=phone, message=message)


class SoonOutOfCreditsException(BasePhoneException):
    def __init__(self, phone, credits_left):
        message = f'API is Soon out of credits: {credits_left}, CONSIDER TO ADD MORE CREDITS TO PHONE API!  '
        super(SoonOutOfCreditsException, self).__init__(phone=phone, message=message)


class CouldNotAuthenticateException(BasePhoneException):
    def __init__(self, phone):
        message = "API couldn't not authenticate API KEY OR PASSWORD"
        super(CouldNotAuthenticateException, self).__init__(phone=phone, message=message)


