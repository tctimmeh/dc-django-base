from dcbase.apps import TIMEZONE_SESSION_KEY
from django.utils import timezone


class DcBaseMiddleware(object):
    def process_request(self, request):
        timezone_name = request.session.get(TIMEZONE_SESSION_KEY)
        if timezone_name is not None:
            timezone.activate(timezone_name)
        else:
            timezone.deactivate()
