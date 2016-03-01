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


class JobTypeManager(models.Manager):
    def get_by_title_part(self, pos):
        types = self.model.objects.filter(name__icontains=pos)
        names = []
        for job_type in types:
            names.append({'value': job_type.name})
        return names

    def create_if_not_exist(self, position):
        pos = self.model.objects.filter(name__iexact=position.strip())
        if len(pos) == 0:
            job_type = self.model()
            job_type.name = position
            job_type.save()
            return job_type
        return pos[0]