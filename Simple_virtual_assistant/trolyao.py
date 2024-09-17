#Thu vien
import speech_recognition
import pyttsx3
from datetime import date, datetime

#Khoi tao
robot_ear = speech_recognition.Recognizer()
robot_month = pyttsx3.init()
robot_brain = ""

while True:
    #Nghe
    with speech_recognition.Microphone() as mic:
        print("Robot : I'm Listening")
        audio =robot_ear.record(mic, duration=5)

    print("Robot: ...")
    try:
        you = robot_ear.recognize_google(audio)
    except:
        you=""
    print("You: "+ you)


    #Hieu

    if you == "":
        robot_brain = "I can't hear you, try again"
    elif "hello" in you:
        robot_brain = "Hello"
    elif "today" in you:
        today = date.today()
        robot_brain = today.strftime("%B %d, %Y")
    elif "time" in you:
        now = datetime.now()
        robot_brain = now.strftime("%H hours %M minutes, %S seconds")
    elif ("president" in you and "America" in you):
        robot_brain = "Joe Biden"
    elif "bye" in you:
        robot_brain = "Bye Windy, See you soon"
        print("Robot: "+ robot_brain)
        robot_month.say(robot_brain)
        robot_month.runAndWait()
        break
    else:
        robot_brain = "I'm fine thank you and you"

    #Noi
    print("Robot: "+ robot_brain)
    robot_month.say(robot_brain)
    robot_month.runAndWait()