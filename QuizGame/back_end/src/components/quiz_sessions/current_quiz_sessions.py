import sys
sys.path.append('G:\\Metropolia\\Metropolia\\2023\\Syksy\\SOFTWARE_2\\PROJECT\\QUIZ_PROJECT\\back_end')
from src.config import dbconfig

connection = dbconfig.connection

def get_all_current_quiz_sessions():
    sql = "select * from current_quiz_session"
    # moreSql = f"{sql} WHERE country.id = city.country AND city.id = player.location"
    # finalSql = f"{sql} AND player.id = {playerId}"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

def get_all_current_quiz_sessions_by_player(player_id):
    sql = "select * from current_quiz_session"
    # moreSql = f"{sql} WHERE country.id = city.country AND city.id = player.location"
    final_sql = f"{sql} WHERE player_id = {player_id}"
    cursor = connection.cursor()
    cursor.execute(final_sql)
    result = cursor.fetchall()
    return result

def insert_new_current_quiz_session(session_id,player_id,question_id,question_option_id,is_correct):
    tables = "session_id, player_id, question_id, question_option_id, is_correct"
    values = f"{session_id},{player_id},{question_id},{question_option_id},{is_correct}"
    
    sql = "INSERT INTO current_quiz_session"
    more_sql = f"{sql} ({tables})"
    final_sql = f"{more_sql} VALUES ({values})"
    cursor = connection.cursor()
    cursor.execute(final_sql)
    print("Insert new current session successfully")
    return

    



if __name__ == "__main__":
    # quiz_sessions = get_all_quiz_sessions()
    # all_closed_quiz_sessions = get_all_closed_quiz_sessions()
    # player_id = 1
    # all_current_quiz_sessions = get_all_current_quiz_sessions()
    # all_current_quiz_sessions_by_player = get_all_current_quiz_sessions_by_player(player_id)
    # print(quiz_sessions)
    # print(all_closed_quiz_sessions)
    # print(all_current_quiz_sessions)
    # print(all_current_quiz_sessions)
    # print(all_current_quiz_sessions_by_player)
    insert_new_current_quiz_session(1,1,3,20,0)