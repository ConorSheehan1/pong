import sqlite3
conn = sqlite3.connect('pong.db')
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS leaderboard"
          "(user_name text, score integer)")

c.execute("CREATE TABLE IF NOT EXISTS users"
          "(user_name text, password text, verified integer)")

c.execute("INSERT INTO users "
          "values (?, ?, ?)", ("me", "me_irl", 0))

conn.commit()
conn.close()