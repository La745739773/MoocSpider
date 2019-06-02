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
    global UserinfoUrl_List
    print(_dict['name'])
    try:
        browser.get('https:' + str(_dict['url'])) 
    except Exception as identifier:
        return
    try:
        
        evaluation_Btns = browser.find_elements_by_class_name('ga-click')
        for btn in evaluation_Btns:
            if '课程评价' in btn.text:
                btn.click()
            else:
                continue
        try:
            course_score = browser.find_element_by_class_name('ux-mooc-comment-course-comment_head_rating-scores').text     #课程评价分数
            _dict['course_score'] = course_score
        except Exception as identifier:
            _dict['course_score'] = 'None'

        try:
            numberOfevaluation = browser.find_element_by_class_name('ux-mooc-comment-course-comment_head_rating-action_tips').text[1:-3]    #评价数量
            _dict['numberOfevaluation'] = numberOfevaluation
        except Exception as identifier:
            _dict['numberOfevaluation'] = 'None'

        try:
            Comment_paper = browser.find_element_by_class_name('ux-mooc-comment-course-comment_pager')      #获取最后一页的标签
            Last_page = int(Comment_paper.find_elements_by_class_name('ux-pager_itm')[-1].text)
        except Exception as identifier:
            Last_page = 1

        Commentstr_List = []
        for i in range(1,Last_page+1):
            try:
                Comment_Div = browser.find_element_by_class_name('ux-mooc-comment-course-comment_comment-list')
                Comment_List = Comment_Div.find_elements_by_class_name('ux-mooc-comment-course-comment_comment-list_item')
                for comment in Comment_List:
                    content = comment.find_element_by_class_name('ux-mooc-comment-course-comment_comment-list_item_body_content').text
                    UserUrl = comment.find_element_by_class_name('primary-link').get_attribute('href')
                    Comment_Score = len(comment.find_element_by_class_name('star-point').find_elements_by_tag_name('i'))
                    temp_dict = {}
                    temp_dict['Comment'] = content
                    temp_dict['UserUrl'] = UserUrl
                    temp_dict['Comment_Score'] = Comment_Score
                    UserinfoUrl_List.append(UserUrl)
                    Commentstr_List.append(temp_dict)
                try:
                    page_btn  = Comment_paper.find_elements_by_class_name('ux-pager_btn')
                    for pageBtn in page_btn:
                        if pageBtn.text == '下一页':
                            pageBtn.click()
                            time.sleep(1.0)
                except Exception as identifier:
                    pass
            except Exception as identifier:
                continue
        _dict['Comment_List'] = Commentstr_List   
    except Exception as identifier:
        pass
    browser.refresh()
    HarvestedList = []
    Number_List = []
    #ux-dropdown_hd  下拉框类名 ux-dropdown_cnt 
    try:
        #classTime_List = browser.find_elements_by_class_name('f-thide')
        temp_dict = {}
        TeachersList = []
        TeachersList_Label = browser.find_element_by_class_name('m-teachers_teacher-list').find_elements_by_class_name('cnt') #教师列表
        for teacher in TeachersList_Label:
            teacher_name = teacher.find_element_by_class_name('f-fc3').text
            try:
                lector_title = teacher.find_element_by_class_name('lector-title').text
            except Exception as identifier:
                lector_title = teacher.find_element_by_class_name('f-fc6').text
            teacher_dict = {'Name':teacher_name,'Lector':lector_title}
            TeachersList.append(teacher_dict)
        _dict['Teachers'] = TeachersList

        breadcrumb = browser.find_element_by_class_name('breadcrumb') #学科分类
        # Classification_List = breadcrumb.find_elements_by_name('a')
        # temp_Item = []
        # for Classification in Classification_List:
        #     temp_Item.append(Classification.text)
        _dict['Classification'] = breadcrumb.text
        bisJingpin = 'false'
        try:
            bisJingpin = browser.find_element_by_id('j-tag').text
        except Exception as identifier:
            bisJingpin = 'false'
        if bisJingpin == 'false':
            _dict['Bisjingpin'] = '否'
        else:
            _dict['Bisjingpin'] = '是'
        # 课程大纲和课程概述
        try:
            ShowFull_btn = browser.find_element_by_class_name('u-icon-thin-caret-down')
            ShowFull_btn.click()
            CourseOverview_List = browser.find_elements_by_class_name('category-content')
            _tempStr = ''
            for CourseOverview in CourseOverview_List:
                _tempStr += CourseOverview.text
            #_dict['CourseOverview'] = CourseOverview
            #CourseOutline = browser.find_elements_by_class_name('category-content')[1].text
            #_dict['CourseOutline'] = CourseOutline
            _dict['CourseOverview'] = _tempStr
        except Exception as identifier:
            CourseOverview_List = browser.find_elements_by_class_name('category-content')
            _tempStr = ''
            for CourseOverview in CourseOverview_List:
                _tempStr += CourseOverview.text
            _dict['CourseOverview'] = _tempStr
        mouse_dropDown = browser.find_element_by_class_name('ux-dropdown_hd')
        if "第" not in mouse_dropDown.text:
            mouse_dropDown = browser.find_element_by_class_name('ux-dropdown_cnt')
        mouse_dropDown.click()
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
        try:
            temp_ClassTime = browser.find_element_by_class_name('course-enroll-info_course-info_term-select_only-term')
            tempNumber_Student = browser.find_element_by_class_name('course-enroll-info_course-enroll_price-enroll_enroll-count').text[2:-3]
            tempCourse_termInfo = browser.find_element_by_class_name('course-enroll-info_course-info_term-info_term-time').text #开课时间
            tempCourse_termWorkload = browser.find_element_by_class_name('course-enroll-info_course-info_term-workload').text # 学时安排
            temp_dict = {'ClassTime':temp_ClassTime.text}
            temp_dict['Number'] = tempNumber_Student
            temp_dict['Course_termInfo'] = tempCourse_termInfo
            temp_dict['Course_termWorkload'] = tempCourse_termWorkload
            #bisJingpin = 'false'
            # try:
            #     bisJingpin = browser.find_element_by_id('j-tag').text
            # except Exception as identifier:
            #     bisJingpin = 'false'
            # if bisJingpin == 'false':
            #     temp_dict['Bisjingpin'] = '否'
            # else:
            #     temp_dict['Bisjingpin'] = '是'
            Number_List.append(temp_dict)
            _dict['Number_List'] = Number_List
            return _dict
        except Exception as identifier:
            print(_dict['name'] + '  抓取失败')
            return _dict
            pass
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
        time.sleep(1)
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
                    #Teachers_name = ''
                    #TeacherList = course_info.select('.f-fc9')
                    #TeacherList.pop(0)
                    #for teacher in TeacherList:
                        #Teachers_name += teacher.text + ';'
                    course_dict = {'name':temp_url.text,'url':temp_url['href'],'University_name':University_name}
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
                    #Teachers_name = course_info.select('a')[2].text
                    course_dict = {'name':temp_url.text,'url':temp_url['href'],'University_name':University_name}
                    Course_Name_url_List.append(course_dict)
                return
        else:
            content = browser.page_source.encode('utf-8')
            soup = BeautifulSoup(content, 'lxml')
            course_List = soup.select('.g-mn1c')
            for course_info in course_List:
                temp_url = course_info.select('a')[0]#课程url
                University_name = course_info.select('a')[1].text
                #Teachers_name = course_info.select('a')[2].text
                course_dict = {'name':temp_url.text,'url':temp_url['href'],'University_name':University_name}
                Course_Name_url_List.append(course_dict)
            return 
if __name__ == "__main__":
    mode = input('输入爬虫工作模式 1: 输入关键词搜索    2: 输入确定的课程url    ::')
    if mode == '1':
        keyword = input("输入关键词:    ")
        CrawlingByKeyword(keyword)
    elif mode == '2':
        sub_mode = input("是否提供输入文件批量进行此功能: 1 YES 2 NO     ::")
        if  sub_mode == '1':
            file_name = input('输入文件名,文件的格式应该是3列(课程名,开课单位,课程Url)\n::')
            with open(file_name,'r',encoding='utf8') as file:
                lines = file.readlines()
                for line in lines:
                    array = line.split(',')
                    course_dict = {'name':str(array[0]),'url':str(array[2]),'University_name':str(array[1])}
                    Course_Name_url_List.append(course_dict)
            pass
        elif sub_mode == '2':
            confirmed_url = input("输入课程url:     ::")
            course_name = input("输入课程名称:  ::")
            University_name = input("输入开设课程的单位:    ::")
            course_dict = {'name':course_name,'url':confirmed_url,'University_name':University_name}
            Course_Name_url_List.append(course_dict)
    #browser.close()'
    UserinfoUrl_List = []
    for dict in Course_Name_url_List:
        try:
            time.sleep(1.0)
            _dict = Crawling_CourseInformation(dict)
            first_Time = False
            index = 0
            for userUrl in UserinfoUrl_List:
                try:
                    if first_Time == False:
                        js = "window.open(" + '\"' + str(userUrl) + '\"' + ")"
                        browser.execute_script(js)
                        browser.switch_to_window(browser.window_handles[-1])
                        first_Time = True
                    else:
                        browser.get(userUrl)
                        #browser.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't') 
                        #browser.get(userUrl)
                    time.sleep(0.5)
                    userinfo_Div = browser.find_element_by_class_name('u-userInfo-container')
                    Username = userinfo_Div.find_element_by_class_name('u-ui-name').text
                    Usertag = userinfo_Div.find_element_by_class_name('u-ui-tag').text
                    NumofIdols = userinfo_Div.find_element_by_class_name('u-ui-f2f').find_elements_by_tag_name('span')[-2].text
                    NumofFans = userinfo_Div.find_element_by_class_name('u-ui-f2f').find_elements_by_tag_name('span')[-1].text
                    
                    userStudyinfo_Div = browser.find_element_by_class_name('u-selectTab-container')
                    NumofSessions = userStudyinfo_Div.find_elements_by_class_name('item')[0].text
                    NumofDiscussions = userStudyinfo_Div.find_elements_by_class_name('item')[1].text
                    NumofCerts = userStudyinfo_Div.find_elements_by_class_name('item')[2].text

                    userSocialinfo_Div = browser.find_element_by_class_name('u-ui-box-i')
                    TimeofTotaltime = userSocialinfo_Div.find_element_by_class_name('u-ui-time-cont').text
                    NumofTotalDiscussions = userSocialinfo_Div.find_element_by_class_name('u-ui-discuss-cont').text
                    NumofTotalWonders = userinfo_Div.find_element_by_class_name('u-ui-zan-cnt').text

                    bisAcqcert = False
                    cert_btn = browser.find_element_by_class_name('u-st-cert_a5')
                    cert_btn.click()
                    time.sleep(0.5)
                    certCardList = browser.find_element_by_class_name('u-certCard-courseFunc').find_elements_by_class_name('certCard-courseFunc-f')
                    for card in certCardList:
                        cardName = card.text
                        if cardName == _dict['name']:
                            bisAcqcert = True
                            break
                        else:
                            continue
                    print(str(dict['Comment_List'][index]['Comment']))
                    with open("Userinfo.csv",'a') as UserFile:
                        UserFile.write(dict['name'] + ',' + Username + ',' + Usertag + ',' + NumofIdols + ',' + NumofFans + ',' + str(bisAcqcert) + ',' + NumofSessions + ',' + NumofDiscussions + ','
                        + NumofCerts + ',' + NumofTotalDiscussions + ',' + NumofTotalWonders + ',' + TimeofTotaltime + ',' + str(dict['Comment_List'][index]['Comment_Score']) + ',' + str(dict['Comment_List'][index]['Comment']) +  '\n')
                    index = index + 1
                    #dict['Comment_List'].pop(0)
                    time.sleep(0.5)    
                    #browser.close()
                    #browser.switch_to_window(browser.window_handles[0])     
                #ActionChains(browser).key_down(Keys.CONTROL).send_keys("w").key_up(Keys.CONTROL).perform()
                except Exception as identifier:
                    index = index + 1
                    #ActionChains(browser).key_down(Keys.CONTROL).send_keys("w").key_up(Keys.CONTROL).perform()
                    #browser.close()
                    #browser.switch_to_window(browser.window_handles[0])
                    continue
            UserinfoUrl_List.clear()
            if first_Time == True:
                browser.close()
                browser.switch_to_window(browser.window_handles[0])
            with open("output.csv",'a') as file:
                file.write('\n')
                #try:
                #except Exception as identifier:
                    #file.write('\r\n')
                #for dict in Course_Name_url_List:
                try:
                    sum_Studens = 0
                    _time = 0
                    for item in _dict['Number_List']:
                        sum_Studens += int(item['Number'])
                        _time += 1
                    file.write(str(_time) + ',' + str(sum_Studens) + ',')
                except Exception as identifier:
                    pass
                try:
                    file.write(_dict['course_score']+ ',')
                    file.write(_dict['numberOfevaluation'] + ',')
                    file.write(_dict['name'] + ',' + _dict['University_name'] + ',' + _dict['url'] + ',' + _dict['Bisjingpin'] + ',' + _dict['Classification'] + ',')
                    #file.write('\"' + _dict['CourseOutline'] + '\"' + ',' + '\"' + _dict['CourseOverview'] + '\"' + ',')
                    file.write('\"' + str(_dict['CourseOverview']).strip().replace('\n','') + '\"' + ',')
                except Exception as identifier:
                    pass
                try:
                    str_Teachers = '\"'
                    for teacher in _dict['Teachers']:
                        str_Teachers += teacher['Name'] + ':' + teacher['Lector'] + '\r   '
                        #file.write(teacher['Name'] + ':' + teacher['Lector'] + '\n')
                    str_Teachers += '\"'
                    file.write(str_Teachers)
                    file.write(',')
                    Comment_str = '\"'
                    for Comment in _dict['Comment_List']:
                        Comment_str += Comment['Comment'] + '\r'
                        #file.write(Comment['Comment'] + '\n')
                    Comment_str += '\"'
                    file.write(Comment_str)
                    file.write(',')
                except Exception as identifier:
                    pass

                try:
                    for item in _dict['Number_List']:
                        file.write(item['ClassTime'] + ',' + item['Number'] + ',' + item['Course_termInfo'] + ',' + item['Course_termWorkload'] + ',')      
                except Exception as identifier:
                    pass     
        except Exception as identifier:
            print(dict['name'] + '  输出失败')
            continue
    # with open("Userinfo.csv",'a') as UserFile:
    #     try:
    #         for userUrl in UserinfoUrl_List:
    #             #js = "window.open(" + '\"' + str(userUrl) + '\"' + ")"
    #             #browser.execute_script(js)
    #             browser.get('https:' + str(userUrl))
    #             browser.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't') 
    #             browser.get(userUrl)
    #             time.sleep(0.5)
    #             userinfo_Div = browser.find_element_by_class_name('u-userInfo-container')
    #             Username = userinfo_Div.find_element_by_class_name('u-ui-name').text
    #             Usertag = userinfo_Div.find_element_by_class_name('u-ui-tag').text
    #             bisAcqcert = False
    #             cert_btn = browser.find_element_by_class_name('u-st-cert_a5')
    #             cert_btn.click()
    #             certCardList = browser.find_element_by_class_name('u-certCard-courseFunc').find_elements_by_class_name('certCard-courseFunc-f')
    #             for card in certCardList:
    #                 cardName = card.text
    #                 if cardName == _dict['name']:
    #                     bisAcqcert = True
    #                     break
    #                 else:
    #                     continue
    #             UserFile.write(Username + ',' + Usertag + ',' + str(bisAcqcert) + '\n')
    #             #browser.close()
    #     except Exception as identifier:
    #         #browser.close()
    #         pass
    #     #UserinfoUrl_List.clear() 
    print('Done')
    pass