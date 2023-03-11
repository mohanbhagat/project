#Libraries===================================================================
from asyncio import sleep
from gtts import gTTS
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import random
import sys
import time
import os
import os.path
import requests
from requests import get
import pyjokes
from pywikihow import search_wikihow
import smtplib
from bs4 import BeautifulSoup 
import wolframalpha
import operator
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import operator
import chatbot
import googletrans
from Brain.AIBrain import ReplyBrain
import audioplayer
#import weather
import pyautogui





#engine = pyttsx3.init('sapi5')
#voices = engine.getProperty('voices')
#print(voices=[0].id)
#engine.setProperty('voice', voices[1].id)
#engine.setProperty('rate', 50)



def Speak(audio):
    #rate = 100
    #engine = pyttsx3.init()
    #voices = engine.getProperty('voices')
    #engine.setProperty('voice', voices[1].id)
    
    tts = gTTS(audio)
    tts.save("friday.mp3")
    audioplayer.AudioPlayer("friday.mp3").play(block=True)
    #engine.setProperty('rate', rate+70)
    #engine.say(audio)
    #engine.runAndWait()
    

def wishMe():

    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%H:%M")
    
    if hour >=0 and hour <  12:
        Speak(f'Good morning, its {tt}')


    elif hour >=12 and hour < 18:
        Speak(f'good Afternoon, its {tt}')

    else:
        Speak(f'good evening, its {tt}')
    
    
    Speak("I am  Nature. How may i help you")

#def fetch_weather(city):
    """
   # City to weather
    :param city: City
    :return: weather
    """
    #api_key = '21f1526515237b4d6959e1752267ae11'
    #units_format = "&units=metric"

    #base_url = "http://api.openweathermap.org/data/2.5/weather?q="
    #complete_url = base_url + city + "&appid=" + api_key + units_format

    #response = requests.get(complete_url)

    #city_weather_data = response.json()

    #if city_weather_data["cod"] != "404":
       # main_data = city_weather_data["main"]
        #weather_description_data = city_weather_data["weather"][0]
        #weather_description = weather_description_data["description"]
       # current_temperature = main_data["temp"]
        #current_pressure = main_data["pressure"]
        #current_humidity = main_data["humidity"]
        #wind_data = city_weather_data["wind"]
        #wind_speed = wind_data["speed"]

        #final_response = f"""
        #The weather in {city} is currently {weather_description} 
        #with a temperature of {current_temperature} degree celcius, 
        #atmospheric pressure of {current_pressure} hectoPascals, 
        #humidity of {current_humidity} percent 
        #and wind speed reaching {wind_speed} kilometers per hour"""

        #return final_response

    #else:
        #return "Sorry Sir, I couldn't find the city in my database. Please try again"
    
def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('projectreport122222@gmail.com','Mohan@1233')
    server.sendmail('projectreport122222', to, content)
    server.close()

def computational_intelligence(question):
    try:
        client = wolframalpha.Client('4223K8-3YPQHYY9PX')
        answer = client.query(question)
        answer = next(answer.results).text
        print(answer)
        return answer
    except:
        Speak("Sorry sir I couldn't fetch your question's answer. Please try again ")
        return None

def news():
    main_url = 'http://newsapi.org/v2/top-headlines?sources=techcrunch&apikey=85f08ee9d58847adaa89fe6eb0990b6c'
    main_page = requests.get(main_url).json()
    articles = main_page["articles"]
    head = []
    day = ["first","Second","third","fourth","fifth","sixth","seventh","eighth","ninth","tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range (len(day)):
        Speak(f"today's {day[i]} news is {head[i]}")

def days():
    """Returns present day"""
    day = datetime.datetime.today().weekday() + 1

    day_dict = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday",
    }

    if day in day_dict:
        day_of_the_week = day_dict[day]
        print(day_of_the_week)
        Speak("The day is " + day_of_the_week)

def date():
    """Returns present date"""
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date1 = int(datetime.datetime.now().day)
    Speak("the current date is")
    Speak(date1)
    Speak(month)
    Speak(year)
    

def ask(self):
    """Solve"""
    Speak("I can answer to computational questions")
    question = self.voicecom().lower()
    app_id = "4223K8-3YPQHYY9PX"
    client = wolframalpha.Client(app_id)
    res = client.query(question)
    answer = next(res.results).text

    Speak(answer)
    print(answer)

#def weather(self, city):
        #try:
           # res = weather.fetch_weather(city)
        #except Exception as e:
           # print(e)
           # res = False
        #return res 
    
def takeCommand():
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
       
        print("listening...")
        r.pause_threshold = 1.5
        audio = r.listen(source,timeout=5,phrase_time_limit=8 )

    try:
        print("Recognize...")
        query = r.recognize_google(audio, language='en-hi')
        print(f"user said :{query}\n")

    except:
        #print("say that again please...")
        return "none"
    query = query.lower()
    return query
 
 
#def MainExecution():
    #Data = str(Data)#
    #Reply = ReplyBrain(Data) 
    #Speak(Reply)
    
        
    
    
    
    
def TaskExecution():
    wishMe()
    while True:
        #Data = str(Data)
        query = takeCommand().lower()
                 
        if 'wikipedia' in query:  #if wikipedia found in the query then this block will be executed
            Speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) 
            Speak("According to Wikipedia")
            print(results)
            Speak(results)
        
        elif "calculate" in query:
                question = query
                answer = computational_intelligence(question)
                Speak(answer)
            
        elif "what is" in query or "who is" in query:                            
                question = query
                answer = computational_intelligence(question)
                Speak(answer)
                       
        elif "tell me a joke" in query:
            joke = pyjokes.get_joke()
            Speak(joke)
            
        elif "tell me news" in query:
            Speak("please wait sir, fetching the lastest news")
            news()
            
        elif "where i am" in query or "where we are" in query:
            Speak("wait sir, let me check")
            try:
                ipAdd = requests.get('https://api.ipify.org').text
                print(ipAdd)
                url = 'https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
                geo_requests = requests.get(url)
                geo_data = geo_requests.json()
                city = geo_data['city']
                country = geo_data['country']
                Speak(f"Sir i am not sure, but i think we are in {city} city of {country} country")
            except Exception as e:
                Speak("Sorry sir, Due to network issue i am not able to find where we are.")
                pass
        
        
        #elif " leave it" in condition or "leave for now" in condition:
            #Speak("Ok sir")
            
        elif 'play music' in query:
            Speak('Playing Music!')
            music_dir = 'C:\\Users\\Dell_owner\\Desktop\\12\\Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'stop music' in query:
            query('okay sir, closing Media Player')
            os.system()
            
        
            
        elif 'song please' in query or 'play some song' in query:
            Speak('Sir what song should i play...')
            song = takeCommand()
            webbrowser.open(f'https://open.spotify.com//search/{song}')
            sleep(13)
            pyautogui.click(x=1055, y=617)
            Speak('Playing' + song)
            
        
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            Speak(f"Sir, the time is {strTime}")
        
        elif 'Whats up' in query  or 'how are you' in query:
            stMsgs=['Just doing my thing!' ,'I am fine !', 'Nice sir!','I am okay! How are you']
            ans_q = random.choice(stMsgs)
            Speak(ans_q)
                    
        elif "activate how to do mode" in query:
            Speak("how to do mode is activated")
            while True:
                Speak("Please tell me what you want to know")
                how = takeCommand()
                try:
                    if"exit" in how or "close" in how:
                        Speak("okay sir, how to do moode is closed")
                        break
                    else:
                        max_results = 1
                        how_to = search_wikihow(how, max_results)
                        assert len(how_to) == 1
                        how_to[0].print()
                        Speak(how_to[0].summary)
                except Exception as e:
                    Speak("sorry sir, I am not able to find this")
        
        #elif 'search' in query:
           # Speak('What do you want to search for?')
           # search = takeCommand()
            #url = 'https://google.com/search?q=' + search
            #webbrowser.get('chrome').open_new_tab(url)
            #Speak('Here is What I found for' + search)

        
        #elif 'voice' in query:
            #if 'female' in query:
                #engine.setProperty('voice', voices[1].id)
            #else:
                #engine.setProperty('voice', voices[0].id)
            #Speak("Hello Sir, I have switched my voice. How is it?")

            
        
        #elif 'weather forecast' in query:
                #city = query.split(' ')[-1]
                #weather_res = weather(city=city)
                #print(weather_res)
                #Speak(weather_res)
                #fetch_weather()
        
        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy','i am okey ! How are you']
            ans_q = random.choice(stMsgs)
            Speak(ans_q)  
            ans_take_from_user_how_are_you = takeCommand()
            if 'fine' in ans_take_from_user_how_are_you or 'happy' in ans_take_from_user_how_are_you or 'okey' in ans_take_from_user_how_are_you:
                Speak('okey..')  
            elif 'not' in ans_take_from_user_how_are_you or 'sad' in ans_take_from_user_how_are_you or 'upset' in ans_take_from_user_how_are_you:
                Speak('oh sorry..')  
        elif 'make you' in query or 'created you' in query or 'develop you' in query:
            ans_m = " For your information Sachin Lohar Created me ! I give Lot of Thannks to Him "
            print(ans_m)
            Speak(ans_m)
        elif "who are you" in query or "about you" in query or "your details" in query:
            about = "I am Acro an A I based computer program but i can help you lot like a your close friend ! i promise you ! Simple try me to give simple command ! like playing music or video from your directory i also play video and song from web or online ! i can also entain you i so think you Understand me ! ok Lets Start "
            print(about)
            Speak(about)
        elif "hello" in query or "hello Acro" in query:
            hel = "Hello Sir ! How May i Help you.."
            print(hel)
            Speak(hel)
        elif "your name" in query or "sweat name" in query:
            na_me = "Thanks for Asking my name my self ! Acro"  
            print(na_me)
            Speak(na_me)
        elif "you feeling" in query:
            print("feeling Very sweet after meeting with you")
            Speak("feeling Very sweet after meeting with you")
        
         
        elif 'remember that' in query:
            Speak("what should i remember sir")
            rememberMessage = takeCommand()
            Speak("you said me to remember"+rememberMessage)
            remember = open('data.txt', 'w')
            remember.write(rememberMessage)
            remember.close()
            
        elif 'do you remember anything' in query:
            remember = open('data.txt', 'r')
            Speak("you said me to remember that" + remember.read())
                    
        elif ' lets talk' in query or 'can we talk' in query:
            Speak('why not sir.')
            chatbot()
            #kk = input("Enter :")
            #print(ReplyBrain(kk))
            #Reply = ReplyBrain(Data) 
            #Speak(ReplyBrain)
        
        elif "you can sleep" in query or "sleep now" in query:
            Speak("Okay sir, I am going to sleep you can call me anytime.")
            break
        Speak("Is their anything that i can do for you")       
        

                    


if __name__ == "__main__":
    while True:
        
        permission = takeCommand().lower()
        if "wake up nature" in permission or "hello nature" in permission:
            TaskExecution()
        elif "Take rest " in permission or "sleep" in permission:
            Speak("Thanks for using me using, call me anytime ill their for you")
            sys.exit()
            
        
            