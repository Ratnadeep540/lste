from django.shortcuts import render

# Create your views here.
def meme(request):
    return render(request,"meme.html")