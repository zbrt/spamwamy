#RECODED AND VERY MUCH IMPROVED BY KLSIY OR ZBRT



from selenium import webdriver
import time
import os
import pyautogui

driver = webdriver.Firefox()
driver.get('http://web.whatsapp.com')
    
driver.set_window_size(1024, 600)
driver.maximize_window()

x=input('Press any key after scanning QR code to login')

def sendimage(xx):
    xx=list(xx)
    try:
        xx.remove('"')
        xx.remove('"')
    except:
        pass
    xx=''.join(xx)

    if(os.path.isabs(xx)==True):
        pass
    else:
        xx=os.path.abspath(xx)

    #print(xx) #line for debugging
    driver.find_element_by_xpath('//span[@data-icon="clip"]').click()
    time.sleep(2)
    driver.find_element_by_xpath('//input[@type="file"]').send_keys(xx)
    while True:
        try:
            driver.find_element_by_xpath('//span[@data-icon="send-light"]').click()
            return
        except:
            pass

def sendimagetxt(xx,text):
    xx=list(xx)
    try:
        xx.remove('"')
        xx.remove('"')
    except:
        pass
    xx=''.join(xx)

    if(os.path.isabs(xx)==True):
        pass
    else:
        xx=os.path.abspath(xx)

    #print(xx) #line for debugging
    driver.find_element_by_xpath('//span[@data-icon="clip"]').click()
    time.sleep(1)
    driver.find_element_by_xpath('//input[@type="file"]').send_keys(xx)
    time.sleep(3)
    driver.find_element_by_xpath('//div[@class="pluggable-input pluggable-input-default"]|//div[@class="pluggable-input-body copyable-text selectable-text"]').send_keys(text)
    while True:
        try:
            driver.find_element_by_xpath('//span[@data-icon="send-light"]').click()
            return
        except:
            pass

while True:
    choice=int(input("Single user spam?-1\nMultiple user spam?-2\nAll user spam-3\n\n"))
    if(choice==1):
        name = input('Name of the user or the group : ')
        msg = input('Put your message here : ')
        count = int(input('Number of times you want to send the same message : '))
        imgchoice=int(input("Add image?\n1->Image without accompanying text\n2->Image with text\n"))
        if(imgchoice==1):
            xx=input("Enter the image path\n")
        elif(imgchoice==2):
            xx=input("Enter the image path\n")
            text=input("Enter the image text\n")
        else:
            pass
        user = driver.find_element_by_xpath('//span[@title="{}"]'.format(name))
        user.click()
        try:
            if(imgchoice==1):
                sendimage(xx)
            elif(imgchoice==2):
                sendimagetxt(xx,text)
            else:
                pass
        except:
            pass
        time.sleep(1)
        msg_box = driver.find_element_by_xpath('//div[@class="pluggable-input-body copyable-text selectable-text"]')
        for i in range(count):
            msg_box.send_keys(msg)
            try:
                driver.find_element_by_xpath('//span[@data-icon="send"]').click()
            except:
                driver.find_element_by_xpath('//button[@class="_2lkdt"]').click()
        
    elif(choice==2):
        listx=[]
        print('Remember:- Input stream will only be stopped when you input -1 as username')
        while True:
            names=input("Enter name of user or group\n")
            listx.append(names)
            try:
                if(int(names)==-1):
                    break
            except:
                pass
        listx.remove('-1')
        msgx=input("Put your message here : ")
        countx=int(input("Number of times you want to send the same message : "))
        imgchoice=int(input("Add image?\n1->Image without accompanying text\n2->Image with text\n"))
        if(imgchoice==1):
            xx=input("Enter the image path\n")
        elif(imgchoice==2):
            xx=input("Enter the image path\n")
            text=input("Enter the image text\n")
        else:
            pass
        print(listx)
        for i in listx:
            userx = driver.find_element_by_xpath('//span[@title="{}"]'.format(i))
            userx.click()
            try:
                if(imgchoice==1):
                    sendimage(xx)
                elif(imgchoice==2):
                    sendimagetxt(xx,text)
                else:
                    pass
            except:
                pass
            msg_boxx = driver.find_element_by_xpath('//div[@class="pluggable-input-body copyable-text selectable-text"]')
            time.sleep(1)
            for j in range(countx):
                msg_boxx.send_keys(msgx)
                try:
                    driver.find_element_by_xpath('//button[@class="_2lkdt"]').click()
                except:
                    driver.find_element_by_xpath('//span[@data-icon="send"]').click()
        listx.clear()

    elif(choice==3):
        cho=input("Are you sure you want to send messages to all users in your contacts?\n1-> YES, 2-> NO\n")
        if(int(cho)==1):
            msgz=input("Put your message here : ")
            countz=int(input("Number of times you want to send the same message : "))
            imgchoice=int(input("Add image?\n1->Image without accompanying text\n2->Image with text\n"))
            if(imgchoice==1):
                xx=input("Enter the image path\n")
            elif(imgchoice==2):
                xx=input("Enter the image path\n")
                text=input("Enter the image text\n")
            else:
                pass
            userx = driver.find_elements_by_xpath('//span[@class="_1wjpf"]')
            for i in userx:
                try:
                    i.click()
                    if(imgchoice==1):
                        sendimage(xx)
                    elif(imgchoice==2):
                        sendimagetxt(xx,text)
                    else:
                        pass
                except:
                    pass
                msg_boxz = driver.find_element_by_xpath('//div[@class="pluggable-input-body copyable-text selectable-text"]')
                time.sleep(4)
                for j in range(countz):
                    msg_boxz.send_keys(msgz)
                    try:
                        driver.find_element_by_xpath('//button[@class="_2lkdt"]').click()
                    except:
                        driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[2]/div[2]/span/div[1]/span/div[1]/div/div[2]/div/div[2]/div[2]/div/div/span').click()
                    try:
                        driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[2]/div[2]/span/div[1]/span/div[1]/div/div[2]/div/div[2]/div[2]/div/div/span').click()
        
    choice=input("Do you want to continue?\n1-> YES\n2-> Anything else-> NO\n")
    if '1' in choice:
        pass
    else:
        break

x=input("Don't do anything that harms the experience of other users.\nUse at your own risk\nPress Enter to exit...")
