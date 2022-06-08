from BaziloLeadProcessor.LeadProcessor.NameProcessor.NameExceptions import NameInvalidException
from BaziloLeadProcessor.LeadProcessor.NameProcessor.NameProcessor import NameProcessor


class NameHandler(NameProcessor):
    def __init__(self, fname, lname):
        super(NameHandler, self).__init__(fname, lname)
        self.valid = None
        self.name_status = None

    def is_name_valid(self):
        try:
            self.get_name_details()
            self.valid = True
            self.name_status = "VALID Name not found in the list"
        except NameInvalidException as error:
            self.name_status = f'{error}'
            self.valid = False
