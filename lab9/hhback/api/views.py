import json
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from api.models import Company, Vacancy
from django.db.models import Count


# Create your views here.
def companies_list(request):
    if request.method == "GET":
        companies = Company.objects.all()
        companies_json = [company.to_json() for company in companies]
        return JsonResponse(companies_json, safe=False)

def company_detail(request, company_id):
    if request.method == "GET":
        try:
            company = Company.objects.get(id=company_id)
            return JsonResponse(company.to_json())
        except Company.DoesNotExist as e:
            return JsonResponse({'error': str(e)})

def company_vacancies(request, company_id):
    if request.method == "GET":
        try:
            company = Company.objects.get(id=company_id)
        except Company.DoesNotExist as e:
            return JsonResponse({'error': str(e)})

        vacancies = company.vacancy_set.all()
        vacancies_json = [vacancy.to_json() for vacancy in vacancies]

        return JsonResponse(vacancies_json, safe=False)

def vacancies_list(request):
    if request.method == "GET":
        vacancies = Vacancy.objects.all()
        vacancies_json = [vacancy.to_json() for vacancy in vacancies]
        return JsonResponse(vacancies_json, safe=False)

def vacancy_detail(request, vacancy_id):
    if request.method == "GET":
        try:
            vacancy = Vacancy.objects.get(id=vacancy_id)
            return JsonResponse(vacancy.to_json())
        except Vacancy.DoesNotExist as e:
            return JsonResponse({'error': str(e)})


def top_vacancies(request):
    if request.method == "GET":
        vacancies= Vacancy.objects.annotate(Count('salary')).order_by('-salary')[:10]
        vacancies_json = [vacancy.to_json() for vacancy in vacancies]
        return JsonResponse(vacancies_json, safe = False)