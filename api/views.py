from dal import autocomplete
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from .forms import SubmissionForm

def choose(request):
    if request.method == "POST":
        form = SubmissionForm(data=request.POST)
        if form.is_valid():
            form.save()
            character = form.cleaned_data.get('character')
            return redirect('/api/character?name={}'.format(character))
            pass
    else:
        form = SubmissionForm()
    return render(request, 'choose.html', {'form': form})