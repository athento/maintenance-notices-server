import urllib
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from django.contrib.auth.models import User
import simplejson as simplejson
from maintenance_messages.models import Maintenance_Message
from django.utils import timezone
from django.contrib.auth.decorators import login_required

# Create your views here.


def json_response(func):
    """
    A decorator that takes a view response and turns it
    into json. If a callback is added through GET or POST
    the response is JSONP.
    """
    def decorator(request, *args, **kwargs):
        objects = func(request, *args, **kwargs)
        if isinstance(objects, HttpResponse):
            return objects
        try:
            data = simplejson.dumps(objects)
            if 'callback' in request.REQUEST:
                # a jsonp response!
                data = '%s(%s);' % (request.REQUEST['callback'], data)
                return HttpResponse(data, "text/javascript")
        except Exception as exception:
            print exception
            data = simplejson.dumps(str(objects))
        return HttpResponse(data, "application/json")
    return decorator


@json_response
def get(request, domain):

    now = timezone.now()
    messages = Maintenance_Message.objects.filter(domain__iexact=urllib.unquote(domain).decode('utf8'),
                                                  start_date__lte=now,
                                                  end_date__gte=now)
    output = ""

    for message in messages:
        output += message.message

    return {'html': output}


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
        delete_id = next(v for k, v in request.POST.items() if 'id' in k)
        message = Maintenance_Message.objects.filter(id=delete_id)
        message.delete()

        return render(request, 'maintenance_messages/index.html', {
            'info_message': "Deleted correctly with id: "+str(request.POST['id']),
            'messages': messages,
        })
    except Exception as exception:
        print exception
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



