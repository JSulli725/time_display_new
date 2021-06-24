from django.shortcuts import render
from time import gmtime, strftime

# Create your views here.
def displayTime(request):
    context = {
        "time": strftime("%b %d, %Y %H:%M %p")
    }
    return render(request, "time.html", context)
