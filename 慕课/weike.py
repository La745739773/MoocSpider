import requests
from bs4 import BeautifulSoup

from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
browser = webdriver.Chrome()
browser.maximize_window()
#browser = webdriver.PhantomJS()
browser.set_page_load_timeout(30) 


host_url = 'http://dasai.cnweike.cn'

weike_course_info_list = []

def parse_course_frame():
    global weike_course_info_list
    time.sleep(1)
    #result_list = browser.find_elements_by_xpath("//div[@id='result-list']//div[@class='search_listView clr']")
    for result in browser.find_elements_by_xpath("//div[@id='result-list']//div[@class='search_listView clr']"):   
        try:
            info_View = result.find_elements_by_tag_name('div')[1]
            course_name = info_View.find_element_by_tag_name('h3').text
            p_subList = info_View.find_elements_by_tag_name('p')
            times_click = p_subList[0].text
            author = p_subList[1].find_elements_by_tag_name('span')[0].text
            author_url = p_subList[1].find_elements_by_tag_name('span')[0].find_element_by_tag_name('a').get_attribute('href')
            upload_time = p_subList[1].find_elements_by_tag_name('span')[1].text



            user_info_view = result.find_elements_by_tag_name('div')[2]
            number_of_support = user_info_view.find_elements_by_tag_name('p')[0].text
            number_of_conmment = user_info_view.find_elements_by_tag_name('p')[1].text
            number_of_save = user_info_view.find_elements_by_tag_name('p')[2].text
            course_dict = {'course_name':course_name,'times_click':times_click,'author_name':author,'upload_time':upload_time,
            'number_of_support':number_of_support,'number_of_conmment':number_of_conmment,'number_of_save':number_of_save}

            js = "window.open(" + '\"' + str(author_url) + '\"' + ")"
            browser.execute_script(js)
            browser.switch_to_window(browser.window_handles[-1])
            time.sleep(0.3)
            author_info_view = browser.find_element_by_xpath("//div[@class='fl w665 ml10']")
            number_of_work = author_info_view.find_element_by_tag_name('p').text
            from_area = author_info_view.find_element_by_tag_name('div').find_elements_by_tag_name('div')[0].text
            author_school = author_info_view.find_element_by_tag_name('div').find_elements_by_tag_name('div')[1].text
            author_subject = author_info_view.find_element_by_tag_name('div').find_elements_by_tag_name('div')[2].text
            browser.close()
            browser.switch_to_window(browser.window_handles[0])
            course_dict['number_of_work'] = number_of_work
            course_dict['from_area'] = from_area
            course_dict['author_school'] = author_school
            course_dict['author_subject'] = author_subject.replace(',','-')
            weike_course_info_list.append(course_dict)
           
        except Exception as identifier:
            print(result.text)
            pass


if __name__ == "__main__":
    #global weike_course_info_list
    browser.get(host_url)
    button_wkzp =  browser.find_element_by_xpath('//div[@class=\'nav-menu\']/a[text()=\'微课作品\']')  #微课作品按钮
    button_wkzp.click()
    button_subject_div = browser.find_elements_by_xpath("//div[@id='selPointSub']")
    keyword = input('输入关键词:        ::')
    button_subject = browser.find_elements_by_xpath("//div[@id='selPointSub']/a")
    for subject in button_subject:
        if subject.text == keyword:
            subject.click()
            break
    
    numof_total_course = browser.find_element_by_xpath("//div[@class='w960 bc h30 mt20 clr border_b']/div[@class='fl']/span").text.encode('utf-8').decode()

    last_page = int(int(numof_total_course) / 10) + 1
    for i in range(1,last_page):
        parse_course_frame()
        time.sleep(1)
        next_page_btn = browser.find_element_by_xpath("//li[@class='page-next paging_but']")
        next_page_btn.click()

        with open('wike.csv','a',encoding='utf8') as file:
            for dict in weike_course_info_list:
                file.write(str(dict['course_name']) + ',' + str(dict['times_click']) + ',' + str(dict['upload_time']) + ',' + 
                str(dict['number_of_support']) + ',' + str(dict['number_of_conmment']) + ',' + str(dict['number_of_save']) + ','
                + str(dict['author_name']) + ',' + str(dict['number_of_work']) + ',' + str(dict['from_area']) + ',' + str(dict['author_school']) + 
                ',' + str(dict['author_subject']) + '\n')
            weike_course_info_list.clear()

