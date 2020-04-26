from bottle import request, route, run, response

@route('/')
def hello_again():
    if request.get_cookie('visited'):
        return 'Olá, bem vindo de volta'
    response.set_cookie('visited', 'yes')
    return 'Olá, é um prezer conhecer voce.'
run(port=8080)