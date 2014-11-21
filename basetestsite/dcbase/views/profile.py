from django.views.generic import View, TemplateView


class ProfileView(TemplateView):
    template_name = 'dcbase/profile.html'

profileView = ProfileView.as_view()
