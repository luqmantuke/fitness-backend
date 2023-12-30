from offers.views import *
from paymentorder.views import *
from myauthentication.views import *
from django.urls import path, include
from madini.views import *
from videos.views import *
from  subscription.views import *
urlpatterns = [
    path('webhook_payment_endpoint/', webhook_payment_endpoint),
    path('create_subscription/', create_subscription),
    path('fetch_madini/', fetch_madini),
    path('fetch_banner_images/', fetch_banner_images),
    path('fetch_banner_images/', fetch_banner_images),
    path('fetch_videos/', fetch_videos),
    path('fetch_search_videos/', fetch_search_videos),
    path('fetch_search_madini/', fetch_search_madini),
    path('add_madini/', add_madini),
    path('edit_madini/', edit_madini),
    path('add_video/', add_video),
    path('fetch_subscriptions/', fetch_subscriptions),
    path('fetch_user_subscription/', fetch_user_subscription),
    path('fetch_subscribers/', fetch_subscribers),
    path('fetch_plans/', fetch_plans),
    path('auth/signup/', signup),
    path('auth/delete_user_data/', delete_user_data),
    path('auth/login/', login),
    path('auth/fetch_users/', fetch_users),
    path('auth/change_current_password/', change_current_password),
    path('auth/forget_password_send_otp/', forget_password_send_0TP),
    path('auth/verify_forget_password_otp/', verify_forget_password_otp),
    path('auth/verify_signup_otp/', verify_signup_otp),
    path('auth/change_forget_password/', change_forget_password),
    path('auth/verify_user_send_otp/', verify_user_send_OTP),
    path('rest/', include('rest_framework.urls')),
]