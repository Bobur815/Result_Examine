from MySQLdb import connect, Error # Menda mysql.connector ishlamayapti, shuning uchun MySQLdb dan foydalandim
 
def get_cursor():
    
    DB_HOST = "localhost"
    DB_USER = "bobur"
    DB_PASSWORD = "a15081993"
    DB_DATABASE = "todo_app"

    try:
        db = connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD
        )
        cursor = db.cursor()

        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_DATABASE}")
        cursor.execute(f"USE {DB_DATABASE}")
        

        cursor.execute(f"""CREATE TABLE IF NOT EXISTS tasks(
                       id INT AUTO_INCREMENT PRIMARY KEY,
                       title VARCHAR(255) NOT NULL,
                       description TEXT,
                       deadline DATE,
                       time TIME,
                       completed BOOLEAN DEFAULT FALSE,
                       assigned_to VARCHAR(255) NOT NULL);
                       """)
        return db
            
    except Error as e:
        print(f"DATABASE MODULIDA XATOLIK: {e}")

get_cursor()
