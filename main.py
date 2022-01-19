import datetime
import random
import sqlite3
import time
import stats

connection = sqlite3.connect("stats.db")
c = connection.cursor()

# c.execute("""
# CREATE TABLE stats (
#     question text,
#     correct_answer text,
#     given_answer text,
#     is_correct boolean,
#     time_taken text
# )
# """)

while True:
    MONTHS = ["January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"]
    date = random.randint(1, 30)
    month = random.choice(MONTHS)
    year = random.randint(2022, 2022)

    question = f"{date} {month}, {year}"
    print(question)

    start_time = time.time()
    
    ans = input("> ").title()
    correct_answer = datetime.datetime.strptime(f'{month} {date}, {year}', '%B %d, %Y').strftime('%A')

    if ans == correct_answer:
        end_time = time.time()
        print(f"Correct. It was a {correct_answer}.")
        c.execute(f"""INSERT INTO stats VALUES (
            '{question}', 
            '{correct_answer}', 
            '{ans}', 
            TRUE,
            '{round(end_time - start_time, 1)}'
            )""")
        connection.commit()
        print(f"You took {round(end_time - start_time, 1)} seconds.")
        
    elif ans == "Stats":
        answers_attempts = stats.correct_vs_attempts()
        average_time = stats.average_time()
        
        print(f"You got {answers_attempts[0]} out of {answers_attempts[1]} correct.")
        print(f"You took an average of {average_time()}.")

    elif ans == "Stop" or ans == "Esc" or ans == "Exit":
        connection.commit()
        connection.close()
        quit()
    else:
        end_time = time.time()
        print(f"Incorrect. It was a {correct_answer}.")
        c.execute(f"""INSERT INTO stats VALUES (
            '{question}', 
            '{correct_answer}', 
            '{ans}', 
            FALSE,
            '{round(end_time - start_time, 1)}'
            )""")
        connection.commit()
        print(f"You took {round(end_time - start_time, 1)} seconds.")

    print("\n")
    time.sleep(1)
