from db.model import UserModel
from db.utils import AutoSession


def create_user(session, **kwargs):
	form_data = kwargs['form_data']
	_user = UserModel.create_user(session, **form_data)
	return {'result': True}

def authenticate_user(**kwargs):
	email_id = kwargs['email_id']
	hash1 = kwargs['password']
	with AutoSession() as session:
		user_details = UserModel.fetch_user_details(session, email_id)

	response_dict = {'result': False}
	if user_details and user_details[0]['email_id'] == email_id and user_details[0]['hash1'] == hash1:
		response_dict = {'result': True}

	return response_dict