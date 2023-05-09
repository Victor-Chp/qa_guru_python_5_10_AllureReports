from selene import browser

def test_github():
    browser.open('https://github.com')
    browser.element('.header-search-input').click()
    browser.element('.header-search-input').send_keys('eroshenkoam/allure-example')
    browser.element('.header-search-input').submit()

    browser.element()
    ...