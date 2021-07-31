from django import template
from django.utils.timesince import timesince
from django.utils.timezone import now

register = template.Library()


@register.filter("custom_title")
def title_filter(value):
    return value.title()


@register.simple_tag()
def timesince_tag(value):
    """Format a date as the time since that date (i.e. "4 days, 6 hours")."""
    return timesince(value, now=now())
