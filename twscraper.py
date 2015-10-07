import sys
import mechanize
from bs4 import BeautifulSoup
import getpass

class Twitter(object):

    def __init__(self):
        self.tweetnum = 0
        self.br = mechanize.Browser()
        self.br.set_handle_robots(False)
        self.br.open("https://www.twitter.com/")

    def login(self):
        print "----------------------------------\nYou are now at log in screen\ntype your information below"
        self.username = raw_input("username/email: ")
        self.password = getpass.getpass("password: ")
        self.br.select_form(nr=1)
        self.br["session[username_or_email]"] = self.username
        self.br["session[password]"] = self.password
        self.response = self.br.submit()
        print "you've logged in!"

    def searchTweets(self):
        twitterfriend = '#' + raw_input("search tweets: #")
        self.br.select_form(nr=0)
        self.br['q'] = twitterfriend
        response1 = self.br.submit()
        self.html = BeautifulSoup(response1.read(), 'lxml')
        return self.html

    def collectTweets(self):
        for tweet in self.html.findAll('p', {'class':'TweetTextSize  js-tweet-text tweet-text'}):
            self.tweetnum += 1
            print "-------------------------------\n",self.tweetnum ,tweet.text,"\n-------------------------------"

    def tweetsAtHome(self):
        self.htmlHome = BeautifulSoup(self.response.read(), 'lxml')
        for tweet in self.htmlHome.findAll('p', {'class':'TweetTextSize  js-tweet-text tweet-text'}):
            self.tweetnum += 1
            print "-------------------------------\n",self.tweetnum ,tweet.text,"\n-------------------------------"


def frontscreen():
    print """
------------Twitter--------------
Welcome to twitter!

Connect with your friends-and
other fascinating people. Get
in-the-moment updates on the
things that interest you. And
watch events unfold, in real
time, from every angle

press c to prepare log-in screen
press x to exit program
    """

    while True:
        usercommand = raw_input(": ")
        if usercommand == 'c':
            return usercommand
            break
        elif usercommand == 'x':
            try:
                sys.exit(1)
            except SystemExit as e:
                sys.exit(e)
        else:
            print "invalid input!"
            print "press c to prepare log-in screen"
            print "press x to exit program"

def homePage():

    userCommand = raw_input("\nThis is twitter home page\n\npress 'l' to get latests tweets\npress 's' to search tweets\nTo exit press 'x'\n:")
    return userCommand

if __name__ == "__main__":
    fsReturn = frontscreen()
    if fsReturn == 'c':
        attempt = Twitter()
        attempt.login()
        while True:
            hpReturn = homePage()
            if hpReturn == 'l':
                attempt.tweetsAtHome()
            elif hpReturn == 's':
                attempt.searchTweets()
                attempt.collectTweets()
            elif hpReturn == 'x':
                sys.exit(0)
            else:
                print "invalid input"
