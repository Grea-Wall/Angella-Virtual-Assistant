import speech_recognition as sr
import os
from gtts import gTTS
from playsound import playsound
import datetime
import warnings
import calendar
import random
import wikipedia
import webbrowser

warnings.filterwarnings('ignore')

def record_audio():
  r = sr.Recognizer()

  with sr.Microphone() as source:
    print("Hi ,I am Angela.I am your personal Assistant.How may I help you")
    audio = r.listen(source)
    data = ''
    try:
      data = r.recognize_google(audio)
      print(f"You said: {data}")
    except sr.UnknownValueError:
      print("Didn't understand! Want to try again")
    except sr.RequestError:
      print("Request Failed! Try Again")

  return data

def assistant_response(text):
  print(text)
  while True:
    try:
      obj = gTTS(text = text, lang = 'en', slow = False)
      obj.save('assitant_response.mp3')
      break
    except:
      print("Error! Trying Again...")
      break

  playsound('assitant_response.mp3')

def wake_words(text):
  WAKE_WORDS = ['Angela','angela','Angella','angella']

  text = text.lower()
  for phrase in WAKE_WORDS:
    if phrase in text:
      return True

  return False

def get_date():
  now = datetime.datetime.now()
  my_date = datetime.datetime.today()
  weekday = calendar.day_name[my_date.weekday()]
  monthNum = now.month
  dayNum = now.day

  month_name = ["january", "february", "march", "april", "may", "june","july", "august", "september","october","november", "december"]

  return f"Today is {weekday}, {dayNum} of {month_name[monthNum - 1]}"


def greeting(text):
  GREETINGS_INPUT = ['hi', 'yo', 'hello', 'hey']

  GREETINGS_OUTPUT = ['hello sir', 'how are you doing', 'hey']

  for word in text.split():
    if word.lower() in GREETINGS_INPUT:
      return random.choice(GREETINGS_OUTPUT)

  return ''


def getInfo(text):
  wordlist = text.split()

  for i in range(0, len(wordlist)):
    if i + 3 <= len(wordlist) -1 and wordlist[i].lower() == 'who' and wordlist[i+1].lower() == 'is':
      return f"{wordlist[i + 2]} {wordlist[i + 3]}"

while True:
  text = record_audio()
  response = ""

  if wake_words(text) == True:
    reponse = response + greeting(text)

    if 'date' in text:
      the_date = get_date()
      response = response + ' ' + the_date

    if 'who is' in text:
      person = getInfo(text)
      wiki = wikipedia.summary(person, sentences = 2)
      response = response + ' ' + wiki

    assistant_response(response)



    