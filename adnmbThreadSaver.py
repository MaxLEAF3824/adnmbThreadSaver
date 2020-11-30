# -*- coding: utf-8 -*-
from selenium import webdriver




def adnmb_thread_getter(fname, cid, PO_only=False, login=True, Browser=1, info=True):
    # ---Initialize variables---
    if Browser == 1:
        browser = webdriver.Chrome()
    elif Browser == 2:
        browser = webdriver.Edge()
    elif Browser == 3:
        browser = webdriver.Firefox()
    else:
        return
    thread_URL = "https://adnmb3.com/m/t/" + str(cid)

    # ---Login in and select cookie---
    if login:
        print("Please log in, click on the cookie list, select one of the cookies and click Apply")
        browser.get("https://adnmb3.com/Member/User/Index/login.html")
        email_input = browser.find_element_by_id("doc-ipt-email-1")
        email_input.send_keys(email)
        pwd_input = browser.find_element_by_id("doc-ipt-pwd-1")
        pwd_input.send_keys(pwd)
        input("If you have completed all the operation above, press Enter to continue...\n")

    # ---Getting Author---
    browser.get(thread_URL + "?page=1")
    print("Getting author......\n")
    author = browser.find_element_by_class_name("h-threads-info-uid").text[3:]

    # ---Getting Pages---
    print("Getting Pages......")
    final_page_link = browser.find_element_by_link_text("末页").get_attribute('href')
    i = len(final_page_link) - 1
    while final_page_link[i] != '=':
        i -= 1
    total_page = int(final_page_link[i + 1:len(final_page_link)])
    if not login:
        total_page = min(99, total_page)

    # ---Save Main Thread---
    js_command = 'document.getElementsByClassName("h-threads-replylist")[0].remove();' \
                 'document.getElementsByClassName("h-threads-reply-btn uk-button uk-button-small")[0].remove();'
    browser.execute_script(js_command)
    if not info:
        js_command = 'document.getElementsByClassName("h-threads-second-col")[0].remove();' \
                     'document.getElementsByClassName("h-threads-first-col")[0].remove();'
        browser.execute_script(js_command)
    main_threads = browser.find_element_by_id("threads_" + str(cid))
    fp = open(fname, 'a', encoding='UTF-8')
    fp.write(main_threads.text)
    fp.write("\n---------Dividing Line---------\n")
    fp.close()
    print("Main thread saved successfully")
    print("Thread Author:%s\nPages:%d\nSaving starting......\n" % (author, total_page))

    # ---Web Crawler---
    fp = open(fname, 'a', encoding='UTF-8')
    for page_num in range(1, total_page + 1):
        print("Downloading Page:%d/%d....." % (page_num, total_page))
        browser.get(thread_URL + "?page=" + str(page_num))
        reply_list = browser.find_elements_by_class_name("h-threads-reply-container")
        for reply in reply_list:
            uid_reply = reply.find_element_by_class_name("h-threads-uid").text[4:]
            content_reply = reply.find_element_by_class_name("h-threads-content").text
            if PO_only:
                if uid_reply == author:
                    if info:
                        fp.write("\n"+reply.text+"\n")
                    else:
                        fp.write("\n" + content_reply + "\n---------Dividing Line---------\n")
            else:
                if info:
                    fp.write("\n" + reply.text + "\n")
                else:
                    fp.write("\n" + content_reply + "\n---------Dividing Line---------\n")
    fp.close()
    browser.close()


if __name__ == "__main__":
    email = ""
    pwd = ""
    thread_id = input("Enter the thread number:\n")
    browser_id = 0
    while browser_id not in ["1", "2", "3"]:
        browser_id = input("Choose your Web browser(Default:Chrome):\n1.Chrome\n2.Edge\n3.Firefox\n")
    browser_id = int(browser_id)
    PO_answer = input("\"Only PO Mode\"?(y/n):\n")
    login_answer = input(
        "Login in?(y/n):\n"
        "(If you do not log in, you are only able to save the first 90 pages of the webpage(mobile version) at most, "
        "that is, the first 891 replies)\n")
    info_answer = input("Save the author and time info?(y/n):\n")
    PO_only_mode = False
    login_mode = True
    info_mode = True
    suffix = "_all"
    if PO_answer in ['', 'y', 'Y', "yes", "Yes", "YES"]:
        PO_only_mode = True
        suffix = "_PO_only"
    if login_answer in ['n', 'N', "no", "No", "NO"]:
        login_mode = False
    if info_answer in ['n', 'N', "no", "No", "NO"]:
        info_mode = False
    try:
        f = open("user_pwd.txt")
        email = f.readline().replace('\n', '')
        pwd = f.readline().replace('\n', '')
        f.close()
    except IOError:
        pass
    adnmb_thread_getter(str(thread_id) + suffix + ".txt", thread_id, PO_only_mode, login_mode, browser_id, info_mode)
    input("Done. Press any key to exit......")
