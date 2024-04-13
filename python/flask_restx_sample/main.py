from flask import Flask
from flask_restx import Resource, Api

app = Flask(__name__)
api = Api(
	title='Time_calculous API 🕒',
	version='1.0',
	description='API to use all of the time_calculous C library'
)

#
api.init_app(app)

@api.route('/wished_week_day_in_choosen_month')
class WishedWdayInChoosenMonth(Resource):
    def get(self):

        """
        Get the wished week day in choosen month
        """

        return {'hello': 'world'}, 200

@api.route('/number_of_weeks_in_a_year_according_to_the_iso_norm')
class NumberWeeksInYearAccordingISONorm(Resource):
    def get(self):

        """
        Get how many weeks there are in the wished year
        """

        return {'hello': 'world'}, 200

if __name__ == '__main__':
    app.run(debug=True)
