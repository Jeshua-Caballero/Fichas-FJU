from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter(name='diccionario')
def get_item(dictionary, key):
    if isinstance(dictionary, dict):
        return mark_safe(dictionary.get(key, ""))
    return ""
