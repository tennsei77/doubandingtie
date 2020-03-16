#-*- Coding:UTF-8 -*-
from selenium import webdriver
#实例化谷歌浏览器
from selenium.webdriver.common.action_chains import ActionChains
#导入鼠标动作链
import time

driver = webdriver.Chrome()
#利用谷歌浏览器访问网页 因为豆瓣登录的滑块是固定的，如果是变动的，需要找到完整的图片，看颜色差的对比，看哪里的颜色不相等，再拼接

driver.get('https://www.douban.com/')
#代码将会被淘汰 有新的方法要代替,0表示第一个
driver.switch_to.frame(0)
#元素定位法！只有一个原因 这个位置信息 是错的
driver.find_element_by_xpath('/html/body/div[1]/div[1]/ul[1]/li[2]').click()
driver.find_element_by_xpath('//*[@id="username"]').send_keys('17621207566')
driver.find_element_by_xpath('//*[@id="password"]').send_keys('icyice320401')
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[5]/a').click()#按 登录按钮

time.sleep(2)
driver.switch_to.frame(0)

#每次移动的距离是相等的，先把鼠标按住 然后拖动 然后释放
huakuaiele = driver.find_element_by_xpath('//*[@id="tcaptcha_drag_thumb"]')
ActionChains(driver).click_and_hold(on_element=huakuaiele).perform()
ActionChains(driver).move_to_element_with_offset(to_element=huakuaiele,xoffset=212,yoffset=0).perform()
ActionChains(driver).release().perform()

