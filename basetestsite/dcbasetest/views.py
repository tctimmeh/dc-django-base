from django.contrib.auth.decorators import login_required
from django.shortcuts import render


def home(request):
    return render(request, 'dcbasetest/home.html')

@login_required
def authwall(request):
    return render(request, "dcbasetest/authwall.html")