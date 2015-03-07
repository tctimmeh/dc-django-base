from django.contrib import messages
from django.core.urlresolvers import reverse
from django.forms import Form, CharField, BooleanField
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render

class TestForm(Form):
    text = CharField(max_length=20, help_text="Help!", required=False)
    errors = CharField(max_length=10, required=True)
    option = BooleanField(help_text="It's a good option...", required=False)

def home(request):
    form = TestForm(data={'text': '', 'errors': '', 'option': False})
    form.add_error(None, "Form-level error")
    form.add_error('errors', 'Field error')
    return render(request, 'dcbasetest/home.html', {'form': form})

def popupForm(request):
    if request.method == 'POST':
        form = TestForm(request.POST)
        if form.is_valid():
            return JsonResponse({'action': 'reload'})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = TestForm()

    messages.success(request, "Example non-form message!")
    return render(request, 'dcbase/form/popup-form.html', {
        'form': form, 'form_url': reverse('popupAjaxForm'),
        'dialog_title': 'Test Pop-up AJAX Form',
        'submit_text': 'Make it so!',
        'submit_style': 'info',
    })
