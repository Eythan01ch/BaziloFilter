
class BaseEmailException(Exception):
    """base exception That are inherited from him,
    Whenever there is one of the problems, the message will be written"""

    def get_error(self):
        return {'error': self.__str__()}

    def __init__(self, email, message=None):
        self.email = email
        self.message = message
        self.default_message = f"ERR Inconclusive email: {self.email}"

    def __str__(self):
        if self.message:
            return f'ERR Email: {self.email}, {self.message} '
        else:
            return f'{self.default_message}'


class EmailAlreadyRegisteredException(BaseEmailException):
    """exception will be if the email is already exist in the database"""

    def __init__(self, email):
        message = 'Email is already Registered'
        super(EmailAlreadyRegisteredException, self).__init__(email=email, message=message)


class EmailPatternInvalidException(BaseEmailException):
    """exception will be if something is not good in the email pattern"""

    def __init__(self, email):
        message = 'Email does not match email pattern'
        super(EmailPatternInvalidException, self).__init__(email=email, message=message)


class EmailInvalidException(BaseEmailException):
    """exception will be if the email is not valid"""

    def __init__(self, email):
        message = 'API returned email-status invalid'
        super(EmailInvalidException, self).__init__(email=email, message=message)


class EmailOutOfCreditsOrInvalidKey(BaseEmailException):
    """exception will be there is nothing left in the credit"""

    def __init__(self, email):
        message = 'API is Out of credits or invalid api-key'
        super(EmailOutOfCreditsOrInvalidKey, self).__init__(email=email, message=message)


class EmailOutOfCredits(BaseEmailException):
    """exception will be if the credit is about to run out soon"""

    def __init__(self, email, api_credits):
        message = f'API is Out of credits amount: {api_credits}'
        super(EmailOutOfCredits, self).__init__(email=email, message=message)


class EmailInvalidKey(BaseEmailException):
    def __init__(self, email):
        message = 'API invalid api-key PLEASE FIX IMMEDIATELY!!!!'
        super(EmailInvalidKey, self).__init__(email=email, message=message)


class EmailSoonOutOfCredits(BaseEmailException):
    def __init__(self, email, amount):
        message = f'API is Soon Out of credits {amount}'
        super(EmailSoonOutOfCredits, self).__init__(email=email, message=message)
