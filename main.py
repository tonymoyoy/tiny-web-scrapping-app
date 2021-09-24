from flask import Flask
from selenium import webdriver
app = Flask(__name__)

# basic message
@app.route('/')
def hello():
        return "Is there anybody out there?"

# web scrapping with selenium, get title of the last post from my blog
@app.route('/blog')
def blog():
        # define webdriver options
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver",options=options)
        driver.get('https://moyoy.blogspot.com')
        # use xpath to locate the title of the last post
        last_post_xpath = '//*[@id="Blog1"]/div[1]/div[1]/div/div/div/h3/a'
        last_post_title = driver.find_element_by_xpath(last_post_xpath).text
        # close driver
        driver.quit()
        # return value
        return last_post_title

if __name__ == '__main__':
    app.run(host='0.0.0.0')

