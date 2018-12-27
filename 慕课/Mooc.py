import requests
from bs4 import BeautifulSoup

from selenium import webdriver

browser = webdriver.Chrome()
browser.set_page_load_timeout(30) 

Cookie = 'EDUWEBDEVICE=f1619e9de9e9486b97712bfb258bd202; WM_TID=BVtYiTp4IjhFEBAQVQZ4LxdCdxI9jqJE; NTESSTUDYSI=6a7fe7fb0b724c9e973c80f33ff31739; utm="eyJjIjoiIiwiY3QiOiIiLCJpIjoiIiwibSI6IiIsInMiOiIiLCJ0IjoiIn0=|aHR0cHM6Ly93d3cuYmFpZHUuY29tL2xpbms/dXJsPU1talpOTTBWaWtVajVPNVN1cVpCaXJKRXM0RUZXclNvNjM2MUdVd2ZscDllS2NmZFN1VjhRbjVmY0xKRXRPUHMmd2Q9JmVxaWQ9OWQwNzgwMWEwMDAxZDFjMDAwMDAwMDAyNWMwNjIzOTg="; hb_MA-A976-948FFA05E931_source=www.baidu.com; __utma=63145271.1470496361.1542183794.1542183794.1543906207.2; __utmc=63145271; __utmz=63145271.1543906207.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; WM_NI=rBX7LV8cH2L5dye9q6yI7IfGOUJRKU08N4A8FN%2BufXERLk%2BZKDjgJRPSJIEEbO6v%2F%2FL%2Fs9LY9KCRLBC5US%2FgO4gVCtA4EVr3n21sOIHDAizdfdoCDw%2FSW%2Fo6w9UoO85fcUY%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6ee9af03f9499f7b3c17282968fa3d85f829e9ebabb5caee7fa92f23fa8edadafd52af0fea7c3b92ab29e98d8cf5efcbd88d3cf3fa8a7abdaf43ebb97f9aae54d8d8b86b3ca5ff4e882d5c4348692e596e554878e848caa52899ca688c95a948d86aac84fa291fa97ae2590f1bddacf53fb958db3cf4a81eb9bb4ae6d8deca9b7c28083ec8bb7f139aeeeff94ce438c9c8f8af970a6bca1a4c77ded8d99d0ee3eb5e79b90ce34f7baadb6dc37e2a3; NTES_YD_PASSPORT=aYPwrf4OKiwbw1rIRmQOFGMvmVt3oNl2WrHzIf5VASW.TirgUzYxslSYW2keghTgDQJMKLADGGD8KlHcHGTjnmLSVbOWRw0vDt9qO1VmOY6aTI.7XdA_MyKk25kn06mPq1BeQDieUIiyK1VgNOF8FYlKl0lfHXOmNZPFu7Z_KY3OXbcPF07CKGJ5dULpQzosjluhGlgP.qwkg; STUDY_INFO="yd.c82456d4b00d4672a@163.com|8|1030266772|1543906257857"; STUDY_SESS="peYE+yknlaVoQsX3X/zhhPae9tRgOlSS55+xWKu7YgG78iQ99p1grvYH1y1q41Nb5hpt7bCWn12GItGQt3G57toU7REeBJvGDW47YxA8Ds44Neknj+JjEjEVQ3F1R2QcNxe4bsGfVN8pHnbPE883zATlplNQ0yC36LFQjFvGVh8Lhur2Nm2wEb9HcEikV+3FTI8+lZKyHhiycNQo+g+/oA=="; STUDY_PERSIST="tZv0lpJ8Eq8F+c+8wQ5UBq4/eoSgfHIL5gPekNbeTYy8QZsXjWE0jqHyrFwmn8ExJh2gCyBid8jaQGEc0R/ITjvbNnyusDDl/mo6B0z9owRIdQhdMRHCeHGxUZgfOcw9VkBraE5l3XSUWd/GOxGkwJYW/fXsNvBqQ+U0jtyBJOc6ab2bQoqNPeJp1us92v6kR5cfVC+Pa2NRz2i5Yh1PMVJ3oGKOn0/g6DF1UfTSXgnZgpjCC7Iso4RP9U87vJE8LtaQzUT1ovP2MqtW5+L3Hw+PvH8+tZRDonbf7gEH7JU="; NETEASE_WDA_UID=1030266772#|#1505897292313; __utmb=63145271.27.9.1543906403789; NTES_YD_SESS=kJQRWizqj7sp0zEfYzBzisl0Jy.X8.VrsZp6amlGhC6dHLluwJTMb9YTfeBOuDHuUIG_hQRUssUuKJgwsPFzVcQ0_Q4lYrAghhyBugJ1Mg4pyRYUqgG.Es6JARNRrGx2FiS7ax9P80afzlzoGQyFpH.W9ugSBj5zdvNB5WiU2GEJvlMPkGUp7NB7Ee3HYBmNWj_dQO9cIxW85skshdziLNpJpoaJidkK6; S_INFO=1543906431|0|3&80##|17751790203; P_INFO=17751790203|1543906431|1|imooc|00&99|null&null&null#jis&320100#10#0|&0|null|17751790203; bpmns=1'

Host_url = 'https://www.icourse163.org'

Course_Name_url_List = []



def HarvestClasstime(browser_text):
    classTime_List = browser_text.find_elements_by_class_name('f-thide')
    temp_List = []
    for classTime in classTime_List:
        if "第" in classTime.text:
            temp_List.append(classTime)
    return temp_List



def Crawling_CourseInformation(_dict):
    print(_dict['name'])
    try:
        browser.get('https:' + str(_dict['url'])) 
    except Exception as identifier:
        return

    HarvestedList = []
    Number_List = []
    #ux-dropdown_hd  下拉框类名 ux-dropdown_cnt 
    try:
        mouse_dropDown = browser.find_element_by_class_name('ux-dropdown_hd')
        if "第" not in mouse_dropDown.text:
            mouse_dropDown = browser.find_element_by_class_name('ux-dropdown_cnt')
        mouse_dropDown.click()
        #classTime_List = browser.find_elements_by_class_name('f-thide')
        time = 1 #第一次开课
        while True:
            temp_List = HarvestClasstime(browser)
            for classTime in temp_List:
                if classTime.text in HarvestedList:
                    continue
                temp_dict = {'ClassTime':classTime.text}
                HarvestedList.append(classTime.text)
                print(classTime.text)
                classTime.click() #换到新一页 
                Number_Student = browser.find_element_by_class_name('course-enroll-info_course-enroll_price-enroll_enroll-count').text[2:-3]
                #print(Number_Student)
                Course_termInfo = browser.find_element_by_class_name('course-enroll-info_course-info_term-info_term-time').text #开课时间
                Course_termWorkload = browser.find_element_by_class_name('course-enroll-info_course-info_term-workload').text # 学时安排
                temp_dict['Number'] = Number_Student
                temp_dict['Course_termInfo'] = Course_termInfo
                temp_dict['Course_termWorkload'] = Course_termWorkload
                bisJingpin = 'false'
                try:
                    bisJingpin = browser.find_element_by_id('j-tag').text
                except Exception as identifier:
                    bisJingpin = 'false'
                if bisJingpin == 'false':
                    temp_dict['Bisjingpin'] = '否'
                else:
                    temp_dict['Bisjingpin'] = '是'
                Number_List.append(temp_dict)
                mouse_dropDown = browser.find_element_by_class_name('ux-dropdown_hd')
                if "第" not in mouse_dropDown.text:
                    mouse_dropDown = browser.find_element_by_class_name('ux-dropdown_cnt')
                mouse_dropDown.click()
                break
            if len(temp_List) == len(HarvestedList) + 1:
                break
        _dict['Number_List'] = Number_List
        return _dict
    except Exception as identifier:  #没有找到下拉框4
        temp_ClassTime = browser.find_element_by_class_name('course-enroll-info_course-info_term-select_only-term')
        tempNumber_Student = browser.find_element_by_class_name('course-enroll-info_course-enroll_price-enroll_enroll-count').text[2:-3]
        tempCourse_termInfo = browser.find_element_by_class_name('course-enroll-info_course-info_term-info_term-time').text #开课时间
        tempCourse_termWorkload = browser.find_element_by_class_name('course-enroll-info_course-info_term-workload').text # 学时安排
        temp_dict = {'ClassTime':temp_ClassTime.text}
        temp_dict['Number'] = tempNumber_Student
        temp_dict['Course_termInfo'] = tempCourse_termInfo
        temp_dict['Course_termWorkload'] = tempCourse_termWorkload
        bisJingpin = 'false'
        try:
            bisJingpin = browser.find_element_by_id('j-tag').text
        except Exception as identifier:
            bisJingpin = 'false'
        if bisJingpin == 'false':
            temp_dict['Bisjingpin'] = '否'
        else:
            temp_dict['Bisjingpin'] = '是'
        Number_List.append(temp_dict)
        _dict['Number_List'] = Number_List
        pass

    # for classTime in temp_List:
    #     try:
    #         if "第" in classTime.text:
    #             HarvestedList.append(classTime.text)
    #             classTime.click() #换到新一页 
    #             Number_Student = browser.find_element_by_class_name('course-enroll-info_course-enroll_price-enroll_enroll-count').text[2:-3]
    #             print(Number_Student)
    #             mouse_dropDown = browser.find_element_by_class_name('ux-dropdown_hd')
    #             if "第" not in mouse_dropDown.text:
    #                 mouse_dropDown = browser.find_element_by_class_name('ux-dropdown_cnt')
    #             mouse_dropDown.click()
    #     except Exception as identifier:
    #         continue

    pass


def CrawlingByKeyword(keyWord):
    # 首先根据输入关键词 爬取所有课程名，讲课单位 教师列表 详情url
    url = Host_url + '/search.htm?search=' + keyWord + '#' + 'type=30&orderBy=0&pageIndex=2'
    headers = {
        'Host':'www.icourse163.org',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
        #'Cookie':Cookie
    }
    browser.get(url)  
    # content = browser.page_source.encode('utf-8')
    # soup = BeautifulSoup(content, 'lxml')
    # # course_List = soup.select('.cnt')
    # #course_List = browser.find_elements_by_class_name('cnt')
    # course_List = soup.select('.g-mn1c')
    # for course_info in course_List:
    #     temp_url = course_info.select('a')[0]#课程url
    #     University_name = course_info.select('a')[1].text
    #     Teachers_name = course_info.select('a')[2].text
    #     course_dict = {'name':temp_url.text,'url':temp_url['href'],'University_name':University_name,'Teachers_name':Teachers_name}
    #     Course_Name_url_List.append(course_dict)
    # print("下一页")
        #print(temp_url.text)
    while True:
        Nextpage_List = browser.find_elements_by_class_name('th-bk-main-gh')
        if(len(Nextpage_List) != 0):
            flag = False
            for page in Nextpage_List:
                if page.text != '下一页':
                    continue
                flag = True
                page.click()
                content = browser.page_source.encode('utf-8')
                soup = BeautifulSoup(content, 'lxml')
                course_List = soup.select('.g-mn1c')
                for course_info in course_List:
                    temp_url = course_info.select('a')[0]#课程url
                    University_name = course_info.select('a')[1].text
                    Teachers_name = ''
                    TeacherList = course_info.select('.f-fc9')
                    TeacherList.pop(0)
                    for teacher in TeacherList:
                        Teachers_name += teacher.text + ';'
                    course_dict = {'name':temp_url.text,'url':temp_url['href'],'University_name':University_name,'Teachers_name':Teachers_name}
                    Course_Name_url_List.append(course_dict)
                print("下一页")
                    #print(temp_url.text)
            if flag == False:
                content = browser.page_source.encode('utf-8')
                soup = BeautifulSoup(content, 'lxml')
                course_List = soup.select('.g-mn1c')
                for course_info in course_List:
                    temp_url = course_info.select('a')[0]#课程url
                    University_name = course_info.select('a')[1].text
                    Teachers_name = course_info.select('a')[2].text
                    course_dict = {'name':temp_url.text,'url':temp_url['href'],'University_name':University_name,'Teachers_name':Teachers_name}
                    Course_Name_url_List.append(course_dict)
                return
if __name__ == "__main__":
    CrawlingByKeyword('地理')
    #browser.close()
    for dict in Course_Name_url_List:
        dict = Crawling_CourseInformation(dict)

    with open("output.csv",'w') as file:
        for dict in Course_Name_url_List:
            file.write(dict['name'] + ',' + dict['University_name'] + ',' + dict['Teachers_name'] + ',' + dict['url']
            + ',' + dict['Number_List'][0]['Bisjingpin'] + ',')
            for item in dict['Number_List']:
                file.write(item['ClassTime'] + ',' + item['Number'] + ',' + item['Course_termInfo'] + ',' + item['Course_termWorkload'] + ',')
            file.write('\n')
    pass