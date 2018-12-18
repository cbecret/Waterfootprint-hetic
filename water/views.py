import json
from django.http import HttpResponse
from django.shortcuts import render

from .forms import WaterDataForm
from .models import WaterData


def index(request):
    return HttpResponse("Hello, world. You're at the water index.")


def get_country():
    return WaterData.objects.values_list('country', flat=True).distinct()


def get_category():
    return WaterData.objects.values_list('category', flat=True).distinct()


def get_product():
    return WaterData.objects.values_list('product', flat=True).distinct()


def search(request):
    provinces_file = open('water/templates/water/province.json', 'r')
    provinces_json = json.loads(provinces_file.read())
    provinces_file.close()

    form = WaterDataForm(request.POST)
    data = {}
    context = {
        'all_country': get_country(),
        'all_category': get_category(),
        'all_product': get_product(),
        'form': form,
        'data': data,
        'waterdata': {},
    }
    context['data']['provinces_json'] = provinces_json

    if form.is_valid:
        params = request.POST.copy()
        context['data'] = params
        context['data']['provinces_json'] = provinces_json

        data = WaterData.objects.filter(region=params.get('region'), product=params.get('product'))
        for e in data:
            context['data']['blue'] = e.blue
            context['data']['green'] = e.green
            context['data']['grey'] = e.grey

        world_data = WaterData.objects.filter(region='Global average', product=params.get('product'))
        for e in world_data:
            context['data']['worldBlue'] = e.blue
            context['data']['worldGreen'] = e.green
            context['data']['worldGrey'] = e.grey

        return render(request, 'water/search.html', context=context)

    return render(request, 'water/search.html', context=context)
