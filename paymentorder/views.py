import json
from datetime import timedelta, date

import requests
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from subscription.models import Subscription, Plan
from utilities.send_sms import send_sms_message

url = "https://swahiliesapi.invict.site/Api"


@csrf_exempt
def webhook_payment_endpoint(request):
    # Read the raw request body
    request_body = request.body
    data = json.loads(request_body)
    order_id = data['transaction_details']['order_id']
    amount_paid = data['transaction_details']['amount']
    reference_id = data['transaction_details']['reference_id']
    subscription = Subscription.objects.get(id=order_id)
    plan = Plan.objects.get(price=amount_paid)
    user = subscription.user
    if plan.price >= amount_paid:
        subscription.active = True
        subscription.plan = plan
        today = date.today()
        subscription.end_date = today + timedelta(days=plan.duration)
        subscription.save()
        numbers = ['255676372280', '255758585847']
        message = f'{user.username} mwenye namba {user.phone_number} amelipia kifurushi cha {plan.name} Tzs {amount_paid}.'
        for number in numbers:
            send_sms_message(number, message)
    print(f'WEBHOOK PAYMENT: {data}')
    return JsonResponse({'status': 'Successfully paid', 'data': data}, )


def make_payment(order_id, amount, phone_number):
    payload = json.dumps({
        "api": 170,
        "code": 104,
        "data": {
            "api_key": "YzA3YThmMTc1MTMzNDFjZWI3NDRiYWJhYzU0OWE4YTM=",
            "order_id": order_id,
            "amount": amount,
            "username": "OmmyFitness",
            "is_live": True,
            "phone_number": phone_number,
            "webhook_url": "https://ommyfitness.fxlogapp.com/api/webhook_payment_endpoint/",

        }
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)
    return response.text


@csrf_exempt
def create_subscription(request):
    user_id = request.POST.get('user_id')
    amount = request.POST.get('amount')
    phone_number = request.POST.get('phone_number')

    try:
        subscription = Subscription.objects.get(user_id=user_id)
        make_payment_response = make_payment(subscription.id, amount, phone_number)

        parsed_json = json.loads(make_payment_response)

        status_code = parsed_json['code']
        if status_code == 200:

            return JsonResponse({'status': 'success', 'message': 'Pushed wallet successfully', 'status_code': 200})
        else:
            return JsonResponse({'status': 'error', "message": 'Failed to push wallet', 'status_code': 400})
    except ObjectDoesNotExist:
        current_date = timezone.now().date()
        subscription = Subscription.objects.create(user_id=user_id, plan_id=1, start_date=current_date,
                                                       end_date=current_date, )
        make_payment_response = make_payment(subscription.id, amount, phone_number)

        parsed_json = json.loads(make_payment_response)

        status_code = parsed_json['code']
        if status_code == 200:

            return JsonResponse({'status': 'success','message': 'Pushed wallet successfully', 'status_code': 200})
        else:
            return JsonResponse({'status': 'error', "message": 'Failed to push wallet', 'status_code': 400})
        return None
