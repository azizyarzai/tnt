from django.shortcuts import render, HttpResponse

# Create your views here.


def welcome(request):
    # return HttpResponse("Welcome to Django")
    name = "Amin"
    context = {"name": name, "title": "TEst 2"}
    print(request.path)

    return render(request, 'index.html', context)
