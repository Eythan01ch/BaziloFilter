class BaseNameException(Exception):
    def __init__(self,  name, message=None):
        self.name = name
        self.message = message
        self.default_message = f"ERR Inconclusive name: {self.name}"

    def __str__(self):
        if self.message:
            return f'ERR Name: {self.name}, {self.message} '
        else:
            return f'{self.default_message}'

    def get_error(self):
        return {'error': self.__str__()}


class NameInvalidException(BaseNameException):
    def __init__(self, name):
        message = 'name is invalid'
        super(NameInvalidException, self).__init__(name=name, message=message)

