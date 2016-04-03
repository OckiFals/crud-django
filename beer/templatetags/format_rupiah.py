__author__ = 'returnFALSE'

from django import template
register = template.Library()

@register.simple_tag
def format_rupiah(value):
    val = '{:10,}'.format(int(value))
    return 'Rp. ' + val.replace(',', '.') + ',-'