from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import NameForm
from main import get_trigger, get_progress, get_exercise, get_comm, get_med

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            #result = int(form.cleaned_data['first_number']) + int(form.cleaned_data['second_number']);
            
            exercise = get_exercise(['exercise1', form.cleaned_data['exercise2'], form.cleaned_data['exercise3'], form.cleaned_data['exercise4'], form.cleaned_data['exercise5']])
            progress = get_progress(['prog1', 'prog2', 'prog3', 'prog4', 'prog5'])
            communication = get_comm(form.cleaned_data['com'], [form.cleaned_data['com1'], form.cleaned_data['com2'], form.cleaned_data['com3'], form.cleaned_data['com4'], form.cleaned_data['com5']]) 
            medication = get_med('med', ['med1', 'med2', 'med3', 'med4', 'med5'])

            result = get_trigger('risk', exercise + progress + communication + medication)
            return render(request, 'results.html', {'result': result})
            # return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else
        form = NameForm()

    return render(request, 'name.html', {'form': form})