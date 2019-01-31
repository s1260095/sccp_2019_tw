import sqlite3
import hashlib
from datetime import datetime 

dbname = 'twitter.db';
conn = sqlite3.connect(dbname);
c = conn.cursor();

# add_user add user into DB
# this func's args are username and password
def add_user(username, password):
    try:
        # ENCRYPT(HASH) Password
        encrypted_password = hashlib.sha256( \
                password.encode('utf-8')).hexdigest()
        # Do
        c.execute('INSERT INTO users(name, password) VALUES(?, ?)',\
                (username, encrypted_password));
        conn.commit()
    except sqlite3.Error as e:
        # if Error occured, raise Error(Exception).
        raise e


# get_user_by_name returns a tupple
# tupple format is (id, name, hashed_password)
def get_user_by_name(name):
    try:
        c.execute('SELECT * FROM users WHERE name = ?', (name,))
        res = c.fetchone()
        return res
    except sqlite3.Error as e:
        # if Error occured, raise Error(Exception).
        raise e

# add_tweet add tweet into DB.
# this func's args are user_id and text.
def add_tweet(user_id, text):
    try:
        # now is an INTEGER, it treat as UNIX Time.
        now = int(datetime.now().strftime('%s'), 10)
        # Do
        c.execute('INSERT INTO tweets(text, user_id, published_at) VALUES (?, ?, ?)', \
                  (text, user_id, now))
        conn.commit()
    except sqlite3.Error as e:
        # if Error occured, raise Error(Exception).
        raise e

# get_all_tweets to get all tweets.
# this func's returns a tuple.
# returning value's format is ((id, text, user_id, published_at), ...)
def get_all_tweets():
    try:
        # Tweet's order should be in the newest order.
        c.execute('SELECT * FROM tweets ORDER BY published_at DESC')
        res = c.fetchall()
        return res
    except sqlite3.Error as e:
        # if Error occured, raise Error(Exception).
raise e
