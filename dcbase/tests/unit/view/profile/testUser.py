from dcbase.tests.unit import UnitTestCase
from django.core.urlresolvers import reverse


class TestUserView(UnitTestCase):
    def setUp(self):
        super().setUp()
        self.user = self.createUser()
        self.url = reverse('account_profile_user', kwargs={'username': self.user.username})

    def test_rendersProfileTemplate(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, 'dcbase/profile.html')

