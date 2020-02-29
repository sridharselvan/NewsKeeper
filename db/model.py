from db.entity import UserEntity
from db.utils import to_dict


class UserModel():

	def create_user(session, **kwargs):
		ins_obj = UserEntity(**kwargs)
		session.add(ins_obj)
		session.flush()
		return ins_obj

	def fetch_user_details(session, email_id):
		query_obj = session.query(
			UserEntity.email_id, 
			UserEntity.hash1
		).filter(UserEntity.email_id == email_id)

		return to_dict(query_obj.all())