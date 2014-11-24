from django.core.urlresolvers import reverse, reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import UpdateView


class NavLink(object):
    def __init__(self, name, url):
        self.name = name
        self.url = url

class ProfileEditor(object):
    @classmethod
    def add_profile_edit_context(cls, context, navName, panelName):
        navLinks = (
            NavLink(_('User'), reverse('account_profile_edit')),
            NavLink(_('Change Password'), reverse('account_change_password')),
            NavLink(_('Update Email'), reverse('account_email')),
            NavLink(_('Update Social Accounts'), reverse('socialaccount_connections')),
        )
        context['profileNavLinks'] = navLinks
        context['selectedProfileNavLink'] = navName
        context['profilePanelHeading'] = panelName

class ProfileEditFormView(UpdateView):
    template_name = 'dcbase/profile_edit.html'
    form_class = None
    profile_nav_name = 'UNKNOWN PROFILE SETTINGS'
    profile_panel_name = 'UNKNOWN PROFILE SETTINGS'
    profile_edit_url = reverse_lazy('account_profile_edit')

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        ProfileEditor.add_profile_edit_context(kwargs, self.profile_nav_name, self.profile_panel_name)
        return kwargs

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        return self.profile_edit_url

