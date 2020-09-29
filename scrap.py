from bs4 import BeautifulSoup
import requests
import sys
import pyttsx3
from selenium import webdriver
import time

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def audioBook():

    res = requests.get('https://en.wikipedia.org/wiki/' + ' '.join(sys.argv[1:]))
    res.raise_for_status()

   #initialise browser.
    driver = webdriver.Chrome("C:/Users/Yadnesh/Downloads/chromedriver_win32 (1)/chromedriver.exe")
    driver.get('https://en.wikipedia.org/wiki/' + ' '.join(sys.argv[1:]))

    soup = BeautifulSoup(res.text, 'html.parser')
    count = 0
    print(count)


    for i in soup.select('p'):

        speak(i.getText())

        count += 1

        if count > 4:
            speak('Terminating.')
            break


    driver.close()

# gives today's top news headlines.
def givenews():
    apiKey = '49e391e7066c4158937096fb5e55fb5d'
    url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={apiKey}"
    r = requests.get(url)
    data = r.json()
    data = data["articles"]
    flag = True
    count = 0
    for items in data:
        count += 1
        if count > 2:
            break

        say = items["title"].split(" - ")[0]
        if flag:
            speak("Today's top 2 headlines are - ")
            flag = False
        else:
            speak("Next news :")
        speak(say)

if __name__ == "__main__":
    # givenews()
     audioBook()


