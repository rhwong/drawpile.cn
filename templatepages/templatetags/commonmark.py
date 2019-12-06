from django import template
from django.utils.safestring import mark_safe

import commonmark

register = template.Library()

@register.filter()
def commonmark_safe(text):
    ast = commonmark.Parser().parse(text)
    html = commonmark.HtmlRenderer({'safe': True}).render(ast)
    return mark_safe(html)


@register.filter()
def commonmark_full(text):
    return mark_safe(commonmark.commonmark(text))
