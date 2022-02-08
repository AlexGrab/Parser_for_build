import datetime

import requests
from bs4 import BeautifulSoup

from get_html_func import get_html


def time_check(time=''):
    timezone = datetime.timezone(offset = datetime.timedelta(hours=5))
    uz_current_time = datetime.datetime.now(timezone)
    numbers = time.split(':')
    hours = int(numbers[0])
    minutes = int(numbers[1])
    time_in_secs = hours * 3600 + minutes * 60
    uz_current_time_in_secs = uz_current_time.hour * 3600 + uz_current_time.minute * 60
    if(uz_current_time_in_secs - time_in_secs <= 700):
        return True
    else:
        return False
def ads_in_profile(ad):
    try:
        html_product = get_html(ad).text
        soup_product = BeautifulSoup(html_product, 'html.parser')
        profile_url = 'https://www.olx.uz' + soup_product.find('a', class_ = 'css-1qj8w5r').get('href')
        html_profile = get_html(profile_url).text
        soup_profile = BeautifulSoup(html_profile, 'html.parser')
        return str(soup_profile).count(r'"wrap"')
    except requests.exceptions.ConnectionError:
        pass
    except AttributeError:
        pass
#url1 = 'https://www.olx.uz/d/obyavlenie/iphone-11-64-gb-white-ID2JXTR.html#c9051cd4d2'
#url2 = 'https://www.olx.uz/d/obyavlenie/kreslo-parikmaherskie-ID1sok4.html'
#url3 = 'https://www.olx.uz/d/obyavlenie/telefon-faks-panasonic-kx-ft987cx-ID2FVNz.html#d677f163fe'
#url4 = 'https://www.olx.uz/d/obyavlenie/shveynye-mashinka-ID2JYKB.html#c9051cd4d2'
#ads_in_profile(url2)

