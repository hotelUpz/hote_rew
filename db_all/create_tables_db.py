def create_tables():
    import mysql.connector
    from mysql.connector import connect, Error 
    from . import config_real

    config = {
        'user': config_real.user,
        'password': config_real.password,
        'host': config_real.host,
        'port': config_real.port,
        'database': config_real.database,      
    }

    try:
        conn = mysql.connector.connect(**config)      
        print("Connection2 established")
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
    
    try:
        cursor = conn.cursor() 
    except Error as e:
        print(f"Error connecting to MySQL: {e}")

    # try:
    #    cursor.execute("DROP TABLE upz_hotels_review_test1")
    # except:
    #     pass
    # try:
    #    cursor.execute("DROP TABLE black_list_reviews_test1")
    # except:
    #     pass

    # create_table_query7 = '''
    # CREATE TABLE result_review_test1 (
    #     id INT AUTO_INCREMENT PRIMARY KEY,
    #     hotelid VARCHAR(20),
    #     title TEXT,
    #     cons TEXT,
    #     pros TEXT,
    #     dt1 TEXT,
    #     average_score TEXT,
    #     author_name TEXT,
    #     room_id TEXT,
    #     checkin TEXT,
    #     checkout TEXT,
    #     languagecode TEXT
    # )ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci
    # '''

    # create_table_query9 = '''
    # CREATE TABLE black_list_reviews_test1 (
    #     id INT AUTO_INCREMENT PRIMARY KEY,
    #     hotelid VARCHAR(20),
    #     url TEXT,
    #     otziv VARCHAR(4)
    # )
    # '''

    modyfi_table_query7 = '''
    ALTER TABLE upz_hotels_review
    MODIFY hotelid INT(15),
    MODIFY room_id INT(15)  
    
'''
# MODIFY average_score FLOAT

 # MODIFY average_score DECIMAL(5, 1),

    create_table_query10 = '''
    CREATE TABLE upz_hotels_review_test1 (
        id INT AUTO_INCREMENT PRIMARY KEY,
        hotelid INT(15),
        title VARCHAR(255),
        cons TEXT,
        pros TEXT,
        dt1 DATETIME,
        average_score FLOAT,
        author_name VARCHAR(255),
        room_id INT(15),
        checkin DATE,
        checkout DATE,
        languagecode VARCHAR(10)
    )ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci
    '''
    alter_table_query = '''
        ALTER TABLE result_review_test2
        ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci
    '''
    # alter_table_query = '''
    #     ALTER TABLE result_review_test2
    #     ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci
    # '''

    # ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci

    # conn.commit()
    # cursor.execute(alter_table_query)
    cursor.execute(modyfi_table_query7)
    # cursor.execute(create_table_query10)


    cursor.close()
    conn.close()
    
    return print("the tables was created successfully")


create_tables()


# python create_tables_db.py
# python -m db_all.create_tables_db


# sudo mysql -u root -p

# CREATE USER 'sonnik12'@'localhost' IDENTIFIED BY '6687vono';
# CREATE DATABASE upz_hotels_copy1;
# GRANT ALL PRIVILEGES ON upz_hotels_copy1.* TO 'sonnik12'@'localhost';

# FLUSH PRIVILEGES;
# EXIT;
