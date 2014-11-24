from dcbase.views.profile.profileEdit import ProfileEditFormView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.forms import ModelForm
from django.utils.translation import gettext as _


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']


class ProfileEditUserView(ProfileEditFormView):
    form_class = UserForm
    profile_nav_name = _('User')
    profile_panel_name = _('User Settings')
    profile_edit_url = reverse_lazy('account_profile_edit')

profileEditUserView = login_required(ProfileEditUserView.as_view())

