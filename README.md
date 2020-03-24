Create a repo on github or bitbucket, please name it "test".
 
Database to be used: postgresql or mongodb
NOTE: if using postgresql, enable the extensions "cube" and "earthdistance" on postgresql
 
web framework to be used - FastAPI is a new kind of python based api server. Its much simpler than django and much faster.
Here's a tutorial - https://fastapi.tiangolo.com/tutorial/intro/
sqlalchemy database tutorial - https://fastapi.tiangolo.com/tutorial/sql-databases/
 
--------Interview Stage 1--------
create a new table in postgres and load this CSV that denotes the mapping between pincode and lat/long (https://github.com/sanand0/pincode/blob/master/data/IN.csv).
Create Two APIs  : Get,Post.
Post api - /post_location : Post lat,lng of any location with pin code+address+city. This api will add new pin code in db.  
IMPORTANT: Remember to check if pin code already exists or if there are existing latitude+longitude THAT ARE CLOSE ENOUGH TO BE THE SAME (dont assume that they will exactly be the same.)
 
Get api - /get_location : Given lat,lng ... it will fetch pin code, address, city as a json response.
 
Write testcases using pytest.
 
--------Interview Stage 2--------
You will write the following functionality : Given a location, fetch all the nearby pin codes within a radius. For example, I can ask - give me all points within 5km radius of (45.12, 71.12) .
 
To do this you will need to do mathematical computation of radius. there are two ways to do this. So you will create two different api:
1.  /get_using_postgres - You can use postgres "earthdistance" to compute all points in 5km radius
2. /get_using_self - Implement the mathematical computation yourself.  
 
Write testcases using Pytest. Importantly, test+compare results between /get_using_postgres and /get_using_self.
 
--------Interview Stage 3--------
a Geojson is a json file which defines shapes of locations - for example the shape of delhi, gurgaon, etc.
 
https://gist.github.com/ramsingla/6202001?short_path=7d9a995 - This geojson is used to define delhi and its areas.
NOTE: you can check it out by going to http://geojson.io and pasting the raw json on the right side (on tab marked JSON).
 
Write code to parse this json, and load the boundaries latitude and longitude (geometry -> coordinates) into postgresql in a new table. IMPORTANT: you can use any database/table structure ... but remember that one place (like "Delhi") will have lots of lat/long (because it marks the boundaries).
Write a new API "/detect" : It will take input as latitude + longitude, it will tell you which place it falls within.
 
Write testcases.