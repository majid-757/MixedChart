from django.shortcuts import render
from .models import ProductSell
from json import dumps



def indexView(request):

    productSell = ProductSell()

    result = productSell.get_report()

    dataJSON = dumps(result)

    context = {

        "result":dataJSON

    }


    return render(request, 'dashboard/index.html', context)


    