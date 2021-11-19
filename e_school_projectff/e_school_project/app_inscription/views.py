from django.shortcuts import render

# Create your views here.
def home_index(request, templates_name="app_inscri/index.html"):
    return render(request,templates_name)

def list_view(request, templates_name="app_inscri/list.html"):
    return render(request,templates_name)