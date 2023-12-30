from django.db.models import Q, Case, When
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .serializers import *
from .models import *


# Create your views here.

@csrf_exempt
def fetch_videos(request):
    videos = Videos.objects.all()
    videos_serializer = VideoSerializer(videos, many=True).data
    return JsonResponse({'status': 'success', 'message': 'Videos fetched successfully', 'status_code': 200,
                         'data': list(videos_serializer)})


# fetch search part
@csrf_exempt
def fetch_search_videos(request):
    search_query = request.POST.get('search_query')
    video = Videos.objects.filter(Q(title__icontains=search_query))
    if video.exists():

        video_serializer = VideoSerializer(video, many=True).data

        return JsonResponse({'status': 'success', 'message': 'video search successfully', 'status_code': 200,
                             'data': list(video_serializer)}, status=200)
    else:
        return JsonResponse({'status': 'error', 'message': 'Video not found', 'status_code': 404, 'data': []})

@csrf_exempt
def add_video(request):
    images = request.FILES.getlist('images')
    title = request.POST.get('title')
    content = request.POST.get('video_url')

    Videos.objects.create(title=title,images=images[0], video_url=content)
    return JsonResponse({'status': 'success', 'message': 'Video created successfully', 'status_code': 201,
                         }, status=201)

