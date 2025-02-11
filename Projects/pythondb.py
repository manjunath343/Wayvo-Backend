import psycopg2
import random
conn = psycopg2.connect(
    dbname="WayvoDB",
    user="postgres",
    password="Manju@343",
    host="localhost"
)
cur = conn.cursor()

def generate_member_id():
    return random.randint(1000, 9999)

per = int(input("Enter whether you want to borrow or return a book: 1.Borrow 2.Return 3.Insert Book 4.Register "))

if per == 1:  
    cur.execute("SELECT * FROM books")
    data = cur.fetchall()
    for i in data:
        print(i)
    
    k = int(input("Enter the book id you want to borrow: "))
    cur.execute("SELECT is_available FROM books WHERE book_id = %s", (k,))
    
    if cur.fetchone()[0] == False:
        print("The book you requested is not available")
    else:
        print("The book you requested is available")
        mem_id = int(input("Enter your mem_id: "))
        try:
            cur.execute("UPDATE books SET is_available = False WHERE book_id = %s", (k,))
            borrow_id = random.randint(1000, 9999)  
            cur.execute("INSERT INTO borrowed_list (borrow_id, book_id, mem_id) VALUES (%s, %s, %s)", 
                        (borrow_id, k, mem_id))
            conn.commit()  
        except Exception as e:
            print("There is a problem:", e)
        else:
            print("Your borrow is approved")

elif per == 2:  
    book_id = int(input("Enter your Book_id: "))
    mem_id = int(input("Enter your member id: "))
    try:
        cur.execute("UPDATE books SET is_available = True WHERE book_id = %s", (book_id,))
        cur.execute("UPDATE borrowed_list SET return_date = current_date WHERE book_id = %s AND mem_id = %s AND return_date IS NULL", 
                    (book_id, mem_id))
        conn.commit()  
    except Exception as e:
        print("There is a problem:", e)
    else:
        print("Your return is recorded")

elif per == 3:  
    book_id = int(input("Enter book id: "))
    book_name = input("Enter book name: ")
    book_author = input("Enter author name: ")
    is_av = True  
    try:
        cur.execute("INSERT INTO books (book_id, book_name, book_author, is_available) VALUES (%s, %s, %s, %s)", 
                    (book_id, book_name, book_author, is_av))
        conn.commit()  
    except Exception as e:
        print("There is a problem:", e)
    else:
        print("Successfully inserted")

elif per == 4:  
    mem_id = generate_member_id()
    print(f"Please record your mem_id: {mem_id}")
    mem_name = input("Enter your name: ")
    mem_email = input("Enter your email: ")
    try:
        cur.execute("INSERT INTO members (member_id, member_name, email) VALUES (%s, %s, %s)", 
                    (mem_id, mem_name, mem_email))
        conn.commit()  
    except Exception as e:
        print("There is a problem:", e)
    else:
        print("You are registered")

cur.close()
conn.close()