from django.shortcuts import render, redirect
from .forms import RegistrationForm


def index(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    form = RegistrationForm()
    context = {
        'form': form
    }

    return render(request, 'main/index.html', context)


def persar(request):
    return render(request, 'main/personal_area.html')


def archive(request):
    return render(request, 'main/archive.html')


def forum(request):
    return render(request, 'main/forum.html')


def consult(request):
    return render(request, 'main/consultations.html')




