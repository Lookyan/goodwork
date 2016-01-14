from django.db import models


class CompanyManager(models.Manager):
    def get_by_name_part(self, term):
        companies = self.model.objects.filter(name__icontains=term)
        names = list()
        for company in companies:
            names.append({'value': company.name})
        return names

    def check_company_exists(self, name):
        quantity = self.model.objects.filter(name__iexact=name.strip()).count()
        return quantity != 0