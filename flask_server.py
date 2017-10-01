from flask import Flask, jsonify, request
from datetime import datetime
import time
import psycopg2
import db
from datetime import datetime, timedelta, date, time as dt_time

app = Flask('Locations')

@app.route('/send_data', methods=['GET'])
def write_db():
	user_id = request.args['user_id']
	user_id = int(user_id)
	gps = request.args['gps']
	pulse = request.args['pulse']
	date = datetime.fromtimestamp(time.time())
	if user_id != 66475832 and user_id != 1:
		return jsonify({'error': 'There is no ' + str(user_id) + ' in our database'})
	else:

		connect = psycopg2.connect(database="location_database",host="localhost", user='location_user', password='Par0lka')
		cursor = connect.cursor()

		# cursor.execute("CREATE TABLE tbl(id INT, data JSON);")

		cursor.execute('INSERT INTO %s VALUES (\'%s\',%s,\'%s\');' % ('userid' + str(user_id), gps,pulse,date))
		connect.commit()

		connect.close()
		db.main()
	    # return 'succesfully'



@app.errorhandler(404)
def not_found(error):
	return jsonify({'error': 'Invalid request'})


if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
