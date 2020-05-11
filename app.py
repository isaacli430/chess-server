from sanic import Sanic
from sanic.response import html
from sanic import response

from jinja2 import Environment, PackageLoader

env = Environment(loader=PackageLoader('app', 'templates'))

app = Sanic(__name__)

app.static('static', './static')

# theres gotta be a better way to do this
bootstrap_css = app.url_for('static', filename='/vendors/bootstrap.min.css')
bootstrap_js = app.url_for('static', filename='/vendors/bootstrap.min.js')
jquery_js = app.url_for('static', filename='/vendors/jquery-3.3.1.min.js')
jquery_ui_css = app.url_for('static', filename='/vendors/jquery-ui.min.css')
jquery_ui_js = app.url_for('static', filename='/vendors/jquery-ui.min.js')
popper_js = app.url_for('static', filename='/vendors/popper.min.js')
socket_js = app.url_for('static', filename='/vendors/socket.io.js')
game_js = app.url_for('static', filename='game.js')

@app.route('/', methods=["POST","GET"])
async def index(request):
    if request.method == 'POST':
        game_url = app.url_for('game', room='123')
        return response.redirect(game_url)
    else:
        template = env.get_template('index.html')
        html_content = template.render()
        return html(html_content)

@app.route('/game/<room>')
async def game(request, room):
    print(room)
    template = env.get_template('game.html')
    html_content = template.render(jquery_js=jquery_js, popper=popper_js, bootstrap_js=bootstrap_js, socket=socket_js, jquery_ui_js=jquery_ui_js, game=game_js, room=room)
    return html(html_content)


app.run(host="0.0.0.0", port=8000)