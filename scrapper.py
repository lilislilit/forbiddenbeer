from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome()
driver.get("https://untappd.com/v/mirbir/2135007?ng_menu_id=19d17d34-8222-4022-aca1-c26ed3b09a29")

elem = driver.find_element_by_class_name("search-text")
elem.clear()
#elem.send_keys("ale")
#elem.send_keys(Keys.RETURN)
# Get scroll height
max_beer_loop = 2
while max_beer_loop > 0:
    try:
        loadMoreButton = driver.find_element_by_class_name('more-list-items')
        time.sleep(2)
        driver.execute_script('var scrollingElement = (document.scrollingElement || document.body);scrollingElement.scrollTop = scrollingElement.scrollHeight;')
        time.sleep(5)
        driver.execute_script('''var x = document.getElementsByClassName("more-list-items"); 
                                x[0].click();''' )
        time.sleep(2)
        max_beer_loop -= 1
    except Exception as e:
        print(e)
        break
print("Complete")
html_doc = driver.page_source
f = open("myfile.html", "w",  encoding="utf-8")
f.write(html_doc)
f.close()
driver.close()


