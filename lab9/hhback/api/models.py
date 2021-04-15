from django.db import models

# Create your models here.

#One to One relation - User and Profile
#One to Many (Many to One) relation - Category and Product
#Many to Many relation - Product and Tags


class Company(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(default='', null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    address = models.TextField(default='', null=True, blank=True)

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'

    def __str__(self):
        return f'{self.id}: {self.name} | {self.city}'

    def to_json(self):
        return{
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'city': self.city,
            'address': self.address
        }

class Vacancy(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(default='', null=True, blank=True)
    salary = models.FloatField(default=0)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Vacancy'
        verbose_name_plural = 'Vacancies'
        ordering = ('-salary', )

    def __str__(self):
        return f'{self.id}: {self.name} | {self.salary} | {self.company}'

    def to_json(self):
        return{
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'salary': self.salary,
        }