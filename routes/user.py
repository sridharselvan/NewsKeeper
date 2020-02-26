from flask import request
from . import routes

@routes.route('/add_user', methods=['POST'])
def add_user():
	form_data = request.get_json()
	return {'msg': 'ok'}