import sys
sys.path.append('G:\\Metropolia\\Metropolia\\2023\\Syksy\\SOFTWARE_2\\PROJECT\\QUIZ_PROJECT\\back_end')
from src.config import dbconfig
connection = dbconfig.connection

def get_cities():
    sql = "select * from city"
    # moreSql = f"{sql} WHERE country.id = city.country AND city.id = player.location"
    # finalSql = f"{sql} AND player.id = {playerId}"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

def get_city_by_id(city_id):
    sql = f"SELECT * from city"
    sql_result = f"{sql} WHERE id = {city_id}"
    # print(sql_result)
    cursor = connection.cursor()
    cursor.execute(sql_result)
    result = cursor.fetchall()
    return result

def get_city_by_name(city_name):
    sql = f"SELECT * from city"
    sql_result = f"{sql} WHERE name = '{city_name}'"
    # print(sql_result)
    cursor = connection.cursor()
    cursor.execute(sql_result)
    result = cursor.fetchall()
    return result


if __name__ == "__main__":
    citi_name = "Helsinki"
    # cities = get_cities()
    # city1 = get_city_by_id(1)
    city2 = get_city_by_name(citi_name)
    print(city2)
    # print(cities)



# G:/Metropolia/Metropolia/2023/Syksy/SOFTWARE_2/PROJECT/Quiz_Project/back_end/src