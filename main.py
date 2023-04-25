import tkinter
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import selenium.common.exceptions as sel_ex

#
# def wait():
#     time.sleep(3)
#
# window = tkinter.Tk()
# window.title("pause?")
#
# quit_button = tkinter.Button(text="wait", command=wait)
# quit_button.pack()
#



chrome_driver = "C:/Users/2025d/Development/chromedriver"

barel = webdriver.Chrome(executable_path=chrome_driver)

barel.get(url="https://orteil.dashnet.org/cookieclicker/")

time.sleep(10)

cookie = barel.find_element_by_id("bigCookie")

cookies = barel.find_element_by_id("cookies")

barel.find_element_by_class_name("cc_btn_accept_all").click()

clicks = 200

while True:
    for i in range(clicks):
        try:
            cookie.click()
        except sel_ex.ElementClickInterceptedException:
            try:
                barel.find_element_by_class_name("shimmer").click()
            except:
                pass
        if i % 50 == 0:
            try:
                barel.find_element_by_class_name("shimmer").click()
            except:
                pass
    while True:
        try:
            upgrade = barel.find_element_by_xpath("//div[@id='upgrades']/div[@class='crate upgrade enabled']")
        except sel_ex.NoSuchElementException:
            break
        else:
            try:
                barel.execute_script("arguments[0].click();", upgrade)
            except sel_ex.StaleElementReferenceException:
                break
        time.sleep(0.1)

    slaves = barel.find_elements_by_xpath("//div[contains(@class, 'product ') and not(contains(@class, 'toggledOff'))]")
    clicks = 100 * len(slaves)
    while True:
        slaves_ = barel.find_elements_by_xpath("//div[@class='product unlocked enabled']")
        top_rank = 0
        best_affordable = "a"
        for slave in slaves_:
            rank = int(slave.get_attribute("id").replace("product", "")) + 1
            if rank > top_rank:
                top_rank = rank
                best_affordable = slave
        if best_affordable == "a":
            break
        best_affordable.click()
        time.sleep(0.1)

# window.mainloop()
