from django.template import Library

register=Library()

def filtro(total):
    return str(total+1)

register.filter("filtro",filtro)