"""
Breve introdução sobre rotas estáticas e dinamicas
"""

from bottle import run, route

@route('/')
def index():
    """Rota estática"""
    return "<h1>Hello!</h1>"

@route('/<person>')
def teste(person):
    """Rota dinamica"""
    if person == 'charles':
        return 'Flw mano!'
    return "<h1>Olá {}!</h1>".format(person)

run(port=8080)