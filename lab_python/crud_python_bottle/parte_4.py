from bottle import jinja2_view, route, run, request, response

@route('/<area>')
@jinja2_view('paginas/teste.html')
def testes(area):
    return dict(nome=area)

@route('/user', method='GET')
@jinja2_view('paginas/user.html')
def user():
    links = ['home', 'about', 'help']
    return dict(links=links)

@route('/user', method='POST')
@jinja2_view('paginas/user.html')
def user_post():
    username = request.forms.get('username')
    password = request.forms.get('password')

    if username == 'eduardo' and password == 'senha' or \
        request.get_cookie('user') == 'eduardo':
        response.set_cookie('user', 'eduardo')
        links = ['home', 'user_space', 'help', 'metrics']

        return dict(string="Voce esta logado", links=links)
    else:
        response.set_cookie('user', 'None')
        return '''
        <h1>Erro ao efetuar login</h1>'''

run(port=8080)