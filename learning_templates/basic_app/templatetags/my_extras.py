from django import template

register = template.Library()


@register.filter
def slices(value):
    """
    This cuts out all values of "arg" from the string!
    """

    return value.upper()

# register.filter('slices',slices)
