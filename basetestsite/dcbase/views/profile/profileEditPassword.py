from allauth.account.views import PasswordChangeView
from dcbase.views.profile.profileEdit import ProfileEditor
from django.contrib.auth.decorators import login_required
from django.utils.translation import gettext as _


class ProfileEditPasswordView(PasswordChangeView):
    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        ProfileEditor.add_profile_edit_context(kwargs, _('Change Password'), _('Change Password'))
        return kwargs

profileEditPasswordView = login_required(ProfileEditPasswordView.as_view())
