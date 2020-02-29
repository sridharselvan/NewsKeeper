from flask import request
from . import routes
from db.utils import AutoSession
from api.user import create_user, authenticate_user

route = routes.route

@route('/add_user', methods=['POST'])
def add_user():
	payload = {}
	payload['form_data'] = request.get_json()
	with AutoSession() as session:
		return create_user(session, **payload)

@route('/sign_in', methods=['POST'])
def sign_in():
	form_data = request.get_json()
	return authenticate_user(**form_data)