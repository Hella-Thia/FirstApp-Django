from django.http import HttpResponse

def Home(request):
    return HttpResponse("Hey there home")