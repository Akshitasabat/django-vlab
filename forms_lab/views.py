from django.shortcuts import render
from .forms import StudentForm


def home(request):
    return render(request, "forms_lab/home.html")


def simulation(request):

    if request.method == "POST":

        form = StudentForm(request.POST)

        if form.is_valid():
            cleaned_data = form.cleaned_data
        else:
            cleaned_data = None

    else:

        form = StudentForm()
        cleaned_data = None

    return render(
        request,
        "forms_lab/simulation.html",
        {
            "form": form,
            "cleaned_data": cleaned_data
        }
    )