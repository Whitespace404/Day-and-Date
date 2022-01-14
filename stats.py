import sqlite3

def correct_vs_attempts():
    conn = sqlite3.connect("stats.db")
    cursor = conn.cursor()
    stats = cursor.execute("""SELECT * FROM stats """).fetchall()

    correct_answers = 0
    attempts = 0
    for i in stats:
        if i[3] == 1:
            correct_answers += 1
            attempts += 1
        else:
            attempts += 1
    conn.commit()
    conn.close()    
    return str(correct_answers), str(attempts)
