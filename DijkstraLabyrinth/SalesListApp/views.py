from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from SalesListApp.models import HepsiBurada
from SalesListApp.serializers import HepsiBuradaSerializer


@csrf_exempt
def hepsiburadaApi(request):
    if request.method == 'GET':
        #hepsiburada_list = HepsiBurada.objects.all()
        #hepsiburada_serializer = HepsiBuradaSerializer(hepsiburada_list, many=True)
        #return JsonResponse(hepsiburada_serializer.data, safe=False)
        ...
    elif request.method == 'POST':
        hepsiburada_data = JSONParser().parse(request)
        hepsiburada_serializer = HepsiBuradaSerializer(data=hepsiburada_data)
        if hepsiburada_serializer.is_valid():
            hepsiburada_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
    return JsonResponse("Failed to Add", safe=False)


kategori_liste = ["İşlemci","Ram","Depolama", "Ekran"]
ozellik_liste = ["Intel core i3","Intel core i5","Intel core i7", "Intel core i9"]


computer_list = [
    {
        "id": 1,
        "name": "Casper Nirvana S500",
        "price": "9598.99 TL",
        "url": "https://www.hepsiburada.com/casper-nirvana-s500-1135-4p00t-g-f-intel-core-i5-1135g7-4gb-250gb-ssd-windows-11-home-15-6-fhd-tasinabilir-bilgisayar-p-HBCV000017G4PO",
        "price1": "12999 TL",
        "url1": "https://www.vatanbilgisayar.com/casper-nirvana-11-nesil-core-i5-1135g7-8gb-500gb-ssd-15-6inc-w11.html",
        "price2": "13299 TL",
        "url2": "https://www.teknosa.com/casper-nirvana-s50011358d00tgf-intel-core-i5-1135g7-156-8-gb-240-gb-ssd-windows-11-home-fhd-tasinabilir-bilgisayar-p-125034153",
        "price3": "11999 TL",
        "url3": "https://www.trendyol.com/casper/nirvana-s500-1135-8d00x-g-f-intel-11-nesil-i5-1135g7-8gb-ram-240gb-ssd-freedos-p-119978624?boutiqueId=61&merchantId=129813",
        "image": "https://productimages.hepsiburada.net/s/283/550/110000271206677.jpg",

        "islemci": "Intel Core i5",
        "islemci_nesli": "11. Nesil",
        "ram": "4GB",
        "depolama": "250GB",
        "ekran": "15,6 inç",
        "isletim_sistemi": "Windows 11 Home"



    },
    {
        "id": 2,
        "name": "Dell Inspiron 3511",
        "price": "10998.99 TL",
        "price1": "10998.99 TL",
        "price2": "10998.99 TL",
        "price3": "10998.99 TL",
        "image": "https://productimages.hepsiburada.net/s/173/550/110000136542954.jpg"
    },

    {
        "id": 3,
        "name": "Huawei Matebook D15",
        "price": "21533.99 TL",
        "price1": "10998.99 TL",
        "price2": "10998.99 TL",
        "price3": "10998.99 TL",
        "image": "https://productimages.hepsiburada.net/s/176/550/110000140392348.jpg"

    },
    {
        "id": 4,
        "name": "Casper Excalibur G770.1140-8EL0T-B",
        "price": "22599 TL",
        "price1": "10998.99 TL",
        "price2": "10998.99 TL",
        "price3": "10998.99 TL",
        "image": "https://productimages.hepsiburada.net/s/241/550/110000225490826.jpg"
    }]



def home(request):
    data = {
        "kategoriler": kategori_liste,
        "computers": computer_list,
        "ozellikler": ozellik_liste
    }
    return render(request, "index.html", data)
def pcs(request):
    ...

def pc_details(request, id):
    data = {
        "id": id,
        "computers": computer_list,
        "kategoriler": kategori_liste,
        "ozellikler": ozellik_liste
    }

    return render(request, "details.html", data)




