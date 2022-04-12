from multiprocessing import set_forkserver_preload
import pyttsx3 #text data to speech
import datetime
import time
import random
import speech_recognition as src #pip install Speech_Recognition == mic to text
import smtplib

from email.message import EmailMessage
import pyautogui
import webbrowser as wb
import wikipedia
import requests
from newsapi import NewsApiClient
import clipboard
#import pywhatkit 
import os
import pyjokes
import string


class Date():
    def __init__(self):
        pass
    def get_year(self):
        year = int(datetime.datetime.now().year)
        return year
    def get_month(self):
        month = int(datetime.datetime.now().month)
        return month
    def get_day(self):
        day = int(datetime.datetime.now().day)
        return day
    def date(self):
        year = int(datetime.datetime.now().year)
        month = int(datetime.datetime.now().month)
        day = int(datetime.datetime.now().day)
        result = f"{day}/{month}/{year}"
        return result



class Roll_a_dice():
    def __init__(self):
        pass
    def roll_dice(self):
        dice_list = ["1","2","3","4","5","6"]
        dice = random.choice(dice_list)
        return dice

class Google():
    def __init__(self):
        pass
    def search(self,search):
        wb.open("https://www.google.com/search?q=" + search)
        
    

class Flip():
    def __init__(self):
        pass
    def flip(self):
        coin = ["Heads","Tales"]
        result = random.choice(coin)
        return result
class Weather():
    def __init__(self):
        pass
    def weather_temp(self,city,api_key):
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&appid={api_key}" #USING OPENWEATHER API
        res = requests.get(url)
        data = res.json()
        temp = data["main"]["temp"] #fahrenheit
        temp = round((temp-32)*5/9) #to celcius
        return temp

    def weather_description(self,city,api_key):
          url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&appid={api_key}" #using OPENWEATHER API
          res = requests.get(url)
          data = res.json()
          desp = data["weather"] [0] ['description']
          return desp

class Password_generator():
    def __init__(self):
        pass
    def generate(self,passlength):
        s1 = string.ascii_uppercase
        s2 = string.ascii_lowercase
        s3 = string.digits
        s4 = string.punctuation
        
        s = []
        s.extend(list(s1))
        s.extend(list(s2))
        s.extend(list(s3))
        s.extend(list(s4))
        random.shuffle(s)
        newpass = ("".join(s[0:passlength]))
        return newpass

class Wikipedia():
    def __init__(self):
        pass
    def search(self,topic):
        topic = topic.replace("wikipedia",'')  
        result = wikipedia.summary(topic,sentences=2)  
        return result         

class Text_to_speech():
    def __init__(self):
        pass
    def convert_text(self,text):
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
class Joke():
    def __init__(self):
        pass
    def joke(self):
        result = pyjokes.get_joke()
        return result

class Day_time():
    def __init__(self):
        pass
    def time(self):
        time = datetime.datetime.now().strftime('%I:%M:%S')
        return time

class Get_word_of_string():
    def __init__(self):
        pass
    def get_word(self,word,index):
        word = word[index]
        return word

 


classDate = Date()
classRoll = Roll_a_dice()
class_Google = Google()
class_Flip = Flip()
class_Weather = Weather()
class_Password_Generator = Password_generator()
classWikipedia = Wikipedia()
class_Text_To_Speech = Text_to_speech()
classJoke = Joke()
classDay_time = Day_time()
classGet_word = Get_word_of_string()






        
    