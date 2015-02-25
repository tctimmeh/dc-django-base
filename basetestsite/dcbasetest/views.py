from django.forms import Form, CharField, BooleanField
from django.shortcuts import render

class TestForm(Form):
    text = CharField(max_length=20, help_text="Help!", required=False)
    errors = CharField(max_length=10, required=False)
    option = BooleanField(help_text="It's a good option...", required=False)

def home(request):
    form = TestForm(data={'text': '', 'errors': '', 'option': False})
    form.add_error(None, "Form-level error")
    form.add_error('errors', 'Field error')
    return render(request, 'dcbasetest/home.html', {'form': form})

