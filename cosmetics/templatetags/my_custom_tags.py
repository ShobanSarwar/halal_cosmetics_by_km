from django import template

register = template.Library()


@register.simple_tag
def media_url():
    return 'my practice/halal_cosmetics_by_km/media/'
