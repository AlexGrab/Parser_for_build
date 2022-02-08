from bs4 import BeautifulSoup
from satisfaction_check import time_check, ads_in_profile

HOST = 'https://www.olx.uz'
def get_content(html):
    final_set = ""
    soup = BeautifulSoup(html, 'html.parser')
    windows = soup.find_all('tr', class_= 'wrap')
    announcements = []
    #print(items)
    for window in windows:
        #print(str(item) + '\n'  + '**************************************')
        #link
        html_link_section = window.find('a', class_ = 'marginright5 link linkWithHash detailsLink')
        text_link_section = str(html_link_section)
        text_link = ''
        for i in range(text_link_section.find('href=') + 6, text_link_section.find('<strong>') - 3):
            text_link += text_link_section[i]
        #time
        html_time_section = window.find_all('small', class_ = 'breadcrumb x-normal')[2].get_text()
        text_time_bad=str(html_time_section)
        text_time = ''
        for i in range(text_time_bad.find(' '), len(text_time_bad) - 1):
            text_time += text_time_bad[i]

        #creating dictionary
        if text_link != '' and time_check(text_time):
            announcements.append(
                {
                   'product_url': text_link,
                    'time': text_time
             }
            )
            final_set += text_link + \
                         '\n' + text_time + \
                         '\n' + str(ads_in_profile(text_link)) + \
                         '\n' + '***************************************************************************' + \
                         '\n'
    return final_set
