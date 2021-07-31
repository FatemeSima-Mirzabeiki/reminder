from django import template
from django.utils.timesince import timesince, timeuntil
from django.utils.timezone import now

register = template.Library()


@register.filter("custom_title")
def title_filter(value):
    return value.title()


@register.simple_tag()
def t_tag(value, arg=now()):
    """Format a date as the time until that date (i.e. "4 days, 6 hours")."""
    if not value:
        return ''
    try:
        if value < now():
            return f'- {str(timeuntil(arg, value))}'
        return timeuntil(value, arg)
    except (ValueError, TypeError):
        return ''
