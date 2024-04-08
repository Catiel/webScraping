import time
import random
from playwright.sync_api import sync_playwright

def dowload_zillow_page(page, url):
    for i in range(3):
        response = page.goto(url, wait_until='domcontentloaded')
        if response.status == 404:
            print(f'Error 404: Page {url} not found. Trying again...')
            continue

        if not page.title().startswith('60661'):
            print(f'Error: Page title does not start with 60657. Current title: {page.title()}')
            page.close()
            time.sleep(5)
            page = browser.new_page(java_script_enabled=True)
            continue

        target_element = page.query_selector('//div[@id="search-page-list-container"]')
        for i in range(12):
            target_element.evaluate("element => element.scrollBy(0, 500)")
            time.sleep(0.5)

        with open(
                f'html-exports/zillow_{city_name}-{state}-{zip_code}_{page_num}.html',
                'w', encoding='utf-8') as f:
            f.write(target_element.inner_html())
        print(f'Page {page_num} downloaded')
        return True

    print(f'Error: Could not download the page after 3 attempts. URL: {url}')
    return False


playwright = sync_playwright().start()

browser = playwright.chromium.launch(
    headless=False,
    args=["--disble-blink-features=AutomationControlled"],
)

city_name = 'Chicago'.replace(' ', '-')
state = 'il'
zip_code = '60661'

for page_num in range(2, 4):
    page = browser.new_page(java_script_enabled=True)
    url = f'https://www.zillow.com/{city_name}-{state}-{zip_code}/{page_num}_p'
    print(url)
    if not dowload_zillow_page(page, url):
        raise Exception(f'Error: Page {url} not found')

    page.close()
    time.sleep(random.randint(100, 200))
browser.close()
playwright.stop()