from allauth.socialaccount.views import ConnectionsView
from dcbase.views.profile.profileEdit import ProfileEditor
from django.contrib.auth.decorators import login_required
from django.utils.translation import gettext as _


class ProfileEditSocialView(ConnectionsView):
    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        ProfileEditor.add_profile_edit_context(kwargs, _('Update Social Accounts'), _('Social Account Connections'))
        return kwargs

profileEditSocialView = login_required(ProfileEditSocialView.as_view())
