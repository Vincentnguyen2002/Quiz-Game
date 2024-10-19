
# In order to turn the object into Json object, I created methods for that purpose that is applicable to a flask program
# that will serve as an endpoint for flask to return a json reponse when a user go to a world map page.




 # fetches the location from the database

def get_location(location_id):
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor(dictionary=True)

    cursor.execute(
        'SELECT city.name as city, city.id as city_id, city.country_id, country.name as country, city_location.longitude, city_location.latitude '
        'FROM city '
        'JOIN country ON city.country_id = country.id '
        'WHERE city.id = %s', (location_id,)
    )
    location_data = cursor.fetchone()

    cursor.close()
    connection.close()

    return location_data


# turns it into a JSON object.

def transform_location(location_data):
    if location_data:
        response_object = {
            'city': location_data['city'],
            'Coordinate': {
                'longitude': location_data['longitude'],
                'latitude': location_data['latitude']
            }
        }
        return response_object
    else:
        return None
