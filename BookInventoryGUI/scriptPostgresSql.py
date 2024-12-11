import psycopg2


def create_db():
    conn=psycopg2.connect("dbname='database1' user='postgres' password='postgres' host='localhost' port='5232'")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL);")
    conn.commit()
    conn.close()

def insert(item,quantity,price):
    conn=psycopg2.connect("dbname='database1' user='postgres' password='postgres' host='localhost' port='5232'")
    cur=conn.cursor()
    #cur.execute("INSERT INTO store VALUES ('%s','%s','%s');" % (item,quantity,price))
    cur.execute("INSERT INTO store VALUES (%s,%s,%s);", (item,quantity,price))
    conn.commit()
    conn.close()

def view():
    conn=psycopg2.connect("dbname='database1' user='postgres' password='postgres' host='localhost' port='5232'")
    cur=conn.cursor()
    cur.execute("SELECT * FROM store;")
    rows=cur.fetchall()
    conn.close()
    return rows

def deleted(item):
    conn=psycopg2.connect("dbname='database1' user='postgres' password='postgres' host='localhost' port='5232'")
    cur=conn.cursor()
    cur.execute("DELETE FROM store WHERE item=%s;", (item,))      #in item, you need add comma in the final
    conn.commit() # Commit the changes to the database
    conn.close()
    

def update(item,quantity,price):
    conn=psycopg2.connect("dbname='database1' user='postgres' password='postgres' host='localhost' port='5232'")
    cur=conn.cursor()
    cur.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s;",(quantity,price,item))
    conn.commit() # Commit the changes to the database
    conn.close()
    

#update("Water Glass", 20,33.4)
#deleted("Wine Glass")
#insert("Wine Glass",6,34.2)
print(view())