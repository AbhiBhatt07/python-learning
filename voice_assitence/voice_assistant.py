import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os

# initialize speech to text engine. 
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 150)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening.")
        recognizer.push_threshold = 1
        audio = recognizer.listen(source)

    try: 
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"Your said: {query}\n")
    except Exception as e: 
        print("⚠️ Could not understand. Please say that again.")
        return 'None'
    return query.lower()

def respond_to_command(command):
    """Respond to voice commands with specific actions."""
    
    if 'time' in command:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The time is {current_time}")

    elif 'date' in command:
        current_date = datetime.datetime.now().strftime("%A, %d %B %Y")
        speak(f"Today is {current_date}")

    elif 'open youtube' in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif 'open google' in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif 'play music' in command:
        music_dir = 'E:\\songs'  # Change this path to a folder with music
        songs = os.listdir(music_dir)
        if songs:
            speak("Playing music")
            os.startfile(os.path.join(music_dir, songs[0]))
        else:
            speak("No music found in the music folder.")

    elif 'exit' in command or 'bye' in command:
        speak("Goodbye! Have a great day.")
        exit()

    else:
        speak("Sorry, I didn’t understand that command.")

# Main function: starts the assistant
if __name__ == "__main__":
    speak("Hello! I am your voice assistant. How can I help you today?")
    
    while True:
        user_command = take_command()
        if user_command != "None":
            respond_to_command(user_command)