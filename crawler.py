from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import time
import pandas as pd

from tool import read_csv, loadWebsite, getComment, getPost, getReact, getNumberCommentShare, getReactExtend
from login import login


# Set up fb posts and Chrome options
data = 'data/websites.csv'
websites = read_csv(data)

chromeOptions = Options()
chromeOptions.add_argument("--incognito")
chromeOptions.add_argument('--start-maximized')

driver = webdriver.Chrome(chromeOptions)

# Login
username = "zds34054@dcobe.com"
password = "khdl123@"
login(driver, username, password)

time.sleep(2)

# Data output
postData = ""
commentData = []
reactData = ""
CmtShareData = []
reactExtendData = {}
df = pd.DataFrame({
    'link': [],
    'post_text': [],
    'comments': [],
    'reacts': [],
    'reacts_extend': [],
    'comment_num': [],
    'share_num': []
})

for website in websites:
    loadWebsite(driver, website)
    postData = getPost(driver, website)
    commentData = getComment(driver, website)
    reactData = getReact(driver, website)
    reactExtendData = getReactExtend(driver, website)
    CmtShareData = getNumberCommentShare(driver, website)
    newRow = pd.DataFrame({
        'link': website,
        'post_text': postData,
        'comments': [commentData],
        'reacts': reactData,
        'reacts_extend': reactExtendData,
        'comment_num': CmtShareData[0],
        'share_num': CmtShareData[1]
    })
    df = pd.concat([df, newRow], ignore_index=True)
    df.to_csv('data/demo2.csv')

driver.quit()