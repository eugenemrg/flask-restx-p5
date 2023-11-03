from flask_restx import Resource, Namespace
from .api_models import user_profile_model, user_history_model
from .models import SearchHistory, User

profile_ns = Namespace('profile', description='Create, update or delete user profile')
login_ns = Namespace('login', description='Handle user log in')
history_ns = Namespace('history', description='Get, update or delete user history')

@profile_ns.route('')
class Profile(Resource):
    @profile_ns.marshal_list_with(user_profile_model)
    def get(self):
        return User.query.all()
    
@login_ns.route('')
class Login(Resource):
    def get(self):
        return {'msg': 'test login'}
    
@history_ns.route('')
class History(Resource):
    @history_ns.marshal_list_with(user_history_model)
    def get(self):
        return SearchHistory.query.all()