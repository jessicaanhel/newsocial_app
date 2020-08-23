from django.template import Library
from django.utils.html import escape
from django.utils.safestring import SafeString

register = Library()


@register.simple_tag
def service_format(service, short=False):
    if short:
        return f'{service.title} ({service.price})'
    return f'{service.title} ({service.price}) - {service.city}'


@register.simple_tag
def basket_format(basket, short=False):
    if short:
        return f'{basket.buyer} ({basket.id_service})'
    return f'{basket.buyer} ({basket.ilosc}) - {basket.id_service}'

@register.filter
def attr_as_p(obj, attrname):
    label = escape(attrname.capitalize())
    value = escape(getattr(obj, attrname))
    return SafeString(f'<p><strong>{label}:</strong>{value}</p>')
