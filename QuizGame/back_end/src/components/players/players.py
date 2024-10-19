import sys
sys.path.append('G:\\Metropolia\\Metropolia\\2023\\Syksy\\SOFTWARE_2\\PROJECT\\QUIZ_PROJECT\\back_end')
from src.config import dbconfig


connection = dbconfig.connection


def convert_name(name):
    
    new_name = name.lower()
    result_name = new_name.strip()
    return result_name


def is_name_exist(name_data):
    
    if len(name_data) != 0:
        return True
    else:
        return False


def get_players():
    
    sql = "select * from player"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    return result


def insert_new_player(name):
    
    converted_name = convert_name(name)
    sql = "INSERT INTO player (name)"
    final_sql=f"{sql} VALUES ('{converted_name}')"
    cursor = connection.cursor()
    cursor.execute(final_sql)
    print("Insert new player successfully")
    return


def get_player_by_name(name):
    
    converted_name = convert_name(name)
    sql = "SELECT * from player"
    final_sql = sql + f" WHERE name = '{converted_name}'"
    cursor = connection.cursor()
    cursor.execute(final_sql)
    result = cursor.fetchall()
    return result


def get_player_by_player_id(player_id):
    sql = "SELECT * from player"
    final_sql = sql + f" WHERE id = {player_id}"
    # print(final_sql)
    cursor = connection.cursor()
    cursor.execute(final_sql)
    result = cursor.fetchall()
    
    return result


if __name__ == "__main__":
    
    # players = get_players()
    # name1_data = get_player_by_name("hoa")
    # # insert_new_player("trung2")
    # trung2 = get_player_by_name("trung2")
    print(get_player_by_player_id(1))