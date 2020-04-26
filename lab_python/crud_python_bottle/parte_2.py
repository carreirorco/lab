from bottle import route, run, request

@route('/', method='GET')
def index_get():
    return '''
    <form action="/" method="post">
        Username: <input name="username" type="text" /></br>
        Password: <input name="password" type="password" /></br>
        <input value="Login" type="submit">
    </form>
    '''

@route('/', method='POST')
def index_post():
    username = request.forms.get('username')
    password = request.forms.get('password')
    return '''
    <h1>Suas informações: </h1></br>
    <h4>{}</h4>
    <h4>{}</h4>'''.format(username, password)
run(port=8080)