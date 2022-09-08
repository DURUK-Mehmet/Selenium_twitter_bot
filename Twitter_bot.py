from userinfo import email,password,tweet
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class Twitter:
    def __init__(self,email,password,tweet):
        self.browser = webdriver.Chrome()
        self.email = email
        self.password = password
        self.tweet=tweet
    def signIn(self):
        self.browser.get("https://twitter.com/login")
        time.sleep(3)

        emailInput = self.browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input")
        passwordInput = self.browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input")
        time.sleep(5)

        emailInput.send_keys(self.email)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(5)
    def tweeting(self):
        self.browser.get("https://twitter.com/home")
        time.sleep(3)
        tweetingInput = self.browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div")
        tweetingInput.send_keys(self.tweet)
        time.sleep(2)
        tweetingInput.send_keys(Keys.CONTROL+Keys.ENTER)

twtr = Twitter(email,password,tweet)
twtr.signIn()
twtr.tweeting()
