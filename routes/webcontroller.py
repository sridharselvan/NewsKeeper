from flask import request
from . import routes
from db.utils import AutoSession
from api.user import create_user, authenticate_user, get_user_details
from routes.route_utils import common_route

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

@route('/get_user', methods=['GET'])
@common_route
def get_user(*args, **kwargs):
	return get_user_details(*args, **kwargs)