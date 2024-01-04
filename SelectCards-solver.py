from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
def click(x):
    driver.find_element(By.XPATH, x).click()
def bit(x,i):
    return (((x)>>(i))&1)

#ChromeDriverをインストール？している（これをしないとちゃんと動かない）
import requests
res = requests.get('https://chromedriver.storage.googleapis.com/LATEST_RELEASE')
driver = webdriver.Chrome(ChromeDriverManager(res.text).install())
# xpaths = ['//*[@id="root"]/div/div/div[3]/div[2]/div[1]',
#           '//*[@id="root"]/div/div/div[3]/div[2]/div[2]',
#           '//*[@id="root"]/div/div/div[3]/div[2]/div[3]']
xpaths = ['//*[@id="root"]/div/div/div[3]/div[2]/div['+str(i)+']' for i in range(1,11)]
baseurl = "https://kusira-select-cards.netlify.app/"
driver.get(baseurl) #開く
time.sleep(2) #この2秒で名前を入力しよう
click('//*[@id="root"]/div/div/div[1]/div[1]') #開始ボタンを押す
starttime = time.time() #時間計測用
#while abs(time.time()-starttime)<60: #こっちは60秒で打ち切り
while 1:
    n = 10
    m = int(driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div[3]/div[1]/div[2]/p[2]').text)
    a = [int(driver.find_element(By.XPATH,xpaths[i]).text) for i in range(n)]
    print(a)
    #部分和問題を解く。bit全探索
    for i in range(1<<10):
        if sum([a[j] if bit(i,j) else 0 for j in range(10)])==m:
            for j in range(10):
                if bit(i,j):
                    driver.find_element(By.XPATH,xpaths[j]).click()
            break
    time.sleep(0.3) #0.25だと動かない
time.sleep(10)
