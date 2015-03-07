from dcbase.views.generic.popupFormView import PopupFormMixin, PopupValidAction
from django.core.urlresolvers import reverse
from django.forms import Form, CharField, BooleanField
from django.shortcuts import render
from django.views.generic import FormView


class TestForm(Form):
    text = CharField(max_length=20, help_text="Help!", required=False)
    errors = CharField(max_length=10, required=True)
    option = BooleanField(help_text="It's a good option...", required=False)


def home(request):
    form = TestForm(data={'text': '', 'errors': '', 'option': False})
    form.add_error(None, "Form-level error")
    form.add_error('errors', 'Field error')
    return render(request, 'dcbasetest/home.html', {'form': form})


class PopupForm(PopupFormMixin, FormView):
    form_valid_action = PopupValidAction.redirect
    form_class = TestForm
    dialog_title = 'Test Pop-up AJAX Form'
    submit_style = 'primary'
    submit_text = 'Make it so!'

    def get_success_url(self):
        return reverse('account_email')


popupForm = PopupForm.as_view()

