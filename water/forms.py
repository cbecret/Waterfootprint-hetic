from django import forms

from .models import WaterData


def get_country():
    return[(country, country) for country in WaterData.objects.values_list('country', flat=True).distinct()]


def get_region():
    return [(region, region) for region in WaterData.objects.values_list('region', flat=True).distinct()]


def get_category():
    return [(category, category) for category in WaterData.objects.values_list('category', flat=True).distinct()]


def get_product():
    return [(product, product) for product in WaterData.objects.values_list('product', flat=True).distinct()]


COUNTRY = get_country()
REGION = get_region()
CATEGORY = get_category()
PRODUCT = get_product()


class WaterDataForm(forms.Form):
    product = forms.MultipleChoiceField(
        required=False,
        widget=forms.Select,
        choices=PRODUCT,
    )
    country = forms.MultipleChoiceField(
        required=True,
        widget=forms.Select,
        choices=COUNTRY,
    )
    region = forms.MultipleChoiceField(
        required=False,
        widget=forms.Select,
        choices=REGION,
    )
