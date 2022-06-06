from loader import conn


async def get_ids():
    with conn.cursor() as cur:
        sql = "SELECT chat_id FROM users" \
              "WHERE active = 1"
        cur.execute(sql)
        result = cur.fetchall()
    return result


async def update_active(data):
    with conn.cursor() as cur:
        sql = "UPDATE users" \
              "SET active = 0" \
              "WHERE user_id NOT IN %s"
        cur.execute(sql, data)
        conn.commit()


async def get_winners():
    with conn.cursor() as cur:
        sql = "SELECT fullname, username FROM users" \
              "WHERE active = 1"
        cur.execute(sql)
        result = cur.fetchall()
    return result