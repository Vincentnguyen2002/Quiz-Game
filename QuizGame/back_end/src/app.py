import json
import os

from flask import Flask, redirect, render_template, request, url_for, session, flash, Response
from src.components.location import cities,countries
from src.components.questions import questions,question_options
from src.components.players import players
from src.components.game import game
from src.components.quiz_sessions import quiz_sessions, current_quiz_sessions

from flask_cors import CORS


from flask_session import Session

app = Flask( __name__)

cors =CORS (app)
app.config['CORS_HEADERS'] = 'Content-Type'


app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


# @app.route("/index")
# @app.route("/home")
@app.route("/", methods = ["POST","GET"])
def index():
  
  quiz_session = session.get("quiz_session")
  
  if not quiz_session:
    return redirect(url_for("login"))
  else:
    correct_counts = quiz_session[3]
    chances = quiz_session[4]
    if correct_counts >= 4 or chances <= 0:
      return redirect(url_for("finish"))
    return render_template("index.html", quiz_session = quiz_session)
  
@app.route("/home/",methods = ["POST","GET"])
def home():
  quiz_session = session.get("quiz_session")
  
  if not quiz_session:
    return redirect(url_for("login"))
  print(quiz_session)
  if request.method == "GET":
    player = players.get_player_by_player_id(quiz_session[1])[0]
    # if not player:
    # return redirect(url_for("login"))
    # player (1, 'trung')
    # quiz_session (1, 1, 0, 0, 3, 1)
    correct_rate = 0
    if quiz_session[2] > 0: # questions answered more than 0
      correct_rate = round((quiz_session[3] / quiz_session[2]),2) * 100
    # print(correct_rate)
    
    return render_template("home.html",quiz_session = quiz_session, player = player, correct_rate = correct_rate)
  else:
    return redirect(url_for("worldmap"))
  
@app.route("/login/", methods = ["POST","GET"])
def login():
  
  if "quiz_session" in session:
    return redirect(url_for("home"))
  
  if request.method == "POST":
    username = request.form.get("username")
    quiz_session = game.get_quiz_session_by_player_name(username)
    session["quiz_session"] = quiz_session[0]
    flash('Welcome to the Quiz World')
    return redirect(url_for("home"))
    
  return render_template("login.html")
    
    

@app.route("/worldmap/", methods = ["POST","GET"])
def worldmap():
  quiz_session = session.get("quiz_session")
  # print(quiz_session)
  if request.method == "GET":
    if not quiz_session:
      return redirect(url_for('login'))   
    player = players.get_player_by_player_id(quiz_session[1])[0]
    country_list = countries.get_countries()
    location_list = cities.get_cities()
    
    # correct_points = session["quiz_session"][3]
    # chances = session["quiz_session"][4]
    correct_points = quiz_session[3]
    chances = quiz_session[4]
    #when victory or game_over
    if correct_points == 4 or chances == 0:
      return redirect(url_for("finish"))
    # print(country_list.size)
    return render_template("worldmap1.html", country_list = country_list, location_list = location_list, quiz_session=quiz_session, player = player)
  else:
    # location_id	"Helsinki"
    location_name = request.form.get("location_name")
    # location_in_request = cities.get_city_by_id(location_id)
    location_in_request = cities.get_city_by_name(location_name)
    # flash(f"You have chosen {location_name}")
    return redirect(url_for("location",city_name = location_in_request[0][1].lower()))

@app.route("/location/<city_name>", methods = ["POST","GET"])
def location(city_name):
  # quiz_session = session["quiz_session"]
  quiz_session = session.get("quiz_session")
  if request.method == "GET":
    player = players.get_player_by_player_id(quiz_session[1])[0]
    city_in_request = cities.get_city_by_name(city_name)
    question = questions.get_random_question_by_location_id(city_in_request[0][0])
    options_of_question = question_options.get_options_by_question_id(question[0][0])
    # print(options_of_question)
    
    return render_template("question2.html",city_in_request=city_in_request,question=question,options_of_question=options_of_question,quiz_session = quiz_session, player = player)
  else:
    answer_question_option_id = request.form.get("option_id")
    quiz_session_by_player = session['quiz_session']

    updated_quiz_session = game.save_option_by_option_id(answer_question_option_id,quiz_session_by_player)[0]
    option = question_options.get_option_by_option_id(answer_question_option_id)
    if question_options.option_is_correct(option):
      flash("You answer correct.")
    else: 
      flash("You answer wrong.")
    #update quiz_session
    session["quiz_session"] = updated_quiz_session

    return redirect(url_for("worldmap"))
  
@app.route("/finish/", methods = ["POST","GET"])
def finish():
  # quiz_session = session['quiz_session']
  quiz_session = session.get("quiz_session")
  print(quiz_session)
  if request.method == "GET":
    correct_counts = quiz_session[3]
    chances = quiz_session[4]
    return  render_template("finish.html",quiz_session = quiz_session, correct_counts = correct_counts, chances = chances )
  else:
    quiz_session_id = quiz_session[0]
    player_id =  quiz_session[1]
    print(f'quiz_session_id: {quiz_session_id}')
    print(f'player id: {player_id}')
    quiz_sessions.update_quiz_session_when_finish(quiz_session_id)
    quiz_sessions.insert_new_quiz_session(player_id)
    new_quiz_session_by_same_player_id = quiz_sessions.get_open_quiz_session_by_player_id(player_id)
    # print(f"this is a new quiz session: {new_quiz_session_by_same_player_id}")
    session['quiz_session'] = new_quiz_session_by_same_player_id[0]
    return redirect(url_for("home"))
    

@app.route("/about/")
def about():
  return render_template("about.html")

@app.route("/logout/")
def logout():
  session.clear()
  return redirect(url_for("login"))  

@app.route("/worldmap/locations/")
def locations():
    data = game.all_locations_json()

    if data == []:
        response = {
            "message": "No locations found"
        }
        json_response = json.dumps(response)
        http_response = Response(response=json_response,status=404,mimetype="application/json")
    else:
        response = data
        json_response = json.dumps(response)
        http_response = Response(response=json_response,status=200,mimetype="application/json")
    return http_response



if __name__ == "__main__":
  app.run(debug=True)

