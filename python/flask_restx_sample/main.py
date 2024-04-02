from flask import Flask
from flask_restx import Resource, Api

app = Flask(__name__)
api = Api(
	title='Time_calculous API 🕒',
	version='1.0',
	description=''
)

#
api.init_app(app)

@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

if __name__ == '__main__':
    app.run(debug=True)
