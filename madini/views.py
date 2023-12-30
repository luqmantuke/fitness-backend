from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .serializers import *
from .models import *
from django.db.models import Q, Case, When


# Create your views here.

@csrf_exempt
def fetch_madini(request):
    madini = Madini.objects.all()
    madini_serializer = MadiniSerializer(madini, many=True).data
    return JsonResponse({'status': 'success', 'message': 'Madini fetched successfully', 'status_code': 200,
                         'data': list(madini_serializer)})

@csrf_exempt
def fetch_search_madini(request):
    search_query = request.POST.get('search_query')
    madini = Madini.objects.filter(Q(title__icontains=search_query)| Q(
        content__icontains=search_query))
    if madini.exists():

        madini_serializer = MadiniSerializer(madini, many=True).data

        return JsonResponse({'status': 'success', 'message': 'Madini search successfully', 'status_code': 200,
                             'data': list(madini_serializer)}, status=200)
    else:
        return JsonResponse({'status': 'error', 'message': 'Madini not found', 'status_code': 404, 'data': []})


@csrf_exempt
def add_madini(request):
    images = request.FILES.getlist('images')
    title = request.POST.get('title')
    content = request.POST.get('content')

    Madini.objects.create(title=title,images=images[0], content=content)
    return JsonResponse({'status': 'success', 'message': 'Madini created successfully', 'status_code': 201,
                         }, status=201)

@csrf_exempt
def edit_madini(request):
    images = request.FILES.getlist('images')
    title = request.POST.get('title')
    content = request.POST.get('content')
    id = request.POST.get('id')

    madini = Madini.objects.get(id=id)
    images_length = len(images)
    madini.content = content
    madini.title = title
    madini.save()
    if images_length > 0:
        madini.images = images[0]
        madini.save()
    return JsonResponse({'status': 'success', 'message': 'Madini updated successfully', 'status_code': 200,
                         }, status=200)