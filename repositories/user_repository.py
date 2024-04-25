from db.run_sql import run_sql
from models.user import User


def save(user):
    sql = "INSERT INTO users (puuid, username, tagline) VALUES (%s, %s) RETURNING id"
    values = [user.puuid, user.username, user.tagline]
    results = run_sql(sql, values)
    id = results[0]["id"]
    user.id = id


def select_all():
    users = []
    sql = "SELECT * FROM users"
    results = run_sql(sql)
    for result in results:
        user = User(result["puuid"], result["username"], result["tagline"])
        users.append(user)
    return users
