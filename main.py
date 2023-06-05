import requests
from fake_useragent import UserAgent
import random 
from random import choice
import time
import math
import re
import atexit
import shutil
import tempfile
import sys
from joblib import Parallel, delayed
# from multiprocessing import cpu_count

from scrapers_funcs import review_func
from db_all import db_reader, db_writerrr

uagent = UserAgent()

def random_headers():
    
    desktop_accept = [
        'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',     
        'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',     
        'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',     
        'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',     
        'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',     
        'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',     
        'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',                
        ]
    device_memoryHelper = [2,4,8,16,32]
    sett = set()
    finHeaders = []    
    finfinH = {}   
 
    headFront = [{
            'authority': 'www.booking.com',
            'accept': choice(desktop_accept), 
            'User-Agent': uagent.random,  
            'accept-language': 'en-US,en;q=0.8',
            # 'accept-language': 'ru-RU,ru;q=0.9',         
            # 'accept-language': f"'en-US,en;q=0.8', 'ru-RU,ru;q=0.9', 'uk-Uk,uk;q=0.5'",       
            'origin': 'https://www.booking.com/',
            'device-memory': f'{choice(device_memoryHelper)}'                  
            }
    ]
    headersHelper = [       
            {"sec-fetch-dest": "empty"},
            {"sec-fetch-mode": "cors"},
            {"sec-fetch-site": "same-origin"},
            {"accept-ch": "sec-ch-ua-model,sec-ch-ua-platform-version,sec-ch-ua-full-version"},
            {'cache-control': 'no-cache'},
            {'content-type': 'application/json'},
            {'rtt': '200'},
            {"ect": "4g"},
            {'sec-fetch-user': '?1'},
            {"viewport-width": "386"},            
            {'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"'},
            {'upgrade-insecure-requests': '1'}
    ]
    headersHelperFormated = []
    strr = ''
    for i in headersHelper[0:len(headersHelper)-random.randrange(0,len(headersHelper))]:
        strr += ((str(choice(headersHelper)))[1:-1]).strip() + ',' + ' '  
         
    sett.add(strr)    
    headersHelperFormated = list(sett)    
    finHeaders = headFront + headersHelperFormated
    finHeaders[1] = eval("{" + finHeaders[1] + "}")    
    finfinH.update(finHeaders[0])
    finfinH.update(finHeaders[1])   
    return finfinH

# //////////////smart headers start///////////////////////////////

# ////////// grendMather_controller block/////////////////////////////////////

def grendMather_controller(data):
    # print('hello controler')
    flag_test = True
    flag_otziv = True 
 
    try:
        data_upz_hotels_item = data.split('SamsonovNik')[1]
    except Exception as ex:
        # print(f"48____{ex}")
        return [None, black_list]
    try:
        data_upz_hotels_item_dict = eval(data_upz_hotels_item)
    except Exception as ex:
        # print(f"53____{ex}")
        data_upz_hotels_item_dict = data_upz_hotels_item 
    try:
        hotelid = data_upz_hotels_item_dict["hotel_id"] 
    except Exception as ex:
        # print(f"61____{ex}")
        hotelid = 'not found'
    # print(hotelid)
    try:
        prLi_str = data.split('SamsonovNik')[0]
        try:
            prLi = eval(prLi_str)
        except Exception as ex:
            # print(f"str68___{ex}")
            prLi = prLi_str
            pass
    except Exception as ex:
        print(f"str715__proxy_error___{ex}")
        pass 
    try:
        link = data_upz_hotels_item_dict["url"] 
        try:
            fixed_url = re.sub(r'\\/', '/', link)  
        except Exception as ex:
            print(f"122____{ex}")
            fixed_url = data_upz_hotels_item_dict["url"]
    except Exception as ex:
        # print(f"str83___{ex}")
        return None

    try:
        otzivInd = data_upz_hotels_item_dict["otziv"]
    except Exception as ex:
        print(f"140____{ex}")
        return None  
    try:
        if otzivInd == "1" or otzivInd == 1:
            flag_otziv = False
    except:
        pass
    if flag_otziv == False:  
        # print('hello_flag false')
        return None    
    else:
        for _ in range(2):
            try:              
                cc1 = fixed_url.split('/')[-2].strip()
                extract_title = fixed_url.split('/')[-1].split('.')[0].strip()  
                refactor_url  = f'https://www.booking.com/reviewlist.ru.html?cc1={cc1}&pagename={extract_title}&r_lang=&review_topic_category_id=&type=total&score=&sort=&time_of_year=&dist=1&offset=0&rows=100&rurl=&text=&translate=&'
          
            except Exception as ex:
                # print(f"str199___{ex}")
                pass  
            try:
                result_reviews = ''          
                black_list = []
                proxy_item = {       
                    "https": f"http://{choice(prLi)}"          
                } 
                # print(fixed_url)
                try:
                   headerss=random_headers()
                   
                except Exception as ex:
                    print(f"headers281____{ex}")
                # print(headerss)                
                # k = 2 / random.randrange(1, 5)
                # m = 1 / random.randrange(1, 11)
                # g = random.randrange(1, 5)
                # n = round(g + k + m, 2) 
                # time.sleep(n)  
                try: 
                    r = requests.get(refactor_url, headers=headerss, allow_redirects=False, proxies=proxy_item, timeout=(12.15, 30.15))
                    r.raise_for_status()
                    # print(r.status_code)
                    if r.status_code == 404: 
                        return None
                    if r.status_code == 200 and r.text is not None and r.text != '':
                        try:
                            try:
                                result_reviews = review_func.page_scraper_otziv(r.text, hotelid)
                            except:
                                result_reviews = None 

                            if result_reviews is None:
                                continue                                                  
                        except Exception as ex:
                            # print(f"str225___{ex}")      
                            pass
                        break
                    else:
                        continue
                except requests.exceptions.HTTPError as ex:
                    print(f"str44___HTTP error occurred: {ex}") 
                    continue

            except Exception as ex:
                print(f"224____{ex}")
                continue
       
        try:
            return result_reviews
        
        except Exception as ex:
            # print(f"220____{ex}")
            return None
        
# ////////// grendMather_controller block end/////////////////////////////////////
#         
def proxy_reader():
    with open("proxy_booking.txt", encoding="utf-8") as f1:    
        prLi = ''.join(f1.readlines()).split('\n')
        prLi= list(i.strip() for i in prLi)
        prLi = list(filter(lambda item: item != '', prLi))
    return prLi

def father_multiprocessor(data_upz_hotels, cpu_count):    
    try:
        data_upz_hotels_new = eval(data_upz_hotels)
    except Exception as ex:
        data_upz_hotels_new = data_upz_hotels
    try:
        prLi = proxy_reader()
    except Exception as ex:
        pass

    try:
        data_upz_hotels_args = [f"{prLi}SamsonovNik{item}" for item in data_upz_hotels_new]
    except Exception as ex:
        pass

    def call_grendMather_controller(item):
        return grendMather_controller(item)

    try:
        finRes = Parallel(n_jobs=cpu_count, prefer="threads")(delayed(call_grendMather_controller)(item) for item in data_upz_hotels_args)
    except Exception as ex:
        print(f"284STR__Error: {ex}")
        return None

    return finRes


def pattern_cycles(data, cpu_count, n2):
    # print('helo pattern_cycles')
    finRes = []
    try:
        finRes = father_multiprocessor(data, cpu_count)
    except Exception as ex:
        print(f"422____{ex}")
        pass
    try:
        db_writerrr.db_wrtr(finRes, n2)
    except Exception as ex:
        # print(f"378____{ex}")
        pass

def cycles_worker(**args_cycles):
    
    try:        
        n1=int(args_cycles["n1"])
        n2=int(args_cycles["n2"])
        interval=int(args_cycles["interval"])
        from_item=int(args_cycles["from_item"])
        len_items=int(args_cycles["len_items"])
        counter=int(args_cycles["counter"])
        flag_end_cycles=args_cycles["flag_end_cycles"]
        cpu_count = int(args_cycles["cpu_count"])
    except Exception as ex:
        print(f"441____{ex}")

    try:
        if flag_end_cycles == True:
           return print('Finish')
        else:            
            try:
                counter +=1
                n1 = (counter * interval) - interval + 1 + from_item
                n2 = (counter * interval) + from_item
                interval_chekcer = len_items - n2
                if interval_chekcer <= interval:
                    n2 = len_items
                    flag_end_cycles = True
                    # print(f"362___{n2}")
            except Exception as ex:
                # print(f"343____{ex}")
                pass
        
            # print(f"348___{n1, n2}")
            try:  
                print('hello')                
                const_data = db_reader.db_opener(n1, n2)
                # print(const_data)
            except Exception as ex:
                print(f"443____{ex}")
            try:
                pattern_cycles(const_data, cpu_count, n2)
            except:
                pass
        
            cleanup_cache()
            args_cycles = {              
                'n1': n1,
                'n2': n2,
                'interval': interval,
                'from_item': from_item,
                'len_items': len_items,
                'counter': counter,
                'flag_end_cycles': flag_end_cycles,
                'cpu_count': cpu_count
            }
            try:
                cycles_worker(**args_cycles) 
            except Exception as ex:
                # print(f"408____{ex}")
                pass
           

    except Exception as ex:
        # print(f"334____{ex}")
        pass

def cleanup_cache():
    try:
        import os
        try:
            cache_dir = tempfile.mkdtemp()
        except Exception as ex:
            # print(f"386____{ex}")
            pass    
        try:
            if os.path.exists("__pycache__"):
                shutil.rmtree("__pycache__")
        except Exception as ex:
            # print(f"392____{ex}")
            pass  
        try:
            if os.path.exists("./utilsss/__pycache__"):
                shutil.rmtree("./utilsss/__pycache__")
        except Exception as ex:
            print(f"445____{ex}")
            pass 
        try:
            if os.path.exists("./scrapers_funcs/__pycache__"):
                shutil.rmtree("./scrapers_funcs/__pycache__")
        except Exception as ex:
            print(f"451____{ex}")
            pass 
        try:
            if os.path.exists("./db_all/__pycache__"):
                shutil.rmtree("./db_all/__pycache__")
        except Exception as ex:
            print(f"457____{ex}")
            pass   
        try:
            if os.path.exists(cache_dir):
                shutil.rmtree(cache_dir)
        except Exception as ex:
            # print(f"396____{ex}")
            pass
    except Exception as ex:
        print(f"551____{ex}") 

def main():
    args_cycles = {       
        'n1': 0,
        'n2': 0,
        'interval': 5000,
        'from_item': 145000,
        'len_items': 326859,
        'counter': 0,
        'flag_end_cycles': False,
        'cpu_count': 64
    }  

    try:
        cycles_worker(**args_cycles)
    except Exception as ex:
        print(f"454____{ex}")

if __name__ == "__main__":
    try:
        atexit.register(cleanup_cache)
    except Exception as ex:
        print(f"461____{ex}")
    start_time = time.time() 
    main() 
    finish_time = time.time() - start_time
    print(f"Total time:  {math.ceil(finish_time)} сек")
    try:
        sys.exit()
    except Exception as ex:
        print(f"467______{ex}")


