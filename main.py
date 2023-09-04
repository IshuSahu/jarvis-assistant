import pyttsx3
import speech_recognition as sr
import pyautogui
import datetime
import wikipedia
import webbrowser
import os
import subprocess
import time
import random
from bs4 import BeautifulSoup
import requests
from googlesearch import search
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie  # using this we can show GIFs
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from JarvisNui import Ui_MainWindow

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def WishMee():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        jarvis.terminalPrint("Good morning!")
        speak("Good morning!")

    elif hour >= 12 and hour < 18:
        jarvis.terminalPrint("Good Afternoon!")
        speak("Good Afternoon!")

    else:
        jarvis.terminalPrint("Good Evening !")
        speak("Good Evening !")

    speak("Initializing Jarvis")
    # speak("Starting all systems applications")
    # speak("Checking the internet connection")
    # speak("Wait a moment sir")
    # speak("All drivers are up and running")
    # speak("All systems have been activated")
    # speak("Now I am online")
    # speak("I am jarvis sir ur Dekstop assitant, please tell how may i help you?")
    jarvis.terminalPrint(
        "I am jarvis sir ur Dekstop Assistant, please tell how may i help you?")

r = sr.Recognizer()
class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()

    def run(self):
        self.TaskExecution()

    def takeCommand(self):
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=1)
            jarvis.terminalPrint("Listening...")
            audio = r.listen(source)
        try:
            jarvis.terminalPrint("Recognizing....")
            self.query = r.recognize_google(audio, language='en-in')
            jarvis.terminalPrint(f"user said:{self.query}\n")

        except Exception as e:
            jarvis.terminalPrint("say that again please...")
            self.query = "None"
        return self.query
    
    # this is Command program start here
    def TakeIntCommand(self):
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=1)
            jarvis.terminalPrint("Listening...")
            audio = r.listen(source)
        try:
            jarvis.terminalPrint("Recognizing....")
            command = r.recognize_google(audio, language='en-in')
            jarvis.terminalPrint(f"user said: {command}\n")

            # Convert the recognized command to an integer if possible
            if command.isdigit():
                return int(command)
            else:
                return command

        except Exception as e:
            jarvis.terminalPrint("say that again please...")
            return "None"

    def TaskExecution(self):
        WishMee()
        while True:
            self.query = self.takeCommand().lower()
            # logic for executing tasks based commd
            if self.query == "None":
                self.query = self.takeCommand().lower()
            if 'wikipedia' in self.query:
                speak("searching in wikipedia....")
                self.query = self.query.replace("wikipedia", "")
                results = wikipedia.summary(self.query, sentences=3)
                speak("According to wikipedia")
                jarvis.terminalPrint(results)
                speak(results)

            elif ('hello' in self.query) or ('hello jarvis' in self.query):
                speak("hello sir")

            elif ('jarvis are you there' in self.query) or ('jarvis you up' in self.query):
                speak("For you sir, Always!")

            elif ('what you do' in self.query) or ('what can you do' in self.query) or ('what task you perform' in self.query):
                jarvis.terminalPrint("I can perform various tasks, fuctionality which are provided by master sir \n"
                                     "For Example: wheather details, time, searching query from Wikipedia, play music, shutdown window, open application, open Browser like (Youtube, Google, facebook) and search, top 5 News headline from Times of India, taking note, note down to remember something, telling master what i remember, taking screenshot etc")
                speak("I can perform various talks which is his program inside my jarvis sir \n"
                                     "For Example: wheather details, time, searching query from Wikipedia, play music, shutdown window, open application, open Browser like (Youtube, Google, facebook) and search, top 5 News headline from Times of India, taking note, note down to remember something, telling master what i remember, taking screenshot etc")

            elif 'jarvis who made you' in self.query:
                speak("Yes Sir, my master build me in AI")


            elif ('play guessing game' in self.query) or ('number guessing game' in self.query) or ('play game' in self.query):
                speak("Sure, let's play a guessing game.")
                jarvis.terminalPrint("Sure, let's play a guessing game.")
                number = random.randint(1, 10)
                guesses = 0
                while True:
                    speak("Guess a number between 1 and 10: ")
                    guess = self.TakeIntCommand().lower()
                    if guess.isdigit():
                        guess = int(guess)
                        guesses += 1
                        if guess == number:
                            speak(f"Congratulations! You guessed the number in {guesses} guesses.")
                            break
                        elif guess < number:
                            speak("The number is higher. Guess again.")
                        else:
                            speak("The number is lower. Guess again.")
                    else:
                        speak("Please enter a valid number.")



            elif ('open youtube' in self.query) or ('onine song' in self.query) or ('search youtube' in self.query):
                speak('What do you want to search on youtube for?')
                search = self.takeCommand()
                webbrowser.open_new_tab(
                    f"https://www.youtube.com/search?q={search}")
                speak('Here is What I found for' + search)

            if 'open google' in self.query or 'open on google' in self.query or 'search' in self.query:
                speak('What do you want to search on Google for?')
                search = self.takeCommand()
                webbrowser.open_new_tab(f"https://www.google.com/search?q={search}")
                speak('Here is what I found for ' + search)


            elif 'open facebook' in self.query:
                speak("Openeing facebook")
                webbrowser.open("https://www.facebook.com/")

            elif 'open stackoverflow' in self.query:
                speak("Openeing stackoverflow")
                webbrowser.open("https://stackoverflow.com/")

            elif ('play song' in self.query) or ('play music' in self.query) or ('play my song' in self.query):
                # music_dir = 'G:\\JanakjiLapyData\\JanakjiDataFDrive\\other song'
                music_dir = 'G:\JanakjiLapyData\JanakjiDataEDrive\\project'
                songs = os.listdir(music_dir)
                # print(songs)
                jarvis.terminalPrint("playing song....")
                os.startfile(os.path.join(music_dir, random.choice(songs)))

            elif 'the time' in self.query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"sir, the time is {strTime}")

            elif ('open code' in self.query) or ('open vs code' in self.query) or ('open vscode' in self.query):
                codepath = "C:\\Users\\Windows\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(codepath)

            elif ('temperature' in self.query) or ('tell me the temperature' in self.query) or ('weather' in self.query) or ('weather forecast' in self.query) or ('Nagpur weather' in self.query):
                city = "Nagpur"
                url = f"https://www.google.com/search?q={city}+weather"
                html = requests.get(url).content
                soup = BeautifulSoup(html, 'html.parser')
                temp = soup.find(
                    'div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
                desc = soup.find(
                    'div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text
                speak("Temperature:"+temp)
                jarvis.terminalPrint(f"Temperature: {temp}")
                speak("Weather description: "+desc)
                jarvis.terminalPrint(f"Weather description: {desc}")

            elif 'shutdown' in self.query:
                speak("Are you sure you want to shut down your computer?")
                response = input("Type 'yes' to confirm or 'no' to cancel: ")
                if response.lower() == 'yes':
                    speak("Shutting down your computer.")
                    os.system("shutdown /s /t 1")
                else:
                    speak("Shutdown cancelled.")

            elif ('screenshot' in self.query) or ('take screenshot' in self.query):
                speak("taking screenshot")
                image = pyautogui.screenshot()
                image.save("screenshot.png")

            elif 'shutdown system' in self.query:
                shutdown = jarvis.terminalPrint.input(
                    "Do you wish to shutdown your computer ? (yes / no): ")
                speak("Do you wish to shutdown system")
                if shutdown == 'no':
                    exit()
                else:
                    os.system("shutdown /s /t 1")

            elif ('news headline' in self.query) or ('read headline' in self.query) or ('todays news' in self.query) or ('todays top news' in self.query):

                url = requests.get(
                    "https://timesofindia.indiatimes.com/briefs")
                toi_soup = BeautifulSoup(url.content, 'html.parser')
                toi_headings = toi_soup.find_all('h2')
                toi_headings = toi_headings[2:-13]
                toi_news = []
                for th in toi_headings:
                    toi_news.append(th.text)

                for news in toi_news[:5]:
                    jarvis.terminalPrint(news)
                    speak(news)

            elif ("open notepad" in self.query) or ("make a note" in self.query) or ("notepad" in self.query) or ("editor" in self.query) or ("9" in self.query):
                pyttsx3.speak("Opening NOTEPAD")
                os.system("start notepad")
                write = self.takeCommand()
                pyautogui.write(write, interval=0.1)
                now = datetime.datetime.now()
                filename = f"note_{now.strftime('%Y-%m-%d_%H-%M-%S')}.txt"
                pyautogui.hotkey("ctrl", "s")
                time.sleep(1)  # wait for Save As dialog to appear
                pyautogui.write(filename, interval=0.1)
                pyautogui.press("enter")
                speak("Note saved.")

            elif ("open vlc" in self.query) or ("vlc media" in self.query) or ("open vlc media" in self.query) or ("vlc media player" in self.query) or ("open music player" in self.query) or ("music player" in self.query):
                pyttsx3.speak("Opening vlc media player")
                subprocess.call(["vlc"])

            elif ('remember that' in self.query) or ('take a note' in self.query) or ('note down' in self.query):
                speak("what should i remember sir")
                rememberMessage = self.takeCommand()
                speak("you said me to remember"+rememberMessage)
                remember = open('data.txt', 'w')
                remember.write(rememberMessage)
                remember.close()
            elif ('do you remember anything' in self.query) or ('speak what you remember' in self.query):
                remember = open('data.txt', 'r')
                speak("you said me to remember that" + remember.read())

            elif ("exit" in self.query) or ("Home" in self.query):
                speak("Goodbye sir!")
                exit()
            
            
startExecution = MainThread()

# This is for ui interface
class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)  # this line give u pop for the ui

        # for buttons
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(
            self.close)  # automatically terminate
        self.ui.pushButton_3.clicked.connect(
            self.ManualcodeInTerminal)  # automatically terminate
        self.show()
    # to add text in UI terminal

    def terminalPrint(self, text):
        self.ui.plainTextEdit.appendPlainText(text)

    def ManualcodeInTerminal(self):
        if self.ui.lineEdit.text():
            cmd = self.ui.lineEdit.text()
            self.ui.lineEdit.clear()
            self.ui.plainTextEdit.appendPlainText(f"You Type--> {cmd}")

            if cmd == "exit":
                jarvis.close()
            elif cmd == "help":
                self.terminalPrint("I can perform various talks which is his program inside my jarvis sir \n"
                                   "For Example: time,searching from Wikipedia, play music, shutdown window, open application, open Browser like (Youtube, Google, facebook),top 5 News headline etc")
            else:
                pass

    def startTask(self):
        # change according to your directory:
        self.ui.movie = QtGui.QMovie(
            "F:\\GITHUB\\JarvisGUI\\Images\\jarvis.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie(
            "F:\\GITHUB\\JarvisGUI\\Images\\Jlogo.gif")
        self.ui.label_3.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie(
            "F:\\GITHUB\\JarvisGUI\\Images\\inilializing.gif")
        self.ui.label_4.setMovie(self.ui.movie)
        self.ui.movie.start()

        # for timeer
        timer = QTimer(self)
        timer.timeout.connect(self.showtime)
        timer.start(1000)
        startExecution.start()

    # we have to shoow time
    def showtime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date = current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)


# now after all this stuff we have to show our ui

app = QApplication([])
jarvis = Main()
jarvis.show()
exit(app.exec_())



