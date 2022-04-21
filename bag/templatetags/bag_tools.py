from django import template


register = template.Library()


#  calculate the subtotal in shopping bag
@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    return price * quantity
