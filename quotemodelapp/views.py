from django.shortcuts import render
from quotemodelapp.models import Quote

# Create your views here.

def get_quotes(request):
    return render(request, 'quotemodel/home.html',
                  {'quotes_list': Quote.objects.all()})
