
import sqlite3


db = sqlite3.connect('myNewApp.db')
cr = db.cursor()
cr.execute('CREATE TABLE IF NOT EXISTS skills(skill MESSAGE_TEXT, progress INTEGER, id INTEGER)')

# change user id to change user
userId = 1


def close():
    db.close()
    print('Connection To Database Is Closed.')


def show_all_skills():  # Don

    cr.execute(f'SELECT * FROM skills Where id = "{userId}"')
    res = cr.fetchall()
    if len(res) > 0:
        print(f'Hello User {userId} You Have {len(res)} Skills, And Your Skills:')
        for key, val in enumerate(res):
            print(f'{key + 1}- {val[0]} => {val[1]}%.')
    else:
        print('Learn Skills Or Add To Your Profile!')


def add_skill():  # Don
    skill = input('Write A Skill To Add: ').strip().capitalize()
    cr.execute(f'SELECT skill From skills WHERE skill = "{skill}" AND id = "{userId}"')
    res = cr.fetchone()
    if res is None:
        progress = input('Write A Progress: ')
        cr.execute(f'INSERT INTO skills VALUES ("{skill}", "{progress}", "{userId}")')
        db.commit()
        print(f'Your Skill {skill} Add.')
    else:
        choice = input('Your Skill Is Already Exists, Want To Update? Y,N. ').strip().capitalize()
        if choice == 'Y':
            newProg = input('Write A New Progress: ')
            cr.execute(f'UPDATE skills SET progress = "{newProg}" WHERE skill = "{skill}" and id = "{userId}"')
            db.commit()
            print(f'Don! Your Progress For {skill} Is {newProg}%.')

        else:
            print('As You Like!')


def delete_skill():  # Don
    skillDel = input('Write Skill You Want To Delete It: ').strip().capitalize()
    cr.execute(f'DELETE From skills WHERE skill = "{skillDel}" AND id = "{userId}"')
    print(f'{skillDel} Deleted Successfully!')
    db.commit()


def update_progress():  # Don
    skillName = input('Write Skill To Update: ').strip().capitalize()
    newProg = input('Write A New Progress: ')
    cr.execute(f'UPDATE skills SET progress = "{newProg}" WHERE skill = "{skillName}" AND id = "{userId}"')
    db.commit()
    print(f'Don!, Now Your Skill {skillName} Progress = {newProg}%.')


def print_method():
    print('*' * 25)

    inputMessage = """What Do You Want?
    'S' => Show all skills.
    'A' => Add new skill.
    'D' => Delete a skill.
    'U' => Update skill progress.
    'q' => Quite the app
    Chose Option: """

    valid = ['S', 'A', 'D', 'U', 'Q']
    user_input = input(inputMessage).strip().capitalize()

    if user_input in valid:
        while user_input[0] == 'Q':
            close()
            print('App is closed.')
            break
        else:
            if user_input == 'A':
                add_skill()
                print_method()
            elif user_input == 'S':
                show_all_skills()
                print_method()
            elif user_input == 'D':
                delete_skill()
                print_method()
            elif user_input == 'U':
                update_progress()
                print_method()

    else:
        print(f'Sorry This Command {user_input} Is Not Valid, Try Again.')
        print_method()


print_method()