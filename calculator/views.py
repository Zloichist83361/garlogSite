from consignment.models import Cities
from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse

from rest_framework import status
from rest_framework.parsers import JSONParser 
from rest_framework.decorators import api_view

from calculator.models import Calculate, Term
from calculator.serializers import CalculateSerializer, TermSerializer

import json
# Create your views here.

def calc(request):

    context = { 
        'is_worker': request.user.groups.filter(name='worker').exists(),
    }
    
    return render(request, 'calculator.html', context)


def get_cities(request):
    if request.is_ajax():
        q = request.GET.get('cities')
        all_city = Cities.objects.filter(cities__icontains=q)
        results = []
        for city in all_city:
            city_json = {}
            city_json = city.cities
            results.append(city_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)


@api_view(['GET', 'POST'])
def create_calculate(request):  
    if request.method == 'GET':
        calc_api = Calculate.objects.all()
        calc_api_serializer = CalculateSerializer(calc_api, many=True)
        return JsonResponse(calc_api_serializer.data, safe=False)

    elif request.method == 'POST':
        calc_api_data = JSONParser().parse(request)
        calc_api_serializer = CalculateSerializer(data=calc_api_data, many=True)
        if calc_api_serializer.is_valid():
            calc_api_serializer.save()
            return JsonResponse(calc_api_serializer.data, safe=False, status=status.HTTP_201_CREATED)
        return JsonResponse(calc_api_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def update_calculate(request, pk):
    try:
        calc_api = Calculate.objects.get(pk=pk)
    except Calculate.DoesNotExist:
        return JsonResponse({'message': 'Накладной не существует'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        calc_api_data = JSONParser().parse(request)
        calc_api_serializer = CalculateSerializer(calc_api, data=calc_api_data)
        if calc_api_serializer.is_valid():
            calc_api_serializer.save()
            return JsonResponse(calc_api_serializer.data, safe=False, status=status.HTTP_201_CREATED)
        return JsonResponse(calc_api_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def create_term(request):  
    if request.method == 'GET':
        term_api = Term.objects.all()
        term_api_serializer = TermSerializer(term_api, many=True)
        return JsonResponse(term_api_serializer.data, safe=False)

    elif request.method == 'POST':
        term_api_data = JSONParser().parse(request)
        term_api_serializer = TermSerializer(data=term_api_data, many=True)
        if term_api_serializer.is_valid():
            term_api_serializer.save()
            return JsonResponse(term_api_serializer.data, safe=False, status=status.HTTP_201_CREATED)
        return JsonResponse(term_api_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def update_term(request, pk):
    try:
        term_api = Term.objects.get(pk=pk)
    except Term.DoesNotExist:
        return JsonResponse({'message': 'Накладной не существует'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        term_api_data = JSONParser().parse(request)
        term_api_serializer = TermSerializer(term_api, data=term_api_data)
        if term_api_serializer.is_valid():
            term_api_serializer.save()
            return JsonResponse(term_api_serializer.data, safe=False, status=status.HTTP_201_CREATED)
        return JsonResponse(term_api_serializer.errors, status=status.HTTP_400_BAD_REQUEST)





def db(request):
    queryset_calc = Calculate.objects.all()
    queryset_term = Term.objects.all()
    context = {
        'calcs': queryset_calc,
        'terms': queryset_term,
    }
    
    return render(request, 'db.html', context)