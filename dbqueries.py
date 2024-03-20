from config import CONNECTION as con, CURSOR as curs

def create_table_items():
    curs.execute(
        """
            CREATE TABLE IF NOT EXISTS items (id integer primary key, name varchar(32), batch_number TEXT, price integer, category_id integer, created_at timestamp)

    """
    )
    
    con.commit()
    
def create_table_categories():
    curs.execute(
        """
            CREATE TABLE IF NOT EXISTS categories (id integer primary key, name varchar(32), description TEXT, created_at timestamp)

    """
    )
    
    con.commit()
    

    
    
create_table_categories()
create_table_items()
