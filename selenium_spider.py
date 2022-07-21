import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver_path = "./chrom-driver-94/chromedriver.exe"
browser = webdriver.Chrome(driver_path)

url = "https://juejin.cn/book/7069596046602534919/section/7070419009824358436"

browser.get(url)

# browser.add_cookie({'_ga':'GA1.2.551302045.1605795899'})
# browser.add_cookie({'MONITOR_WEB_ID':'e13c8a50-1e38-485d-8613-1231cea2d348'})
# browser.add_cookie({'__tea_cookie_tokens_2608':'%257B%2522web_id%2522%253A%25226896840858072679944%2522%252C%2522ssid%2522%253A%252219d32df5-c911-45fa-bd72-473ad62638fe%2522%252C%2522user_unique_id%2522%253A%25226896840858072679944%2522%252C%2522timestamp%2522%253A1626618792231%257D'})
# browser.add_cookie({'n_mh':'BV0owX9ixhphmaHMNVQVPonmbSBXtFmvd2f8rcwIUQo'})
# browser.add_cookie({'_gid':'GA1.2.491979819.1658156701'})
# browser.add_cookie({'passport_csrf_token':'e5ca6c47f2fb161a0af185ef00b59404'})
# browser.add_cookie({'passport_csrf_token_default':'e5ca6c47f2fb161a0af185ef00b59404'})
# browser.add_cookie({'sid_guard':'358c1a22b6a442089f69e9019f6b905c%7C1658159783%7C31536000%7CTue%2C+18-Jul-2023+15%3A56%3A23+GMT'})
# browser.add_cookie({'uid_tt':'322c4cdf7b38ab4af9c7bdcc56b4534b'})
# browser.add_cookie({'uid_tt_ss':'322c4cdf7b38ab4af9c7bdcc56b4534b'})
# browser.add_cookie({'sid_tt':'358c1a22b6a442089f69e9019f6b905c'})
# browser.add_cookie({'sessionid':'358c1a22b6a442089f69e9019f6b905c'})
# browser.add_cookie({'sessionid_ss':'358c1a22b6a442089f69e9019f6b905c'})
# browser.add_cookie({'sid_ucp_v1':'1.0.0-KDFmODUxZjAxYzA5MDc1MmE4Njc0NGNlMWRhYzVmNzM4MDAzYjgwYmMKFwiHq8C-_fXxBxCnhdaWBhiwFDgBQOoHGgJsZiIgMzU4YzFhMjJiNmE0NDIwODlmNjllOTAxOWY2YjkwNWM'})
# browser.add_cookie({'ssid_ucp_v1':'1.0.0-KDFmODUxZjAxYzA5MDc1MmE4Njc0NGNlMWRhYzVmNzM4MDAzYjgwYmMKFwiHq8C-_fXxBxCnhdaWBhiwFDgBQOoHGgJsZiIgMzU4YzFhMjJiNmE0NDIwODlmNjllOTAxOWY2YjkwNWM'})
# browser.add_cookie({'_tea_utm_cache_2608':'{%22utm_source%22:%22gold_browser_extension%22}'})
cookies = '_ga=GA1.2.551302045.1605795899; MONITOR_WEB_ID=e13c8a50-1e38-485d-8613-1231cea2d348; __tea_cookie_tokens_2608=%257B%2522web_id%2522%253A%25226896840858072679944%2522%252C%2522ssid%2522%253A%252219d32df5-c911-45fa-bd72-473ad62638fe%2522%252C%2522user_unique_id%2522%253A%25226896840858072679944%2522%252C%2522timestamp%2522%253A1626618792231%257D; n_mh=BV0owX9ixhphmaHMNVQVPonmbSBXtFmvd2f8rcwIUQo; _gid=GA1.2.491979819.1658156701; passport_csrf_token=e5ca6c47f2fb161a0af185ef00b59404; passport_csrf_token_default=e5ca6c47f2fb161a0af185ef00b59404; _tea_utm_cache_2018=undefined; sid_guard=358c1a22b6a442089f69e9019f6b905c%7C1658159783%7C31536000%7CTue%2C+18-Jul-2023+15%3A56%3A23+GMT; uid_tt=322c4cdf7b38ab4af9c7bdcc56b4534b; uid_tt_ss=322c4cdf7b38ab4af9c7bdcc56b4534b; sid_tt=358c1a22b6a442089f69e9019f6b905c; sessionid=358c1a22b6a442089f69e9019f6b905c; sessionid_ss=358c1a22b6a442089f69e9019f6b905c; sid_ucp_v1=1.0.0-KDFmODUxZjAxYzA5MDc1MmE4Njc0NGNlMWRhYzVmNzM4MDAzYjgwYmMKFwiHq8C-_fXxBxCnhdaWBhiwFDgBQOoHGgJsZiIgMzU4YzFhMjJiNmE0NDIwODlmNjllOTAxOWY2YjkwNWM; ssid_ucp_v1=1.0.0-KDFmODUxZjAxYzA5MDc1MmE4Njc0NGNlMWRhYzVmNzM4MDAzYjgwYmMKFwiHq8C-_fXxBxCnhdaWBhiwFDgBQOoHGgJsZiIgMzU4YzFhMjJiNmE0NDIwODlmNjllOTAxOWY2YjkwNWM; _tea_utm_cache_2608={%22utm_source%22:%22gold_browser_extension%22}'
cookie_items = cookies.split(";")


for item in cookie_items:
    key_value = item.split("=")
    key = key_value[0]
    value = key_value[1]
    cookie_dict = {}
    cookie_dict = {
        'name': key.strip(),
        'value': value.strip()
    }
    print(cookie_dict)
    browser.add_cookie(cookie_dict)

time.sleep(2)
# 刷新页面
browser.refresh()

time.sleep(3)
content = browser.find_elements(by=By.CLASS_NAME, value="markdown-body")
print(len(content))
text = content[0].get_attribute("innerHTML")
print(text)

# chrome headless
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
#
# chrome_options = Options()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')
#
# path = 'C:\Program Files\Google\Chrome\Application\chrome.exe'
#
# chrome_options.binary_location = path
#
# browser = webdriver.Chrome(chrome_options=chrome_options)
#
# url = "https://juejin.cn/book/7069596046602534919/section/7070419009790803976"
# browser.get(url)
#
# content = browser.find_elements(by=By.CLASS_NAME, value="markdown-body")
# text = content[0].get_attribute("innerHTML")
# print(text)