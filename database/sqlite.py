import sqlite3 as sq


def sql_start():
    global base, cur
    base = sq.connect('pizza_cool.db')
    cur = base.cursor()
    if base:
        print('Database is connected succesfully!')
    base.execute('create table if not exists menu(img text, name text primary key, description text, price text)')
    base.commit()

async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute('insert into menu values (?, ?, ?, ?)', tuple(data.values()))
        base.commit()