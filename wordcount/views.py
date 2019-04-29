from django.http import HttpResponse
from django.shortcuts import render


def home(requests):
    return render(requests, 'home.html')


def main(requests):
    val = requests.POST
    print(val)
    return render(requests, 'main.html', {'val': val})
