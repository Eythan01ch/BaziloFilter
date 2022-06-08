from BaziloLeadProcessor.models import InvalidName


class NameUtils:

    @staticmethod
    def get_names():
        names_query_set = InvalidName.objects.values('name')
        names_list = [name['name'] for name in names_query_set]
        return names_list



