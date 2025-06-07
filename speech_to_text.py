import speech_recognition as sr

r = sr.Recognizer()

def record_text():
    while True:
        try:
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source, duration=0.2)
                print("Listening, Please speak...")
                audio = r.listen(source)
                myText = r.recognize_google(audio)
                return myText.lower()
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
        except sr.UnknownValueError:
            print("Unknown error occurred")

def output_text(text):
    with open("output.txt", "a") as f:
        f.write(text + "\n")
    print(f"Written text: {text}")

def clear_file():
    with open("output.txt", "w") as f:
        pass  
    print("output.txt cleared!")

while True:
    text = record_text()
    if text in ["exit", "stop", "quit"]:
        print("Stopping program as requested.")
        break
    elif text == "clear":
        clear_file()
    else:
        output_text(text)
