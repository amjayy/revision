import sqlite3
from customer import Customer



conn = sqlite3.connect(':memory:')

c = conn.cursor()

c.execute("""CREATE TABLE customers (
            first text,
            last text,
            points integer
            )""")


def insert_cust(cust):
    with conn:
        c.execute("INSERT INTO customers VALUES (:first, :last, :points)", {'first': cust.first, 'last': cust.last, 'points': cust.points})
    


def get_custs_by_name(lastname):
    c.execute("SELECT * FROM customers WHERE last=:last", {'last': lastname})
    return c.fetchall()


def update_points(cust, points):
    with conn:
        c.execute("""UPDATE customers SET points = :points
                    WHERE first = :first AND last = :last""",
                  {'first': cust.first, 'last': cust.last, 'points': points})


def remove_custs(cust):
    with conn:
        c.execute("DELETE from customers WHERE first = :first AND last = :last",
                  {'first': cust.first, 'last': cust.last})
cust_1 = Customer('James', 'Gibson', 670)
cust_2= Customer('Holly ', 'Burns', 12039)
cust_3 = Customer('Alyson', 'Harper', 835)
cust_4 = Customer('Kimberly', 'Reeves', 23489)

def input_answer():
    while True: 
    answer= input("Enter Y for yes  or N for No:")
    if answer == "y":
    
        
print("Welcome to Esobar Mart.")
print("Are you a returning customer?")



def returning customer():



insert_cust(cust_1)
insert_cust(cust_2)

custs = get_custs_by_name('Doe')
print(custs)

update_points(cust_2, 95000)
remove_custs(cust_1)

custs = get_custs_by_name('Doe')
print(custs)

conn.close()
