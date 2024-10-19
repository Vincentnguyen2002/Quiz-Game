import string
from random import random

from src.config import dbconfig


# Just the log-in Logic of the game
# I tried to copy the format from the sample back-end and make it compatible for our own back-end.
class Game:

    def __init__(self, player_name=None):
        self.cursor = None
        self.status = {}  # Dictionary for game stuff
        self.location = []  # List for game places

        if player_name:
            player_id = self.check_player_existence(player_name)

            if player_id:
                self.load_existing_game(player_id)
            else:
                self.create_new_game(player_name)

    # Name DB scanner
    def check_player_existence(self, player_name):
        cur = config.conn.cursor()
        cur.execute("SELECT id FROM player WHERE name=%s", (player_name,))
        result = cur.fetchone()
        return result[0] if result else None

    # Continue Game loader
    def load_existing_game(self, player_id):
        cur = config.conn.cursor()
        cur.execute("SELECT id, co2_consumed, location FROM Game WHERE player_id=%s", (player_id,))


    # Make new G
    def create_new_game(self, player_name):
        letters = string.ascii_lowercase + string.ascii_uppercase + string.digits
        game_id = ''.join(random.choice(letters) for _ in range(20))

        self.status = {
            "id": game_id,
            "name": player_name,
            "co2": {
                "consumed": 0,
            },
            "attempts": 0,
            "chances": config.default_chances
        }

    # insert new G to DB
    def insert_new_game(self, player_name=None):
        sql = f"INSERT INTO quiz_session (id, player_id, question_answers, correct_count, chances, is_open) VALUES " \
              f"('{self.status['id']}', (SELECT id FROM player WHERE name = '{self.status['name']}'), 0, 0, {self.status['chances']}, 1)"
        self.cursor.execute(sql)
        dbconfig.conn.commit()
