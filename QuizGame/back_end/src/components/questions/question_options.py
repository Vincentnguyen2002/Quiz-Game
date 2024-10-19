import sys
sys.path.append('G:\\Metropolia\\Metropolia\\2023\\Syksy\\SOFTWARE_2\\PROJECT\\new_backend\\src')
from src.config import dbconfig
# sys.path.append('G:\\Metropolia\\Metropolia\\2023\\Syksy\\SOFTWARE_2\\PROJECT\\QUIZ_PROJECT\\back_end')
# from src.config import dbconfig

connection = dbconfig.connection

def get_all_options():
    sql = "select * from quiz_question_option"
    # moreSql = f"{sql} WHERE country.id = city.country AND city.id = player.location"
    # finalSql = f"{sql} AND player.id = {playerId}"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

def get_options_by_question_id(question_id):
    sql = f"SELECT * from quiz_question_option"
    sql_result = f"{sql} WHERE quiz_question_id = '{question_id}'"
    # print(sql_result)
    cursor = connection.cursor()
    cursor.execute(sql_result)
    result = cursor.fetchall()
    return result

def get_option_by_option_id(option_id):
    sql = f"SELECT * from quiz_question_option"
    sql_result = f"{sql} WHERE id = '{option_id}'"
    # print(sql_result)
    cursor = connection.cursor()
    cursor.execute(sql_result)
    result = cursor.fetchall()
    return result


def option_is_correct(option):
    is_correct =  option[0][3]
    if is_correct == 1:
        return True
    else:
        return False
    

if __name__ == "__main__":
    options = get_all_options()
    options_by_question = get_options_by_question_id(1)
    option1 = get_option_by_option_id(20)
    print(option1)
    print(option_is_correct(option1))
