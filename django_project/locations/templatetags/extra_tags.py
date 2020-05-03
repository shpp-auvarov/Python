from django import template

register = template.Library()


@register.filter
def slice(value, count_symbols=100):
    if len(value) > count_symbols:
        return value[0:count_symbols - 3] + '...'
    return value
