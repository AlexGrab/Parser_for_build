import datetime
from get_html_func import get_html
from parse_main import get_content

URLS = [
    'https://www.olx.uz/detskiy-mir/',
    'https://www.olx.uz/dom-i-sad/',
    'https://www.olx.uz/elektronika/',
    'https://www.olx.uz/hobbi-otdyh-i-sport/',
]
def final_parse():
    #uz time
    timezone = datetime.timezone(offset = datetime.timedelta(hours=5))
    uz_current_time = datetime.datetime.now(timezone)
    print(uz_current_time)
    #parse different chapters
    chapter_content = ''
    for url in URLS:
        #print('New chapter')
        #print(url)
        #print('*************************************')
        #print('*************************************')
        #print('*************************************')
        html = get_html(url)
        chapter_content += get_content(html.text)
    return chapter_content
#print(final_parse())