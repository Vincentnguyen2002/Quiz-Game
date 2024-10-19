import sys
sys.path.append('G:\\Metropolia\\Metropolia\\2023\\Syksy\\SOFTWARE_2\\PROJECT\\QUIZ_PROJECT\\back_end')
from src.config import dbconfig

from src.components.location import cities,countries
from src.components.questions import questions,question_options
from src.components.players import players
from src.components.quiz_sessions import quiz_sessions, current_quiz_sessions
from src.components.external_api import weather

#when such username not exist, add that username to player table and add a new quiz_session with that new username to quiz_session table
def get_session_when_player_not_exist(username):
    players.insert_new_player(username)
    new_player = players.get_player_by_name(username) #[(3, 'hoa')]
    # print(new_player)
    quiz_sessions.insert_new_quiz_session(new_player[0][0])
    new_quiz_session = quiz_sessions.get_open_quiz_session_by_player_id(new_player[0][0])
    print("when player not exist, creating new quiz session")
    return new_quiz_session
  
def get_session_when_player_exist(username):
  
    username_data = players.get_player_by_name(username)
    quiz_session = quiz_sessions.get_open_quiz_session_by_player_id(username_data[0][0])
    
    # name is exist but no open quiz_session with that name
    if not quiz_session: 
      quiz_sessions.insert_new_quiz_session(username_data[0][0])
      new_opened_quiz_session = quiz_sessions.get_open_quiz_session_by_player_id(username_data[0][0])
      quiz_session = new_opened_quiz_session
      print("when player exist but quiz_session closed, create new open quiz_session ")
    
    else:
      print("player exist and quiz_session open, getting that quiz_session")
    
    return quiz_session



def get_quiz_session_by_player_name(username):
  username_data = players.get_player_by_name(username)
  quiz_session = None
  # print(username_data)
  if not players.is_name_exist(username_data):
    quiz_session = get_session_when_player_not_exist(username)
  else:
    quiz_session = get_session_when_player_exist(username)
      
  return quiz_session

def do_insert_new_current_quiz_session(quiz_session_by_player,answer_by_player):
  session_id =  quiz_session_by_player[0]
  player_id= quiz_session_by_player[1]
  question_id  = answer_by_player[0][1]
  question_option_id = answer_by_player[0][0]
  is_correct = answer_by_player[0][3]
  current_quiz_sessions.insert_new_current_quiz_session(session_id,player_id,question_id,question_option_id,is_correct)  
  return

def quiz_session_when_answer_correct(quiz_session_by_player, answer_by_player):
  
  # print(f"old: {quiz_session_by_player}")
  do_insert_new_current_quiz_session(quiz_session_by_player,answer_by_player)
  session_id = quiz_session_by_player[0]
  new_questions_answered = quiz_session_by_player[2] + 1
  new_correct_counts = quiz_session_by_player[3] + 1
  print("Player answer correct")
  print("Update this player points")
  
  quiz_sessions.update_quiz_session_when_right(session_id,new_questions_answered,new_correct_counts)
  updated_quiz_session = quiz_sessions.get_quiz_session_by_id(session_id)
  print("new ",updated_quiz_session)
  return updated_quiz_session


def quiz_session_when_answer_wrong(quiz_session_by_player, answer_by_player):
  
  # print(f"old: {quiz_session_by_player}")
  do_insert_new_current_quiz_session(quiz_session_by_player,answer_by_player)
  session_id = quiz_session_by_player[0]
  new_questions_answered = quiz_session_by_player[2] + 1
  new_chances = quiz_session_by_player[4] - 1
  print("Player answer wrong")
  print("Update this player points")
  
  quiz_sessions.update_quiz_session_when_wrong(session_id, new_questions_answered, new_chances)
  updated_quiz_session = quiz_sessions.get_quiz_session_by_id(session_id)
  print(f"new: {updated_quiz_session} ")
  return updated_quiz_session

def save_option_by_option_id(option_id, quiz_session_by_player):
  
  answer_option_data = question_options.get_option_by_option_id(option_id)
  is_correct = question_options.option_is_correct(answer_option_data)

  print(f'answer is correct: {is_correct}')
  
  if is_correct:
    
    updated_quiz_session = quiz_session_when_answer_correct(quiz_session_by_player,answer_option_data)
  else:
    updated_quiz_session = quiz_session_when_answer_wrong(quiz_session_by_player,answer_option_data)
  return updated_quiz_session

# def get_all_location():
#   locations = cities.get_cities()
#   return locations

def get_all_locations_json(location_list):
  
  json_response = []
  for location_name in location_list:
    location_reponse = weather.get_json_response(location_name)
    # print(location_reponse)
    json_response.append(location_reponse)
    # json_response = json_response + location_reponse
  return json_response  

def get_location_name_list (locations):
  return list(map(lambda obj: obj[1],locations))

def all_locations_json():
  locations = cities.get_cities()
  location_name_list = get_location_name_list(locations)
  location_json_list = get_all_locations_json(location_name_list)
  return location_json_list
    
def game() :
  
  # username = 'hoa'
  # quiz_session = get_quiz_session_by_player_name(username)
  # # answer_option_id = request.form.get("option_id")
  # # print(quiz_session)
  # wrong_answer_option_id = 19 # wrong
  # right_answer_option_id = 18 # right
  # save_option_by_option_id(right_answer_option_id,quiz_session)
  # locations = get_all_location()
  # location_list = get_location_name_list(locations)
  json_response = all_locations_json()
  # print(location_list)
  print(json_response)


if __name__ == "__main__":
  game()