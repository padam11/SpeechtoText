import speech_recognition as sr

x = sr.Recognizer()

with sr.Microphone() as source:
    print("Begin Talking.")
    audion = x.listen(source)
    print("It's been done.")
    try:
        print("Text: "+x.recognize_google(audion))
    except:
        print("Didn't work, sorry.")
