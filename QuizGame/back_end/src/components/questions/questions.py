import sys
sys.path.append('G:\\Metropolia\\Metropolia\\2023\\Syksy\\SOFTWARE_2\\PROJECT\\new_backend\\src')
from src.config import dbconfig
sys.path.append('G:\\Metropolia\\Metropolia\\2023\\Syksy\\SOFTWARE_2\\PROJECT\\QUIZ_PROJECT\\back_end')
from src.config import dbconfig
# from 
connection = dbconfig.connection

def get_questions():
    sql = "select * from quiz_question"
    # moreSql = f"{sql} WHERE country.id = city.country AND city.id = player.location"
    # finalSql = f"{sql} AND player.id = {playerId}"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

def get_random_question_by_location_id(location_id):
    sql = "select * from quiz_question"
    more_sql = f"{sql} WHERE location_id = {location_id}"
    final_sql = f"{more_sql} ORDER BY RAND() LIMIT 1"
    # print(final_sql)

    cursor = connection.cursor()
    cursor.execute(final_sql)
    result = cursor.fetchall()
    return result



# converting data to Ojbect

# object = {
#     "id": data[0]
#      question_name:data[1]
#     location:[2]
# }


if __name__ == "__main__":
    questions = get_questions()
    print(questions)
    # class session(player_id,questions_answered,correct_count,chances,is_open)


    # class current_quiz(session_id,player_id,question_id,answer_option_id,is_correct):

    # question_data = (get_random_question_by_location_id(1))
    # options_by_question_data

    # # [(1, 'What are Finnish households encouraged to recycle?', 1)]
    # question1 = Question(question_data[0],question_data[1],question_data[2])
    # option1 = Option
    # option2 = Option
    # option3 = Option
    # option4 = Option


    # question1.add_options(option1,option2,option3,top4)
    # current_quiz.add(question1)

    # question1.id, question1.name,question1.location_id

# When a user he type a username
# our database will check if that username exists in our database or not
## yes: we will let the user continue his game >> fetch the session for this user
## no: we will create a new session for this user

# /login
# /home ( display map)
#/location/location_name
## get questions and option relating to this location_name
##
##display them on browser



#user answer questiontion >> uswer answer option_id
# logic to handle  user answer
# option_id
# question_id
# session_id
# player_id
# is_corect

# current_quiz_session =Current_quiz_session(session_id,player_id,question_id,answer_option_id,is_correct)

# insert .... table  value (option_id,session_id,question_id,player_id,is_correct)

#name = input("type Name)")

# user1 = User(name)
#user1.name = new_name
# quiz_session1 = updatedSession
# update_to_database(updatedSession)
# return to home page


# quiz_session1.how_question

# user
# session = get_session_by_user


