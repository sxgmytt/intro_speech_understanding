pip install SpeechRecognition

import speech_recognition as sr

def transcribe_flac(filename, language='en'):

    recognizer = sr.Recognizer()

    with sr.AudioFile(filename) as source:
        audio_data = recognizer.record(source)
        
        try:
            text = recognizer.recognize_google(audio_data, language=language)
            return text
        except sr.UnknownValueError:
            print("Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
    
    return None

filename = '264752__copyc4t__phone-messages-english-and-italian.flac'
recognized_text = transcribe_flac(filename, language='en')

if recognized_text:
    print(f"Recognized Text: {recognized_text}")
else:
    print("Failed to transcribe audio.")
