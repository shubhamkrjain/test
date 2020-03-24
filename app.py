#from flask import Flask, jsonify , request
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask import render_template, redirect, url_for
from app import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:jimmy@localhost/geolocation'
db = SQLAlchemy(app)

class GeoLocation(db.Model):
	key=db.Column(db.String(9), primary_key=True)
	place_name=db.Column(db.String(30), unique=False)
	admin_name1=db.Column(db.String(30), unique=False)
	latitude=db.Column(db.Float(asdecimal=True), unique=False)
	longitude=db.Column(db.Float(asdecimal=True), unique=False)
	accuracy=db.Column(db.Integer, unique=False)
	
	def __init__(self, key, place_name, admin_name1, latitude, longitude, accuracy):
		self.key=key
		self.place_name=place_name
		self.admin_name1=admin_name1
		self.latitude=latitude
		self.longitude=longitude
		self.accuracy=accuracy
		
	def __repr__(self):
		return '<Pincod %r>' % self.key

@app.route('/')
def index():
	return render_template('add_geolocation.html')

@app.route('/post_location', methods=['POST'])
def post_user():
	geoLoc = GeoLocation(request.form['key'],request.form['place_name'],request.form['admin_name1'],request.form['latitude'],request.form['longitude'],request.form['accuracy'])
	exists = GeoLocation.query.filter_by(key=request.form['key']).first()
	#print(exists)
	if(exists == None):
		db.session.add(geoLoc)
		db.session.commit()	
		return "<p>Pincode is insert in database.</p>"
	else:
		return "<p>Pincode is already insert in database !</p>"
		
@app.route('/get_using_self', methods=['GET', 'POST'])
def get_using_self():
	if request.method == "POST":
		geo_location_data = db.engine.execute('select * from ( SELECT  *,( 3959 * acos( cos( radians(6.414478) ) * cos( radians( '+request.form['latitude']+' ) ) * cos( radians( '+request.form['longitude']+' ) - radians(12.466646) ) + sin( radians(6.414478) ) * sin( radians( '+request.form['latitude']+' ) ) ) ) AS distance FROM geo_location ) al where distance < 5 ORDER BY distance;')
		db.session.commit()
		return render_template('find_pincode.html',geo_locations=geo_location_data)
	return render_template('find_pincode.html')
		
if __name__ == "__main__":
     # Check the System Type before to decide to bind
     # If the system is a Linux machine -:) 
     app.run()