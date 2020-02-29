import os
from flask import Flask, session
from routes import *

app = Flask(__name__, static_url_path='/') 
app.static_folder="static"
app.register_blueprint(routes)
app.secret_key = "secret_key"

@app.route('/', defaults={'path': 'index'}, methods=['GET', 'POST'])
@app.route('/<path:path>.html', methods=['GET', 'POST'])
def views(path):
    html_path = 'htmls/{}.html'.format(path)
    return app.send_static_file(html_path)

# @app.before_request
# def do_something_whenever_a_request_comes_in():
#     session_obj = session.get('item', '')
#     import pdb;pdb.set_trace()
#     if not session_obj:
#         return {'is_session_valid' : False}

if __name__ == '__main__':
    app.run(port=4770, debug=True)
