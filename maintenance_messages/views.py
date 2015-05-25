from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from django.contrib.auth.models import User
from maintenance_messages.models import Maintenance_Message
from django.utils import timezone
from django.contrib.auth.decorators import login_required

# Create your views here.


def get(request, domain):

    now = timezone.now()
    messages = Maintenance_Message.objects.filter(domain__startswith=domain,
                                                  start_date__lte=now,
                                                  end_date__gte=now)
    output = ""

    for message in messages:
        output += str(message)

    return HttpResponse("Hello, world." + output)


def delete(request):
    pass


def create(request):
    try:
        user = User.objects.filter(username__startswith=request.POST['user'])[0]

        message = Maintenance_Message(domain=request.POST['domain'],
                                      message=request.POST['message'],
                                      owner=user,
                                      start_date=request.POST['start_date'],
                                      end_date=request.POST['end_date'],
                                      create_date=timezone.now())
        message.save()
        return HttpResponse()
    except Exception as exception:
        print exception
        return HttpResponseBadRequest()


@login_required(login_url='/login/')
def index(request):

    messages = Maintenance_Message.objects.all().order_by('domain', 'start_date')

    try:
        user = User.objects.filter(username__startswith=request.POST['user'])[0]

        message = Maintenance_Message(domain=request.POST['domain'],
                                      message=request.POST['message'],
                                      owner=user,
                                      start_date=request.POST['start_date'],
                                      end_date=request.POST['end_date'],
                                      create_date=timezone.now())
        try:
            message.save()
            return render(request, 'maintenance_messages/index.html', {
                'info_message': "Created correctly.",
                'messages': messages,
            })
        except Exception as exception:
            print exception
            return render(request, 'maintenance_messages/index.html', {
                'error_message': "Couldn't create.",
                'messages': messages,
            })
    except Exception as exception:
        print exception
        return render(request, 'maintenance_messages/index.html', {
            'messages': messages,
        })
