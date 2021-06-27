from django.shortcuts import render
from time import gmtime, strftime

# Create your views here.
def displayTime(request):
    context = {
        "date": strftime("%b %d, %Y"),
        "time": strftime("%H:%M %p")
    }
    return render(request, "time.html", context)
