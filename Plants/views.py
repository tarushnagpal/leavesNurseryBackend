from Plants.models import Plant, Categories
from Plants.serializers import PlantSerializer
from rest_framework import generics
from django.http import JsonResponse, HttpResponse
from django.forms.models import model_to_dict
import json


class GetPlants(generics.ListCreateAPIView):
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer

def getCategories(request):

    to_ret = []

    for i in Categories.objects.all():
        to_ret.append( model_to_dict(i)['category_name'] )
    
    json_stuff = json.dumps({ "categories" : to_ret })    
    return HttpResponse(json_stuff, content_type ="application/json")

def GetFeaturedPlants(request):
    
    to_ret = []

    for i in Plant.objects.all():
        print(model_to_dict(i))
        if(model_to_dict(i)['is_featured']):
            ret = {}
            ret['category'] = str(model_to_dict(i)['category'])
            ret['indian_name'] = str(model_to_dict(i)['indian_name'])
            ret['binomial_name'] = str(model_to_dict(i)['binomial_name'])
            ret['image_url'] = str(model_to_dict(i)['image_url'])
            to_ret.append(ret)

    json_stuff = json.dumps({ "featuredPlants" : to_ret })    
    return HttpResponse(json_stuff, content_type ="application/json")

    return(HttpResponse( {"featuredPlants": to_ret } ))
