from django.db.models.expressions import F
from django.http.response import JsonResponse
from django.shortcuts import render

from calculator.models import Calculate, Term

import json
# Create your views here.

def calc(req):

    dataPrice = list(Calculate.objects.values())
    responsePrice = json.dumps(dataPrice)

    dataTerm = list(Term.objects.values())
    responseTerm = json.dumps(dataTerm)
    
    context = {
        'is_worker': req.user.groups.filter(name='worker').exists(),
        'responseAll': responsePrice + responseTerm,
    }

    return render(req, 'calculator.html', context)