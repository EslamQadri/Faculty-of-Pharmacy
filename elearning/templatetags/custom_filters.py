from django import template

register = template.Library()

@register.filter(name='custom_replace')
def custom_replace(value, args):
    old, new = args.split(',')
    return value.replace(old.strip(), new.strip())
