from db.model import UserModel
from db.utils import AutoSession
from flask import session


def create_user(session, **kwargs):
	form_data = kwargs['form_data']
	_user = UserModel.create_user(session, **form_data)
	return {'result': True}

def authenticate_user(**kwargs):
	email_id = kwargs['email_id']
	hash1 = kwargs['password']
	with AutoSession() as db_session:
		user_details = UserModel.fetch_user_details(db_session, email_id)

	response_dict = {'result': False}
	if user_details and user_details[0]['email_id'] == email_id and user_details[0]['hash1'] == hash1:
		session['item'] = user_details[0]
		response_dict = {'result': True, 'is_session_valid': True}

	return response_dict

def get_user_details(*args, **kwargs):
	import pdb;pdb.set_trace()
	response_dict = kwargs
	response_dict['data'] = session['item']
	return response_dict