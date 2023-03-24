from django import template

register = template.Library()

@register.filter
def get_hours_worked(obj):
    return obj.hours_worked()


