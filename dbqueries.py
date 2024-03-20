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
            CREATE TABLE IF NOT EXISTS categories (id integer primary key, name varchar(32), description TEXT, created_at timestamp default CURRENT_TIMESTAMP )

    """
    )
    
    con.commit()

def insert_items(name, batch_number, price, category):
    curs.execute(
        """
        INSERT INTO items(name, batch_number, price, category_id) VALUES (?, ?, ?, ?)
        """,
        (name, batch_number, price, category)
    )
    
    con.commit()
    
def insert_categories(name, description):
    curs.execute(
        """
        INSERT INTO categories (name, description) VALUES (?, ?)
        """,
        (name, description)
    )
    
    con.commit()
    
create_table_categories()
create_table_items()
