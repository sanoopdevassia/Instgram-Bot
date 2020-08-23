from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import imp
import time
driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
driver.get('https://www.instagram.com/')
driver.implicitly_wait(8)
driver.find_element_by_name('username').send_keys(imp.username)
driver.find_element_by_name('password').send_keys(imp.password)
driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div').click()
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()
driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/section/div[3]/div[1]/div/div[2]/div[1]/a').click()
driver.implicitly_wait(5)
driver.find_element_by_partial_link_text("follower").click()
driver.implicitly_wait(10)
followers = []
dialog = driver.find_element_by_xpath("//div[contains(@role, 'dialog')]")
action = ActionChains(driver)
i=0
numberOfFollowersInList = len(dialog.find_elements_by_css_selector('li'))
while(numberOfFollowersInList<409):
    if(i<=5):
        dialog.click()
        i=i+1
    action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
    numberOfFollowersInList = len(dialog.find_elements_by_css_selector('li'))

names = dialog.find_elements_by_tag_name('a')
for name in names:
    if(name.text!=" " and name.text!=""):
        followers.append(name.text)
# print(followers)
driver.find_element_by_xpath('/html/body/div[4]/div/div/div[1]/div/div[2]/button').click()
driver.find_element_by_xpath("//a[contains(@href,'/{}')]".format('following')).click()
dial=driver.find_element_by_xpath('/html/body/div[4]/div')
numberOfFollowingInList = len(dial.find_elements_by_css_selector('li'))
j=0
k=0
while(k<45):
    if(j<=2):
        dial.click()
        j=j+1
    action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
    k=k+1

following=[]
followingnames = dial.find_elements_by_tag_name('a')
for name in followingnames:
    if name.text!= " " and name.text!= "" and name.text!= "HASHTAGS" and name.text!= "PEOPLE":
        following.append(name.text)
# print(following)
nof=[f for f in following if f not in followers]
print(nof)
time.sleep(10)
driver.quit()

