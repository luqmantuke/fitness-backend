from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token

from .serializers import SubscriptionSerializer,PlanSerializer
from .models import Subscription,Plan
from myauthentication.models import CustomUser as User


@csrf_exempt
def fetch_subscriptions(request):
    if request.method == 'POST':
        subscription = Subscription.objects.all()
        subscription_serializer = SubscriptionSerializer(subscription, many=True).data
        return JsonResponse(
            {'status': 'success', 'message': 'Subscriptions fetched  successfully',
             'status_code': 200, 'data': list(subscription_serializer)},
            status=200)


@csrf_exempt
def fetch_user_subscription(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        user = User.objects.get(id=user_id)
        subscription = Subscription.objects.get(user=user)
        subscription_serializer = SubscriptionSerializer(subscription,many=False).data
        return JsonResponse(
            {'status': 'success', 'message': 'Subscription fetched  successfully',
             'status_code': 200, 'data': subscription_serializer},
            status=200)

@csrf_exempt
def fetch_plans(request):
    if request.method == 'POST':
        plans = Plan.objects.all()
        plan_serializer = PlanSerializer(plans,many=True).data
        return JsonResponse(
            {'status': 'success', 'message': 'plans fetched  successfully',
             'status_code': 200, 'data': list(plan_serializer)},
            status=200)

@csrf_exempt
def fetch_subscribers(request):
    token_key = request.POST.get('token')

    if token_key:
        try:
            token = Token.objects.get(key=token_key)
            user = token.user
        except Token.DoesNotExist:
            return JsonResponse(
                {'status': 'error', 'message': 'Invalid token.', 'status_code': 401},
                status=401)

        if not user.is_staff:
            return JsonResponse(
                {'status': 'error', 'message': 'Not authorized as an admin.', 'status_code': 401},
                status=401)

        # Token is valid and user is staff
        subscribers = Subscription.objects.filter(active=True)

        subs_serializer = SubscriptionSerializer(subscribers, many=True).data
        return JsonResponse(
            {'status': 'success', 'message': 'Subscribers fetched succesfully.', 'data': list(subs_serializer),
             'status_code': 200}, status=200)

    return JsonResponse(
        {'status': 'error', 'message': 'Token not provided.', 'status_code': 400},
        status=400)