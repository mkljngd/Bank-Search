from django.shortcuts import render
from .models import Banks, Branches
import json
from django.http import HttpResponse
from django.http import JsonResponse
from django.db.models import Q


def autocomplete(request):
    branch = request.GET['branch']
    offset = int(request.GET['offset'])
    limit = int(request.GET['limit'])
    result = list(Branches.objects.filter(branch__icontains=branch).order_by('ifsc')[offset:limit].values())
    return JsonResponse(result, safe=False) 

def search(request):
    query = request.GET['q']
    offset = int(request.GET['offset'])
    limit = int(request.GET['limit'])

    result = list(Branches.objects.filter(Q(ifsc__icontains=query) | Q(bank__name__icontains=query) | Q(branch__icontains=query) | Q(address__icontains=query) | Q(city__icontains=query) | Q(district__icontains=query) | Q(state__icontains=query)).order_by('ifsc')[offset:limit].values())
    return JsonResponse(result, safe=False) 
