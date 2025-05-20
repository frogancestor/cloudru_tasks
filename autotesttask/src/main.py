from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By

edge_options = Options()
edge_options.page_load_strategy = 'normal'
driver = webdriver.Edge(options=edge_options)

driver.get('https://example.com')

driverTitle = driver.title

titleKeyword = "Example"
if titleKeyword in driverTitle:
    print(f'"{titleKeyword}" keyword is in title')
else:
    print(f'No "{titleKeyword}" keyword in title')

link_element = 'More information'
try:
    moreInfo = driver.find_element(By.PARTIAL_LINK_TEXT, link_element)
    moreInfo.click()
except Exception as e:
    print(f'{link_element} is not found by PARTIAL_LINK_TEXT')

currentUrl = driver.current_url
if currentUrl == 'https://www.iana.org/help/example-domains':
    print(f'Current url is {currentUrl}')
else:
    print('Current url is not "https://www.iana.org/help/example-domains"')
    
driver.quit()