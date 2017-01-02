import sqlite3
conn = sqlite3.connect('pong.db')
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS leaderboard"
          "(user_name TEXT PRIMARY KEY, score INTEGER)")

c.execute("CREATE TABLE IF NOT EXISTS users"
          "(user_name TEXT PRIMARY KEY, password TEXT, verified INTEGER)")

# c.execute("INSERT INTO users "
#           "values (?, ?, ?)", ("me", "me_irl", 0))

c.execute("INSERT INTO leaderboard "
          "values (?, ?)", ("me", 100))

conn.commit()
conn.close()