from django.contrib import admin
from api.models import Company, Vacancy
# Register your models here.

@admin.register(Vacancy)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'salary', 'description', 'company',)
    search_fields = ('name', 'salary',)
    list_filter = ('company',)


admin.site.register(Company)