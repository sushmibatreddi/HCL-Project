from django.shortcuts import render
import wikipedia

def home(request):


    return render(request,'home.html')


def speak(request):

    user_input = request.POST.get('search')

    # pip install pyttsx3 pypiwin32
    import pyttsx3

    # One time initialization
    engine = pyttsx3.init()

    # Set properties _before_ you add things to say
    engine.setProperty('rate', 130)  # Speed percent (can go over 100)
    engine.setProperty('volume', 0.9)  # Volume 0-1

    # Queue up things to say.
    # There will be a short break between each one
    # when spoken, like a pause between sentences.
    engine.say(user_input)


    # Flush the say() queue and play the audio
    engine.runAndWait()

    # Program will not continue execution until
    # all speech is done talking

    return render(request,'speak.html')




def speech_to_text(request):
    data = request.POST.get('record')
    import speech_recognition as sr

    # get audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak:")
        audio = r.listen(source)

    try:
        output = " " + r.recognize_google(audio)
    except sr.UnknownValueError:
        output = "Could not understand audio"
    except sr.RequestError as e:
        output = "Could not request results; {0}".format(e)
    data =output

    return render(request,'speech_to_text.html',{'data':data})