from config import CONNECTION as con, CURSOR as curs

def create_table_items():
    curs.execute(
        """
            CREATE TABLE IF NOT EXISTS items (id integer primary key, name varchar(32), batch_number TEXT, price integer, category_id integer, created_at timestamp default CURRENT_TIMESTAMP)

    """
    )
    
    con.commit()
    
def create_table_categories():
    curs.execute(
        """
            CREATE TABLE IF NOT EXISTS categories (id integer primary key, name varchar(32) unique, description TEXT, created_at timestamp default CURRENT_TIMESTAMP )

    """
    )
    
    con.commit()

def insert_items(name, batch_number, price, category):
    check_category = curs.execute("SELECT name FROM categories WHERE name = ?", (category,)).fetchone()

    if check_category:
        category_id = curs.execute(""" SELECT id from categories where name = ? """, (category, )).fetchone()
        curs.execute(
            """
            INSERT INTO items(name, batch_number, price, category_id) VALUES (?, ?, ?, ?)
            """,
            (name, batch_number, price, category_id[0])
        )
        con.commit()
        print("Stock Recorded successfully")
    else:
        print("Oops, category doesn't exist")
        
        
    
def insert_categories(name, description):
    curs.execute(
        """
        INSERT INTO categories (name, description) VALUES (?, ?)
        """,
        (name, description)
    )
    
    con.commit()


def select_all_items():
    return curs.execute(""" SELECT i.id, i.name, i.batch_number, i.price, c.name, i.created_at FROM items i LEFT JOIN categories c on i.category_id = c.id""").fetchall()


def select_all_categories():
    return curs.execute(""" SELECT * FROM categories """).fetchall()


