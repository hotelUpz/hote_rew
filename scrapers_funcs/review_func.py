from bs4 import BeautifulSoup
import dateparser
from faker import Faker
from datetime import datetime, timedelta
from random import randint
import unicodedata

def generate_fake_dates(date_string):
    # Convert the input date string to a datetime object
    base_date = datetime.strptime(date_string, '%Y-%m-%d')
    # Subtract a random number of days between 3 and 12 from the base date
    subtract_days = randint(3, 12)
    checkin_date = base_date - timedelta(days=subtract_days)
    # Calculate the remaining days between the check-in date and the base date
    remaining_days = (base_date - checkin_date).days
    # Add a random number of days between 1 and the remaining days to the check-in date
    add_days = randint(1, remaining_days)
    checkout_date = checkin_date + timedelta(days=add_days)
    # Format the dates as strings in the desired format
    checkin_date_str = checkin_date.strftime('%Y-%m-%d')
    checkout_date_str = checkout_date.strftime('%Y-%m-%d')

    return checkin_date_str, checkout_date_str



def page_scraper_otziv(resHtml, hotelid):
    # return print('hello page_scraper_otziv')
    result_review_upz = []

    try:
        soup1 = BeautifulSoup(resHtml, "lxml")  
        # print(resHtml)     
    except Exception as ex:
        # print(f"str102___{ex}")
        return None
 
    try:
        # print('hello finder')
        try:
           review_block = soup1.find('ul', attrs={}).find_all('li', class_='review_list_new_item_block')
        except:
            return None
        # print(len(review_block))
        for item in review_block:
            try:
                try:
                    title = item.find('h3', attrs={'class': 'c-review-block__title', 'class': 'c-review__title--ltr'}).get_text().strip()
                    title = "".join(c for c in title if unicodedata.category(c) != "So")
                    # print(title)               
                except Exception as ex:
                    title = ''
                    # print(f"str27___{ex}")
                try:
                    pros = item.find('p').find('span', class_='c-review__body').get_text().strip()
                    pros = "".join(c for c in pros if unicodedata.category(c) != "So")             
                    # print(pros)              
                except Exception as ex:
                    pros = '' 
                    # print(f"str33___{ex}")
                try:
                    cons = item.find_all('p')[1].find('span', class_='c-review__body').get_text().strip()
                    cons = "".join(c for c in cons if unicodedata.category(c) != "So")
                    # print(cons)
                except Exception as ex:
                    cons = '' 
                    # print(f"str39___{ex}") 
                try:
                    try:
                       dt1 = item.find_all(class_='c-review-block__date')[1].get_text().split(':')[1].strip()
                    except:
                       dt1 = item.find_all(class_='c-review-block__date')[0].get_text().split(':')[1].strip()
                
                    parsed_date = dateparser.parse(dt1, languages=['en', 'ru'])           
                    transformed_date = parsed_date.strftime('%Y-%m-%d')
                    fake = Faker()
                    fake_time = fake.time(pattern='%H:%M:%S')
                    dt2 = f"{transformed_date} {fake_time}"
                    # print(dt2)
                except Exception as ex:
                    dt2 = ''
                    # print(f"str46___{ex}") 
                try:             
                    checkin, checkout = generate_fake_dates(transformed_date)
                except:
                    checkin, checkout = '', ''
                try:
                    try:
                        average_score = float(item.find('div', class_='bui-review-score__badge').get_text().strip().replace(',', '.'))
                    except:
                        average_score = int(item.find('div', class_='bui-review-score__badge').get_text().strip()) + 0.0
                    # print(average_score)
                #    break
                except Exception as ex:
                    average_score = 9.3
                    # print(f"str53___{ex}") 
                try:
                    author_name = item.find('span', class_='bui-avatar-block__title').get_text().strip()
                    # print(author_name)
                #    break
                except Exception as ex:
                    author_name = ''
                    # print(f"str60___{ex}") 
                try:
                    element = item.find('div', attrs={'data-room-id': True})      
                    room_id = element['data-room-id']
                    # print(room_id)

                except Exception as ex:
                    room_id = ''
                    # print(f"str67___{ex}")

                try:                
                    languagecode = item.find('h3', attrs={'class': 'c-review-block__title', 'class': 'c-review__title--ltr'}).get('lang').strip()
                except:
                    try:
                        languagecode = item.find('p').find('span', class_='c-review__body').get('lang').strip()
                    except:
                        try:
                            languagecode = item.find_all('p')[1].find('span', class_='c-review__body').get('lang').strip()
                        except Exception as ex:
                            languagecode = ''
                            print(f"review_func__str92___{ex}") 
                # print(languagecode)
                result_review_upz.append({
                    "hotelid": int(hotelid),
                    "title": title, 
                    "cons": cons, 
                    "pros": pros, 
                    # "dt1": '2022-10-01 14:18:22',
                    "dt1": dt2,
                    "average_score": average_score, 
                    "author_name": author_name, 
                    "room_id": int(room_id), 
                    "checkin": checkin, 
                    "checkout": checkout, 
                    "languagecode": languagecode            
                })
            except:
                continue

            # print(len(result_review_upz_list))
    except Exception as ex:
        print(f"str162___{ex}") 
        pass
    try:
        return result_review_upz
    except:
        return None
    







            # try:
            #     checkinBlock = item.find_all('div', class_='bui-list__body')[1]
            #     #    print(checkinBlock)
            #     checkin = checkinBlock.get_text(strip=True, separator="\n")
            #     # print(checkin)
            #     #    break
            # except Exception as ex:
            #     checkin = ''
            #     print(f"str76___{ex}") 
            # try:
            #     checkout = checkin 
            # except Exception as ex:
            #     checkout = ''
            #     print(f"str81___{ex}") 