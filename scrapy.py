from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium import webdriver
import urllib.request
opener=urllib.request.build_opener()
import time 



wd = webdriver.Firefox(executable_path="/mnt/e/20202/GR1/crawl-image/geckodriver")
wd.get("https://google.com")


input = wd.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')

input.send_keys('wildfires')
input.send_keys(Keys.RETURN)

time.sleep(2)

wd.find_element_by_xpath('/html/body/div[7]/div/div[4]/div/div[1]/div/div[1]/div/div[2]/a').click()

last_height = wd.execute_script('return document.body.scrollHeight')
while True:
    wd.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(2)
    new_height = wd.execute_script('return document.body.scrollHeight')
    try:
        wd.find_element_by_xpath('//*[@id="islmp"]/div/div/div/div/div[3]/div[2]/input').click()
        time.sleep(2)
    except:
        pass
    if new_height == last_height:
        break
    last_height = new_height

link = []


for i in range(1, 50):
    
    if i % 25 != 0:
        wd.find_element_by_xpath('/html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div/div[1]/span/div[1]/div[1]/div[' + str(i) + ']/a[1]').click()
        time.sleep(3)
        a = wd.find_element_by_xpath('/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div/div[2]/a/img').get_attribute('src')
        if (("http" in a) and ('encrypt' not in a)):
            link.append(a)
    

opener=urllib.request.build_opener()
opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
urllib.request.install_opener(opener)
for i in range(len(link)):
    urllib.request.urlretrieve(link[i], filename="/mnt/e/20202/GR1/crawl-image/wildfires/"+ str(i)+".jpeg")
    
        
        


