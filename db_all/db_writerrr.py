def db_wrtr(total, n2):
    try:
        import time
        import mysql.connector
        from mysql.connector import connect, Error 
        from . import config_real
        print('hello db_writerr')

        config = {
            'user': config_real.user,
            'password': config_real.password,
            'host': config_real.host,
            'port': config_real.port,
            'database': config_real.database,      
        }
        for _ in range(3):
            try:
                conn = mysql.connector.connect(**config)      
                print("Writerr connection established otziv")
                break
            except Error as e:
                print(f"Error connecting to MySQL: {e}")
                time.sleep(3)
                continue
            
        try:
            cursor = conn.cursor() 
        except Error as e:
            print(f"Error connecting to MySQL: {e}")
                # time.sleep(3)
                   
        try:
            print(len(total))
            resReviews = []          
            whiteList = []
            n = int(int(n2)/1000)
        except:
            pass
        try:
            for t in total:
                try:
                    resReviews += t
                except:
                    continue
            resReviews = list(filter(None, resReviews))
            if len(resReviews) == 0:
                try:
                    semaforr(conn, cursor, n)
                except:
                    pass 
                return print('len_=0')
            print(f"len___{len(resReviews)}")
            # resReviews = remove_repetitions(resReviews)
            # print(f"arter___{len(resReviews)}") 
  
        except:
            pass  

        try:
            whiteList = writerr_table(conn, cursor, resReviews)
        except:
            pass
        try:
            changing_hotelsCritery(cursor, conn, whiteList)   
        except:
            pass 

        try:
           semaforr(conn, cursor, n)
        except:
            pass
 
        try:
            cursor.close()
            conn.close()
        except Error as e:
            print(f"Error connecting to MySQL: {e}")
    except:
        pass
    return


def writerr_table(conn, cursor, resReviews):
    rew_white = []
    rew_white_add = []
    rew_white_set = set()
    rew_white_batch_set = set()

    try:
        query7 = "INSERT INTO upz_hotels_review (hotelid, title, cons, pros, dt1, average_score, author_name, room_id, checkin, checkout, languagecode) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"         

        batch_size = 250
        batch_values = []

        for item in resReviews:
            try:
                values = (item["hotelid"], item["title"], item["cons"], item["pros"], item["dt1"], item["average_score"], item["author_name"], item["room_id"], item["checkin"], item["checkout"], item["languagecode"])
                batch_values.append(values)
                rew_white_batch_set.add(item["hotelid"])

                if len(batch_values) >= batch_size:
                    try:
                        cursor.executemany(query7, batch_values)
                        conn.commit()
                        rew_white_set.update(rew_white_batch_set)
                        rew_white_batch_set = {}
                        batch_values = []
                    except Exception as ex:
                        print(f"117___{ex}")                        
                        rew_white_add = insert_rows_individually_rew(conn, cursor, query7, batch_values)
                        rew_white += rew_white_add
                        rew_white_batch_set = {}
                        batch_values = []
                        continue                   

            except Exception as ex:
                print(f"122___{ex}")
                continue

        if batch_values:     
            try:
                cursor.executemany(query7, batch_values)
                conn.commit()
                rew_white_set.update(rew_white_batch_set)
            except Exception as ex:
                print(f"130___{ex}")
                rew_white_add = insert_rows_individually_rew(conn, cursor, query7, batch_values)
                rew_white += rew_white_add
                rew_white_batch_set = {}
    except Exception as ex:
        print(f"123___{ex}")
        pass

    try:
        rew_white += list(rew_white_set)
    except Exception as ex:
        print(ex)

    return rew_white


def insert_rows_individually_rew(conn, cursor, query, data):
    rew_white_set = set()
    rew_white = []
    try:
        data = eval(data)
    except:
        data = data
    for item in data:
        try:
            values = (item)
            cursor.execute(query, values)            
            rew_white_set.add(item[0])
        except Exception as ex:
            # print(f"204___: {ex}")
            continue
    try:
        conn.commit()
    except:
        rew_white = []
        return rew_white
    rew_white = list(rew_white_set)
    return rew_white

def changing_hotelsCritery(cursor, conn, whiteList):
    try:       
        query12 = "UPDATE upz_hotels SET otziv = %s WHERE hotel_id = %s"

        for item in whiteList:
            try:
                try:
                    find_query = "SELECT hotel_id FROM upz_hotels WHERE hotel_id = %s"                     
                    cursor.execute(find_query, (item,))                      
                    row = cursor.fetchone()                      
                except Exception as ex:
                    print(f"db_writerr__str87__{ex}")

                if row:
                    try:                      
                        cursor.execute(query12, (1, item))                      
                    except Exception as ex:
                        print(f"db_writerr__str90__{ex}")

            except Exception as ex:
                print(f"db_writerr__str95__{ex}")
                continue
        conn.commit()           

    except Exception as ex:
        print(ex)

    return

def semaforr(conn, cursor, n):
    print(n)
    try:
        select_queryF = "SELECT otziv_flag FROM hotels_simafor WHERE id = %s"
        cursor.execute(select_queryF, (n,))
        row = cursor.fetchone()

        if row:
            update_query = "UPDATE hotels_simafor SET otziv_flag = %s WHERE id = %s"
            cursor.execute(update_query, (1, n))
            conn.commit()  
            print('hello simafor commit!')      

    except Exception as ex:
        print(ex)

# def remove_repetitions(data):
#     unique_values = set()
#     result = []
#     for item in data:
#         unil_value = item.get("room_id")
#         if unil_value not in unique_values:
#             result.append(item)
#             unique_values.add(unil_value)
#     return result
