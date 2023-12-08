from django.shortcuts import render
from listings.choices import price_choices, bedroom_choices, state_choices, city_choices

from listings.models import Listing
from realtors.models import Realtor

# Create your views here.

def index(request):
    listings = Listing.objects.order_by('-list_date')[:3]

    context = {
        'listings': listings,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'city_choices': city_choices
    }

    return render(request, 'pages/index.html', context)

def about(request):
    # Get all realtors
    realtors = Realtor.objects.order_by('-created_date')


    context = {
        'realtors': realtors,
    }

    return render(request, 'pages/about.html', context)
