from BaziloLeadProcessor.LeadProcessor.NameProcessor.NameExceptions import NameInvalidException
from BaziloLeadProcessor.LeadProcessor.NameProcessor.NameUtils import NameUtils


class NameProcessor(NameUtils):

    def __init__(self, fname, lname):
        super(NameProcessor, self).__init__()
        self.fname = fname
        self.lname = lname

    def get_name_details(self):
        names = self.get_names()
        if self.fname not in names:
            # and self.lname not in names:
            return True
        else:
            raise NameInvalidException(f'{self.lname} {self.fname}')
