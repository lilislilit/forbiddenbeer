import sys

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class BeerScrapper:
    def __init__(self, source, query=''):
        self.source = f'https://untappd.com/{source}'
        self.query = query

    def get_html(self):
        print(self.source)
        with webdriver.Chrome() as driver:
            driver.get(self.source)
            if self.query != '':
                elem = self.driver.find_element_by_class_name("search-text")
                elem.clear()
                elem.send_keys("ale")
                elem.send_keys(Keys.RETURN)
            max_beer_loop = 10
            while max_beer_loop > 0:
                try:
                    time.sleep(2)
                    driver.execute_script(
                    'var scrollingElement = (document.scrollingElement || document.body);'
                    'scrollingElement.scrollTop = scrollingElement.scrollHeight;')
                    time.sleep(5)
                    #TODO Figure out way to trigger a correct loadmore event
                    driver.execute_script('''var x = document.getElementsByClassName("more-list-items"); 
                                        x[0].click();''')
                    time.sleep(2)
                    max_beer_loop -= 1
                except Exception as e:
                    print(e)
                    break
            print("Complete")
            return driver.page_source


if __name__ == "__main__":
    if len(sys.argv) < 2:
        default_url = 'v/mirbir/2135007?ng_menu_id=19d17d34-8222-4022-aca1-c26ed3b09a29'
    else:
        default_url = sys.argv[1]
    html_doc = BeerScrapper(default_url).get_html()
    f = open('my_file.html', 'w', encoding='utf-8')
    f.write(html_doc)
    f.close()
