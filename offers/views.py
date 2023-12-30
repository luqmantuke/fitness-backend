from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import BannerImages
from .serializers import BannerImageSerializer


# Create your views here.

@csrf_exempt
def fetch_banner_images(request):
    banner_images = BannerImages.objects.all()
    banner_images_serializer = BannerImageSerializer(banner_images, many=True).data
    return JsonResponse({'status': 'success', 'message': 'Car Engines fetched successfully', 'status_code': 200,
                         'data': list(banner_images_serializer)}, status=200)
