from django.shortcuts import render, HttpResponse

# Create your views here.

# View
# - Class based view
# - Function based view

from .models import Student


def welcome(request):
    # studs = Student.objects.get(id=1)
    # studs = Student.objects.get(id=2)
    # studs = Student.objects.all()
    studs = Student.objects.values("name")
    final_studs = list(map(lambda x: x["name"], studs))

    return HttpResponse(f"Welcome to the Django Application...!!, {final_studs}") 