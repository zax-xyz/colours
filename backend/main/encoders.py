from datetime import datetime

from django.core.serializers.json import DjangoJSONEncoder


class TimeEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%-d %b %H:%M:%S')