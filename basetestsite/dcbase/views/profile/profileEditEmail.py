from allauth.account.views import EmailView
from dcbase.views.profile.profileEdit import ProfileEditor
from django.contrib.auth.decorators import login_required
from django.utils.translation import gettext as _


class ProfileEditEmailView(EmailView):
    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        ProfileEditor.add_profile_edit_context(kwargs, _('Update Email'), _('Email Addresses'))
        return kwargs

profileEditEmailView = login_required(ProfileEditEmailView.as_view())
