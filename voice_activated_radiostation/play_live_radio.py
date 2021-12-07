# Below is the Xpath of the play button from https://onlineradiobox.com/us/?cs=in.startamil for startamil fm
# //*[@id="b_top_play

# pre-requisite: Install relevant chromium driver from https://chromedriver.chromium.org/downloads

from selenium import webdriver
browser = webdriver.Chrome(executable_path='./chromedriver')
browser.get("https://onlineradiobox.com/us/?cs=in.startamil")
button = browser.find_element_by_xpath('//*[@id="b_top_play"]')
button.click()
