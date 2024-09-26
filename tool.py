from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.action_chains import ActionChains

import pandas as pd
import time
import re
import csv


def read_csv(file):
    websites = []
    with open(file, mode = 'r') as file:
        csv_websites = csv.reader(file)
        for website in csv_websites:
            websites.append(website[0])
    
    return websites


def loadWebsite(driver, website):
    driver.get(website)

    time.sleep(5)

    replyPattern = r'\d+ phản hồi'
    lastHeight = driver.execute_script("return document.body.scrollHeight")

    time.sleep(5)

    loopCount = 0
    while True:
        try:
            sortingButton = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div/div/div[13]/div/div/div[4]/div/div/div[2]/div[2]/div/div/span/div')
            sortingButton.click()
            time.sleep(5)

            allComments = driver.find_element(By.XPATH, "//span[contains(text(), 'Tất cả bình luận')]")
            allComments.click()
            time.sleep(5)
        except:
            print('All Comments Error')

        time.sleep(5)
    
        try:
            replies = driver.find_elements(By.XPATH, '//span[@class="x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x xudqn12 x3x7a5m x6prxxf xvq8zen x1s688f xi81zsa" and @dir="auto"]')
            # print("Element found:", expandComments)
        except NoSuchElementException:
            print("Elements not found")

        if len(replies) > 0:
            count = 0
            for reply in replies:
                action = ActionChains(driver)
                try:
                    text = reply.text
                except StaleElementReferenceException:
                    continue
                if re.search(replyPattern, text):
                    print(1)
                else:
                    count += 1
                    continue

                try:
                    action.move_to_element(reply).click().perform()
                    time.sleep(1)
                    count += 1
                except:
                    try:
                        driver.execute_script("arguments[0].click();", reply)
                        time.sleep(2)
                        count += 1
                    except:
                        continue
            if len(replies) - count > 0:
                print('replies issue:', len(replies) - count)
            time.sleep(1)
        else:
            pass

        while True:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(5)
            newHeight = driver.execute_script("return document.body.scrollHeight")
            if newHeight == lastHeight:
                print('End')
                loopCount += 1
                break
            lastHeight = newHeight
            loopCount = 0
        
        if loopCount > 1:
            break


def getComment(driver, website):
    commentData = []

    # time.sleep(10)

    # clearLogin = driver.find_element(By.XPATH, '//div[@class ="x92rtbv x10l6tqk x1tk7jg1 x1vjfegm"]')
    # clearLogin.click()

    comments = driver.find_elements(By.XPATH, '//div[@class="xdj266r x11i5rnm xat24cr x1mh8g0r x1vvkbs"]')

    for comment in comments:
        commentData.append(comment.text)
    
    return commentData


def getPost(driver, website):
    postContent = ""

    time.sleep(5)

    try:
        postElement = driver.find_element(
            By.XPATH, '//span[@class="x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x xudqn12 x3x7a5m x6prxxf xvq8zen xo1l8bm xzsf02u x1yc453h"]')
        postContent = postElement.text
        print(f'Link: {website}, Post content found')
    except NoSuchElementException:
        postContent = "Content not found"
        print(f'Link: {website}, Post content not found')

    return postContent


def getReact(driver, website):
    reactCount = ""

    time.sleep(5)

    try:
        reactElement = driver.find_element(
            By.XPATH, '//span[@class="xt0b8zv x1e558r4"]')
        reactCount = reactElement.text
        print(f'Link: {website}, Number comments and shares found')
    except NoSuchElementException:
        reactCount = "0"
        print(f'Link: {website}, Number comments and shares not found')

    return reactCount

def getReactExtend(driver, website):
    reactExtendCount = {
        'like': [],
        'love': [],
        'care': [],
        'haha': [],
        'wow': [],
        'sad': [],
        'angry': [] 
    }

    likeCount = "0"
    loveCount = "0"
    careCount = "0"
    hahaCount = "0"
    wowCount = "0"
    sadCount = "0"
    angryCount = "0"

    time.sleep(5)

    # Extend facebook reactions list
    try:
        reactExtendElement = driver.find_element(
            By.XPATH, '//span[@class="xt0b8zv x1e558r4"]')
        reactExtendElement.click()
        print(f'Link: {website}, Reacts extend found')
    except NoSuchElementException:
        print(f'Link: {website}, Reacts extend not found')

    # Further extend
    try:
        furtherExtendElement = driver.find_element(
            By.XPATH, '/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[1]/div/div/div/div[2]/div[9]/div/div[1]/span')
        furtherExtendElement.click()
        print(f'Link: {website}, Further extend found')
    except NoSuchElementException:
        print(f'Link: {website}, No further extend not found')


    # Like count
    try:
        likeElement = driver.find_element(
            By.XPATH, '/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[1]/div/div/div/div[2]/div[3]/div[1]/span')
        likeCount = likeElement.text
        print(f'Link: {website}, Like found')
    except NoSuchElementException:
        print(f'Link: {website}, No like')

    # Love count
    try:
        loveElement = driver.find_element(
            By.XPATH, '/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[1]/div/div/div/div[2]/div[4]/div[1]/span')
        loveCount = loveElement.text
        print(f'Link: {website}, Love found')
    except NoSuchElementException:
        print(f'Link: {website}, No love')

    # Care count
    try:
        careElement = driver.find_element(
            By.XPATH, '/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div/div/div/div/div[1]/div/div[2]/div[2]/div/div/span')
        careCount = careElement.text
        print(f'Link: {website}, Care found')
    except NoSuchElementException:
        print(f'Link: {website}, No care')

    # Haha count
    try:
        hahaElement = driver.find_element(
            By.XPATH, '/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div/div/div/div/div[1]/div/div[1]/div[2]/div/div/span')
        hahaCount = hahaElement.text
        print(f'Link: {website}, Haha found')
    except NoSuchElementException:
        print(f'Link: {website}, No haha')

    # Wow count
    try:
        wowElement = driver.find_element(
            By.XPATH, '/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[1]/div/div/div/div[2]/div[5]/div[1]/span')
        wowCount = wowElement.text
        print(f'Link: {website}, Wow found')
    except NoSuchElementException:
        print(f'Link: {website}, No wow')

    # Sad count
    try:
        sadElement = driver.find_element(
            By.XPATH, '/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div/div/div/div/div[1]/div/div[3]/div[2]/div/div/span')
        sadCount = sadElement.text
        print(f'Link: {website}, Sad found')
    except NoSuchElementException:
        print(f'Link: {website}, No sad')

    # Angry count
    try:
        angryElement = driver.find_element(
            By.XPATH, '/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div/div/div/div/div[1]/div/div[4]/div[2]/div[1]/div/span')
        angryCount = angryElement.text
        print(f'Link: {website}, Angry found')
    except NoSuchElementException:
        print(f'Link: {website}, No angry')

    reactExtendCount_tmp = {
        'like': likeCount,
        'love': loveCount,
        'care': careCount,
        'haha': hahaCount,
        'wow': wowCount,
        'sad': sadCount,
        'angry': angryCount 
    }

    reactExtendCount = pd.concat([reactExtendCount, reactExtendCount_tmp], ignore_index=True)

    return reactExtendCount


def getNumberCommentShare(driver, website):
    CmtShareCount = []

    time.sleep(5)

    try:
        reactElement = driver.find_element(
            By.XPATH, '//span[@class="html-span xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x1hl2dhg x16tdsg8 x1vvkbs x1sur9pj xkrqix3"]')
        print(f'Link: {website}, Number comments and shares found')
    except NoSuchElementException:
        print(f'Link: {website}, Number comments and shares not found')

        for react in reactElement:
            CmtShareCount.append(react.text)

    return CmtShareCount