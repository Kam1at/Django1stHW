from django.shortcuts import render


def home(request):
    return render(request, 'pupi/home.html')


def contacts(request):
    if request.method == "POST":
        print(request.POST.get('name'))
        print(request.POST.get('phone'))
        print(request.POST.get('message'))
    return render(request, 'pupi/contacts.html')
