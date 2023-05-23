from django import template
from django.utils import timezone
from django.utils.timesince import timesince
from django.utils.translation import gettext as _

register = template.Library()

@register.filter
def twitter_time(value):
    """
    Formats a date as the time since that date (e.g. "4 hours ago").
    For dates older than 7 days, displays the date in the format "M d".
    """
    if value is None:
        return ''

    now = timezone.now()
    diff = now - value

    if diff.days >= 7:
        return value.strftime('%b %d')
    elif diff.days > 0:
        return _('%(count)sd') % {'count': diff.days}
    elif diff.seconds >= 3600:
        return _('%(count)sh') % {'count': diff.seconds // 3600}
    elif diff.seconds >= 60:
        return _('%(count)sm') % {'count': diff.seconds // 60}
    else:
        return _('now')