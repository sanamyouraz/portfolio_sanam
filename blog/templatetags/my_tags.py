
from django import template
import re

register = template.Library()



@register.filter
def trimtags(html):
    """Removes all HTML tags from the string."""
    return re.sub(r'<[^>]*>', '', html)


@register.filter
def strip(value):
    """Strips whitespace from start and end of a string."""
    if value:
        return value.strip()
    return value


@register.filter
def trim(value):
    """Alias for strip filter to match template usage."""
    if value:
        return value.strip()
    return value


@register.filter
def multiply(value, arg):
    """Multiplies the value by the argument."""
    return value * arg


