from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
def format_string(str,length):
    if (length==1):
        return str
    while(len(str)<length):
        str+=" "
    return str
option=Options()
# option.add_argument("--headless")
driver=Chrome(executable_path="/home/tharikh/scrapz/chromedriver",chrome_options=option)
url="https://tkmce.linways.com/student/parent.php"
driver.get(url)
username=input("enter user name")
driver.find_element_by_name('studentAccount').clear()
driver.find_element_by_name('studentAccount').send_keys('{}'.format(username))
driver.find_element_by_name('parentPassword').clear()
driver.find_element_by_name('parentPassword').send_keys('{}'.format(username))
driver.find_element_by_tag_name('button').click()
driver.find_element_by_xpath('./html/body/div[4]/div[2]/div/div[1]/div[2]/div/div[2]/a').click()
driver.find_element_by_xpath('./html/body/div[3]/div[2]/div/div[1]/div[2]/div/div[2]/a[4]').click()
driver.implicitly_wait(3)
temp=driver.find_elements_by_tag_name('tr')
with open("temp.txt","w") as f:
    for i in temp:
        collection=driver.find_elements_by_tag_name('td') or driver.find_elements_by_tag_name('th')
        for j in collection:
            str=format_string(j.text,15)
            f.write(str)
driver.close()